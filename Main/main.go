package main

import (
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"

	controller "first.go/Controller"
)

func main() {
	router := mux.NewRouter()
	router.HandleFunc("/reservation/", controller.Allreservation).Methods("GET")
	router.HandleFunc("/reservation/{id}", controller.GetReservationById).Methods("GET")
	router.HandleFunc("/reservation/insert/", controller.InsertReservation).Methods("POST")
	router.HandleFunc("/reservation/delete/{id}", controller.DeleteReservation).Methods("DELETE")
	router.HandleFunc("/reservation/update/{id}", controller.UpdateReservation).Methods("PUT")

	router.HandleFunc("/chambre/", controller.AllChambre).Methods("GET")
	router.HandleFunc("/chambre/{id}", controller.GetChambreById).Methods("GET")
	router.HandleFunc("/chambre/insert/", controller.InsertChambre).Methods("POST")
	router.HandleFunc("/chambre/delete/{id}", controller.DeleteChambre).Methods("DELETE")
	router.HandleFunc("/chambre/update/{id}", controller.UpdateChambre).Methods("PUT")

	router.HandleFunc("/niveau/", controller.AllNiveau).Methods("GET")
	router.HandleFunc("/niveau/{id}", controller.GetNiveauById).Methods("GET")
	router.HandleFunc("/niveau/insert/", controller.InsertNiveau).Methods("POST")
	router.HandleFunc("/niveau/delete/{id}", controller.DeleteNiveau).Methods("DELETE")
	router.HandleFunc("/niveau/update/{id}", controller.UpdateNiveau).Methods("PUT")

	router.HandleFunc("/facture/", controller.AllFacture).Methods("GET")
	router.HandleFunc("/facture/{id}", controller.GetFactureById).Methods("GET")
	router.HandleFunc("/facture/insert/", controller.InsertFacture).Methods("POST")
	router.HandleFunc("/facture/delete/{id}", controller.DeleteFacture).Methods("DELETE")
	router.HandleFunc("/facture/update/{id}", controller.UpdateFacture).Methods("PUT")

	router.HandleFunc("/annexe/", controller.AllAnnexe).Methods("GET")
	router.HandleFunc("/annexe/{id}", controller.GetAnnexeById).Methods("GET")
	router.HandleFunc("/annexe/insert/", controller.InsertAnnexe).Methods("POST")
	router.HandleFunc("/annexe/delete/{id}", controller.DeleteAnnexe).Methods("DELETE")
	router.HandleFunc("/annexe/update/{id}", controller.UpdateAnnexe).Methods("PUT")

	http.Handle("/", router)
	fmt.Println("Connected to port 8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
