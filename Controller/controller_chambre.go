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

//----------------------------------------------GET_ALL-----------------------------------------------------------

func AllChambre(w http.ResponseWriter, r *http.Request) {
	var chambre model.Chambre
	var response model.Response_chambre
	var arrChambre []model.Chambre

	db := config.Connect()
	defer db.Close()

	rows, err := db.Query("SELECT * FROM chambre")

	if err != nil {
		log.Print(err)
	}

	for rows.Next() {
		err = rows.Scan(&chambre.Numero, &chambre.Classe, &chambre.Etat, &chambre.TarifChambre, &chambre.Numero_niveau)
		if err != nil {
			log.Fatal(err.Error())
		} else {
			arrChambre = append(arrChambre, chambre)
		}
	}

	response.Status = 200
	response.Message = "Success"
	response.Data = arrChambre

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

// ---------------------------------------------------------------INSERT-----------------------------------------------------------------
func InsertChambre(w http.ResponseWriter, r *http.Request) {
	var response model.Response_chambre

	db := config.Connect()
	defer db.Close()

	err := r.ParseMultipartForm(4096)
	if err != nil {
		panic(err)
	}
	classe := r.FormValue("classe")
	etat := r.FormValue("etat")
	tarifChambre := r.FormValue("tarifChambre")
	niveau_numeroNiveau := r.FormValue("niveau_numeroNiveau")

	_, err = db.Exec("INSERT INTO chambre(classe, etat, tarifChambre, niveau_numeroNiveau) VALUES(?, ?, ?, ?)", classe, etat, tarifChambre, niveau_numeroNiveau)

	if err != nil {
		log.Print(err)
		return
	}
	response.Status = 200
	response.Message = "Insert data successfully"
	fmt.Print("Insert data to database")

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

//------------------------------------------------------ GET_BY_ID ------------------------------------------------------------

func GetChambreById(w http.ResponseWriter, r *http.Request) {
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
	row := db.QueryRow("SELECT * FROM chambre WHERE numero = ?", id)

	// Récupération des données de la chambre
	var chambre model.Chambre
	err = row.Scan(&chambre.Numero, &chambre.Classe, &chambre.Etat, &chambre.TarifChambre, &chambre.Numero_niveau)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Création de la réponse
	response, err := json.Marshal(chambre)
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

func DeleteChambre(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'identifiant de la chambre depuis les paramètres de l'URL
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
	result, err := db.Exec("DELETE FROM chambre WHERE numero = ?", id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Vérification que la chambre a bien été supprimée
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "Chambre not found", http.StatusNotFound)
		return
	}

	// Envoi de la réponse
	response := model.Response_reservation{
		Status:  http.StatusOK,
		Message: "Chambre deleted successfully",
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
func UpdateChambre(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'ID de la chambre à modifier
	vars := mux.Vars(r)
	idChambre, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Lecture des données de la chambre à partir du corps de la requête
	var chambre model.Chambre
	err = json.NewDecoder(r.Body).Decode(&chambre)
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
	result, err := db.Exec("UPDATE chambre SET classe = ?, etat = ?, tarifChambre = ?, niveau_numeroNiveau = ? WHERE numero = ?", &chambre.Classe, &chambre.Etat, &chambre.TarifChambre, &chambre.Numero_niveau, idChambre)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Vérification que la chambre a bien été modifiée
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "La chambre n'a pas été trouvée", http.StatusNotFound)
		return
	}

	// Création de la réponse
	response := model.Response_reservation{
		Status:  http.StatusOK,
		Message: "Chambre updated successfully",
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
