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

func AllNiveau(w http.ResponseWriter, r *http.Request) {
	var niveau model.Niveau
	var response model.Response_niveau
	var arrNiveau []model.Niveau

	db := config.Connect()
	defer db.Close()

	rows, err := db.Query("SELECT * FROM niveau")

	if err != nil {
		log.Print(err)
	}

	for rows.Next() {
		err = rows.Scan(&niveau.Numero, &niveau.NombreChambre)
		if err != nil {
			log.Fatal(err.Error())
		} else {
			arrNiveau = append(arrNiveau, niveau)
		}
	}

	response.Status = 200
	response.Message = "Success"
	response.Data = arrNiveau

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

// ---------------------------------------------------------------INSERT-----------------------------------------------------------------
func InsertNiveau(w http.ResponseWriter, r *http.Request) {
	var response model.Response_niveau

	db := config.Connect()
	defer db.Close()

	err := r.ParseMultipartForm(4096)
	if err != nil {
		panic(err)
	}
	nombreChambre := r.FormValue("nombreChambre")

	_, err = db.Exec("INSERT INTO niveau(nombreChambre) VALUES(?)", nombreChambre)

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

func GetNiveauById(w http.ResponseWriter, r *http.Request) {
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
	row := db.QueryRow("SELECT * FROM niveau WHERE numeroNiveau = ?", id)

	// Récupération des données de la chambre
	var niveau model.Niveau
	err = row.Scan(&niveau.Numero, &niveau.NombreChambre)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Création de la réponse
	response, err := json.Marshal(niveau)
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

func DeleteNiveau(w http.ResponseWriter, r *http.Request) {
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
	result, err := db.Exec("DELETE FROM niveau WHERE numeroNiveau = ?", id)
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
		http.Error(w, "niveau not found", http.StatusNotFound)
		return
	}

	// Envoi de la réponse
	response := model.Response_niveau{
		Status:  http.StatusOK,
		Message: "Niveau deleted successfully",
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
func UpdateNiveau(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	idNiveau, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Lecture des données de la chambre à partir du corps de la requête
	var niveau model.Niveau
	err = json.NewDecoder(r.Body).Decode(&niveau)
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
	result, err := db.Exec("UPDATE niveau SET nombreChambre = ? WHERE numeroNiveau = ?", &niveau.NombreChambre, idNiveau)
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
		http.Error(w, "Le niveau n'a pas été trouvée", http.StatusNotFound)
		return
	}

	// Création de la réponse
	response := model.Response_niveau{
		Status:  http.StatusOK,
		Message: "Niveau updated successfully",
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
