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

func AllAnnexe(w http.ResponseWriter, r *http.Request) {
	var annexe model.Annexe
	var response model.Response_annexe
	var arrAnnexe []model.Annexe

	db := config.Connect()
	defer db.Close()

	rows, err := db.Query("SELECT * FROM annexes")

	if err != nil {
		log.Print(err)
	}

	for rows.Next() {
		err = rows.Scan(&annexe.Numero, &annexe.Recettes, &annexe.NombreClient, &annexe.Mois)
		if err != nil {
			log.Fatal(err.Error())
		} else {
			arrAnnexe = append(arrAnnexe, annexe)
		}
	}

	response.Status = 200
	response.Message = "Success"
	response.Data = arrAnnexe

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

// ---------------------------------------------------------------INSERT-----------------------------------------------------------------
func InsertAnnexe(w http.ResponseWriter, r *http.Request) {
	var response model.Response_annexe

	db := config.Connect()
	defer db.Close()

	err := r.ParseMultipartForm(4096)
	if err != nil {
		panic(err)
	}
	recettes := r.FormValue("recettes")
	nombreClient := r.FormValue("nombreClient")
	mois := r.FormValue("mois")

	_, err = db.Exec("INSERT INTO annexes(recettes,nombreClient,mois) VALUES(?, ?, ?)", recettes, nombreClient, mois)

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

func GetAnnexeById(w http.ResponseWriter, r *http.Request) {
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
	row := db.QueryRow("SELECT * FROM annexes WHERE id_annexes = ?", id)

	// Récupération des données
	var annexe model.Annexe
	err = row.Scan(&annexe.Numero, &annexe.Recettes, &annexe.NombreClient, &annexe.Mois)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Création de la réponse
	response, err := json.Marshal(annexe)
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

func DeleteAnnexe(w http.ResponseWriter, r *http.Request) {
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
	result, err := db.Exec("DELETE FROM annexes WHERE id_annexes = ?", id)
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
	response := model.Response_annexe{
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
func UpdateAnnexe(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	idAnnexe, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Lecture des données à partir du corps de la requête
	var annexe model.Annexe
	err = json.NewDecoder(r.Body).Decode(&annexe)
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
	result, err := db.Exec("UPDATE annexes SET recettes = ?, nombreClient = ?,  mois = ? WHERE id_annexes = ?", &annexe.Recettes, &annexe.NombreClient, &annexe.Mois, idAnnexe)
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
