package model

type Reservation struct {
	Id_reservation  int    `json:"id_reservation"`
	Prenom          string `json:"prenom"`
	Nom             string `json:"nom"`
	Telephone       string `json:"telephone"`
	Nuitee          int    `json:"nuitee"`
	DateReservation string `json:"dateReservation"`
	DateEntree      string `json:"dateEntree"`
	DateSortie      string `json:"dateSortie"`
	Chambre_numero  string `json:"chambre_numero"`
	Facture_numero  string `json:"facture_numero"`
}

type Response_reservation struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    []Reservation
}

type Chambre struct {
	Numero        int     `json:"numero"`
	Classe        string  `json:"classe"`
	Etat          string  `json:"etat"`
	TarifChambre  float64 `json:"tarifChambre"`
	Numero_niveau int     `json:"niveau_numeroNiveau"`
}

type Response_chambre struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    []Chambre
}

type Niveau struct {
	Numero        int `json:"numeroNiveau"`
	NombreChambre int `json:"nombreChambre"`
}

type Response_niveau struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    []Niveau
}

type Facture struct {
	Numero int `json:"numeroFacture"`
	Total  int `json:"total_a_payer"`
	Annexe int `json:"id_annexes"`
}

type Response_facture struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    []Facture
}

type Annexe struct {
	Numero       int     `json:"id_annexes"`
	Recettes     float64 `json:"recettes"`
	NombreClient int     `json:"nombreClient"`
	Mois         string  `json:"mois"`
}

type Response_annexe struct {
	Status  int    `json:"status"`
	Message string `json:"message"`
	Data    []Annexe
}
