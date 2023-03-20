package config

import (
	"database/sql"
)

func Connect() *sql.DB {
	db, err := sql.Open("mysql", "apache:@tcp(127.0.0.1:3308)/hotel")
	if err != nil {
		panic(err.Error())
	}
	return db
}
