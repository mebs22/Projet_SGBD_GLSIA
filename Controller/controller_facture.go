package controller

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"

	config "first.go/Config"
	model "first.go/Model"
	"github.com/gorilla/mux"
)

func AllFacture(w http.ResponseWriter, r *http.Request) {
	var facture model.Facture
	var response model.Response_facture
	var arrFacture []model.Facture

	db := config.Connect()
	defer db.Close()

	rows, err := db.Query("SELECT * FROM facture")

	if err != nil {
		log.Print(err)
	}

	for rows.Next() {
		err = rows.Scan(&facture.Numero, &facture.Total, &facture.Annexe)
		if err != nil {
			log.Fatal(err.Error())
		} else {
			arrFacture = append(arrFacture, facture)
		}
	}

	response.Status = 200
	response.Message = "Success"
	response.Data = arrFacture

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

// ---------------------------------------------------------------INSERT-----------------------------------------------------------------
func InsertFacture(w http.ResponseWriter, r *http.Request) {
	var response model.Response_facture

	db := config.Connect()
	defer db.Close()

	err := r.ParseMultipartForm(4096)
	if err != nil {
		panic(err)
	}
	total := r.FormValue("total_a_payer")
	annexe := r.FormValue("id_annexes")

	_, err = db.Exec("INSERT INTO facture(total_a_payer,id_annexes) VALUES(?, ?)", total, annexe)

	if err != nil {
		log.Print(err)
		return
	}
	response.Status = 200
	response.Message = "Insert data successfully \n"
	fmt.Print("Insert data to database")

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

//------------------------------------------------------ GET_BY_ID ------------------------------------------------------------

func GetFactureById(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'identifiant de la chambre dans les paramètres de l'URL
	params := mux.Vars(r)
	id, err := strconv.Atoi(params["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Connexion à la base de données
	db, err := sql.Open("mysql", "apache:@tcp(127.0.0.1:3308)/hotel")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer db.Close()

	// Exécution de la requête de sélection
	row := db.QueryRow("SELECT * FROM facture WHERE numeroFacture = ?", id)

	// Récupération des données de la chambre
	var facture model.Facture
	err = row.Scan(&facture.Numero, &facture.Total, &facture.Annexe)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Création de la réponse
	response, err := json.Marshal(facture)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Envoi de la réponse
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write(response)
}

//---------------------------------------------------------- DELETE ------------------------------------------------------------------

func DeleteFacture(w http.ResponseWriter, r *http.Request) {
	idStr := mux.Vars(r)["id"]
	id, err := strconv.Atoi(idStr)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Connexion à la base de données
	db, err := sql.Open("mysql", "apache:@tcp(127.0.0.1:3308)/hotel")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer db.Close()

	// Exécution de la requête de suppression
	result, err := db.Exec("DELETE FROM facture WHERE numeroFacture = ?", id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "data not found", http.StatusNotFound)
		return
	}

	// Envoie de la réponse
	response := model.Response_facture{
		Status:  http.StatusOK,
		Message: "data deleted successfully",
		Data:    nil,
	}
	jsonResponse, err := json.Marshal(response)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonResponse)
}

// ---------------------------------------------------------- UPDATE ------------------------------------------------------------------
func UpdateFacture(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	idFacture, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Lecture des données à partir du corps de la requête
	var facture model.Facture
	err = json.NewDecoder(r.Body).Decode(&facture)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Connexion à la base de données
	db, err := sql.Open("mysql", "apache:@tcp(127.0.0.1:3308)/hotel")
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer db.Close()

	// Exécution de la requête de mise à jour
	result, err := db.Exec("UPDATE facture SET total_a_payer = ?, id_annexes = ? WHERE numeroFacture = ?", &facture.Total, &facture.Annexe, idFacture)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "Data not found", http.StatusNotFound)
		return
	}

	// Création de la réponse
	response := model.Response_niveau{
		Status:  http.StatusOK,
		Message: "Data updated successfully",
		Data:    nil,
	}
	jsonResponse, err := json.Marshal(response)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jsonResponse)
}
