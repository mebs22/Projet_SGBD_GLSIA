
-- MySQL Script generated by MySQL Workbench
-- Fri Mar 17 21:23:01 2023
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `hotel` ;

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel` DEFAULT CHARACTER SET utf8 ;
USE `hotel` ;

-- -----------------------------------------------------
-- Table `hotel`.`annexes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`annexes` ;

CREATE TABLE IF NOT EXISTS `hotel`.`annexes` (
  `id_annexes` INT NOT NULL AUTO_INCREMENT,
  `recettes` FLOAT NULL,
  `nombreClient` INT NULL,
  `mois` VARCHAR(45) NULL,
  PRIMARY KEY (`id_annexes`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`chambre`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`chambre` ;

CREATE TABLE IF NOT EXISTS `hotel`.`chambre` (
  `numero` INT NOT NULL AUTO_INCREMENT,
  `classe` VARCHAR(45) NULL,
  `etat` VARCHAR(45) NULL,
  `tarifChambre` FLOAT NOT NULL,
  `niveau_numeroNiveau` INT NOT NULL,
  PRIMARY KEY (`numero`),
  INDEX `fk_chambre_niveau1_idx` (`niveau_numeroNiveau` ASC) VISIBLE,
  CONSTRAINT `fk_chambre_niveau1`
    FOREIGN KEY (`niveau_numeroNiveau`)
    REFERENCES `hotel`.`niveau` (`numeroNiveau`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`facture`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`facture` ;

CREATE TABLE IF NOT EXISTS `hotel`.`facture` (
  `numeroFacture` INT NOT NULL AUTO_INCREMENT,
  `total_a_payer` FLOAT NOT NULL,
  `id_annexes` INT NOT NULL,
  PRIMARY KEY (`numeroFacture`),
  INDEX `fk_facture_annexes1_idx` (`id_annexes` ASC) VISIBLE,
  CONSTRAINT `fk_facture_annexes1`
    FOREIGN KEY (`id_annexes`)
    REFERENCES `hotel`.`annexes` (`id_annexes`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`niveau`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`niveau` ;

CREATE TABLE IF NOT EXISTS `hotel`.`niveau` (
  `numeroNiveau` INT NOT NULL AUTO_INCREMENT,
  `nombreChambre` INT NULL,
  PRIMARY KEY (`numeroNiveau`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`reservation`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `hotel`.`reservation` ;

CREATE TABLE IF NOT EXISTS `hotel`.`reservation` (
  `id_reservation` INT NOT NULL AUTO_INCREMENT,
  `prenom` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `telephone` VARCHAR(45) NULL,
  `nuitee` INT NULL,
  `dateReservation` DATE NULL,
  `dateEntree` DATE NULL,
  `dateSortie` DATE NULL,
  `chambre_numero` INT NOT NULL,
  `facture_numero` INT NOT NULL,
  PRIMARY KEY (`id_reservation`),
  INDEX `fk_reservation_chambre_idx` (`chambre_numero` ASC) VISIBLE,
  INDEX `fk_reservation_facture1_idx` (`facture_numero` ASC) VISIBLE,
  CONSTRAINT `fk_reservation_chambre`
    FOREIGN KEY (`chambre_numero`)
    REFERENCES `hotel`.`chambre` (`numero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reservation_facture1`
    FOREIGN KEY (`facture_numero`)
    REFERENCES `hotel`.`facture` (`numeroFacture`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- Insertions ---------------------------------------------------------
insert into annexes (recettes,nombreClient,mois)
values (10000,2,"Janvier");

insert into facture (total_a_payer,id_annexes)
values (5000,1),(5000,1);

insert into niveau (nombreChambre)
values (5);

insert into chambre (classe,etat,tarifChambre,niveau_numeroNiveau)
values ("economic","bon",5000,1),("first_class","bon",5000,1);;

insert into reservation (prenom,nom,telephone,nuitee,dateReservation,dateEntree,dateSortie,chambre_numero,facture_numero)
values ("Ndeya","Diouf","+221773710489",2,"2023-03-17","2023-03-17","2023-03-19",1,1),("Beyonce","Kardashian","+221781147727",2,"2023-03-17","2023-03-17","2023-03-19",2,2);