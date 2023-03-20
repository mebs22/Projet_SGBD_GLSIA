package controller

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strconv"

	"github.com/gorilla/mux"

	config "first.go/Config"
	model "first.go/Model"
)

// --------------------------------------------------- GET_ALL --------------------------------------------------------
func Allreservation(w http.ResponseWriter, r *http.Request) {
	var reservation model.Reservation
	var response model.Response_reservation
	var arrReservation []model.Reservation

	db := config.Connect()
	defer db.Close()

	rows, err := db.Query("SELECT * FROM reservation")

	if err != nil {
		log.Print(err)
	}

	for rows.Next() {
		err = rows.Scan(&reservation.Id_reservation, &reservation.Prenom, &reservation.Nom, &reservation.Telephone, &reservation.Nuitee, &reservation.DateReservation, &reservation.DateEntree, &reservation.DateSortie, &reservation.Chambre_numero, &reservation.Facture_numero)
		if err != nil {
			log.Fatal(err.Error())
		} else {
			arrReservation = append(arrReservation, reservation)
		}
	}

	response.Status = 200
	response.Message = "Success"
	response.Data = arrReservation

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	json.NewEncoder(w).Encode(response)
}

// --------------------------------------------------- ADD --------------------------------------------------------

func InsertReservation(w http.ResponseWriter, r *http.Request) {
	var response model.Response_reservation

	db := config.Connect()
	defer db.Close()

	err := r.ParseMultipartForm(4096)
	if err != nil {
		panic(err)
	}
	prenom := r.FormValue("prenom")
	nom := r.FormValue("nom")
	telephone := r.FormValue("telephone")
	nuitee := r.FormValue("nuitee")
	dateReservation := r.FormValue("dateReservation")
	dateEntree := r.FormValue("dateEntree")
	dateSortie := r.FormValue("dateSortie")
	chambre_numero := r.FormValue("chambre_numero")
	facture_numero := r.FormValue("facture_numero")

	_, err = db.Exec("INSERT INTO reservation(prenom,nom,telephone,nuitee, dateReservation, dateEntree, dateSortie, chambre_numero, facture_numero) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", prenom, nom, telephone, nuitee, dateReservation, dateEntree, dateSortie, chambre_numero, facture_numero)

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

func GetReservationById(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'identifiant de la reservation dans les paramètres de l'URL
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
	row := db.QueryRow("SELECT * FROM reservation WHERE id_reservation = ?", id)

	// Récupération des données de la reservation
	var reservation model.Reservation
	err = row.Scan(&reservation.Id_reservation, &reservation.Prenom, &reservation.Nom, &reservation.Telephone, &reservation.Nuitee, &reservation.DateReservation, &reservation.DateEntree, &reservation.DateSortie, &reservation.Chambre_numero, &reservation.Facture_numero)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Création de la réponse
	response, err := json.Marshal(reservation)
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

func DeleteReservation(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'identifiant de la réservation depuis les paramètres de l'URL
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
	result, err := db.Exec("DELETE FROM reservation WHERE id_reservation = ?", id)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Vérification que la réservation a bien été supprimée
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "Reservation not found", http.StatusNotFound)
		return
	}

	// Envoi de la réponse
	response := model.Response_reservation{
		Status:  http.StatusOK,
		Message: "Reservation deleted successfully",
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
func UpdateReservation(w http.ResponseWriter, r *http.Request) {
	// Récupération de l'ID de la réservation à modifier
	vars := mux.Vars(r)
	idReservation, err := strconv.Atoi(vars["id"])
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	// Lecture des données du client à partir du corps de la requête
	var reservation model.Reservation
	err = json.NewDecoder(r.Body).Decode(&reservation)
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
	result, err := db.Exec("UPDATE reservation SET prenom = ?, nom = ?, telephone = ?, nuitee = ?, dateReservation = ?, dateEntree = ?, dateSortie = ?, chambre_numero = ?, facture_numero = ? WHERE id_reservation = ?", &reservation.Prenom, &reservation.Nom, &reservation.Telephone, &reservation.Nuitee, &reservation.DateReservation, &reservation.DateEntree, &reservation.DateSortie, &reservation.Chambre_numero, &reservation.Facture_numero, idReservation)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	// Vérification que la réservation a bien été modifiée
	rowsAffected, err := result.RowsAffected()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	if rowsAffected == 0 {
		http.Error(w, "La réservation n'a pas été trouvée", http.StatusNotFound)
		return
	}

	// Création de la réponse
	response := model.Response_reservation{
		Status:  http.StatusOK,
		Message: "Reservation updated successfully",
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
