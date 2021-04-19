/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 14.1 		*/
/*  Created On : 19-dub-2021 17:07:17 				*/
/*  DBMS       : PostgreSQL 						*/
/* ---------------------------------------------------- */

/* Drop Sequences for Autonumber Columns */

DROP SEQUENCE IF EXISTS adresa_adresaid_seq
;

DROP SEQUENCE IF EXISTS alergen_alergenid_seq
;

DROP SEQUENCE IF EXISTS jidlo_jidloid_seq
;

DROP SEQUENCE IF EXISTS menu_menuid_seq
;

DROP SEQUENCE IF EXISTS objednavka_jidla_objednavka_jidlaid_seq
;

DROP SEQUENCE IF EXISTS rezervace_objednavka_jidlaid_seq
;

DROP SEQUENCE IF EXISTS rozvrh_rozvrhid_seq
;

DROP SEQUENCE IF EXISTS stul_stulid_seq
;

DROP SEQUENCE IF EXISTS uzivatel_uzivatelid_seq
;

/* Drop Tables */

DROP TABLE IF EXISTS "Adresa" CASCADE
;

DROP TABLE IF EXISTS "Alergen" CASCADE
;

DROP TABLE IF EXISTS "Je_soucasti" CASCADE
;

DROP TABLE IF EXISTS "Je_zarezervovan" CASCADE
;

DROP TABLE IF EXISTS "Jidlo" CASCADE
;

DROP TABLE IF EXISTS "Menu" CASCADE
;

DROP TABLE IF EXISTS "Objednavka_jidla" CASCADE
;

DROP TABLE IF EXISTS "Obsahuje" CASCADE
;

DROP TABLE IF EXISTS "Prebyva_na_adrese" CASCADE
;

DROP TABLE IF EXISTS "Rezervace" CASCADE
;

DROP TABLE IF EXISTS "Rozvrh" CASCADE
;

DROP TABLE IF EXISTS "Stul" CASCADE
;

DROP TABLE IF EXISTS "Uzivatel" CASCADE
;

/* Create Tables */

CREATE TABLE "Adresa"
(
	"Mesto" varchar(50) NULL,
	"Psc" integer NULL,
	"Stat" varchar(50) NULL,
	"Ulice" varchar(50) NULL,
	"AdresaID" integer NOT NULL   DEFAULT NEXTVAL(('"adresa_adresaid_seq"'::text)::regclass)
)
;

CREATE TABLE "Alergen"
(
	"Cislo" integer NULL,
	"Nazev" varchar(50) NULL,
	"AlergenID" integer NOT NULL   DEFAULT NEXTVAL(('"alergen_alergenid_seq"'::text)::regclass)
)
;

CREATE TABLE "Je_soucasti"
(
	"JidloID" integer NULL,
	"AlergenID" integer NULL
)
;

CREATE TABLE "Je_zarezervovan"
(
	"RezervaceID" integer NULL,
	"StulID" integer NULL
)
;

CREATE TABLE "Jidlo"
(
	"Cena" integer NULL,
	"Nazev" varchar(50) NULL,
	"JidloID" integer NOT NULL   DEFAULT NEXTVAL(('"jidlo_jidloid_seq"'::text)::regclass)
)
;

CREATE TABLE "Menu"
(
	"Platnostdo" date NULL,
	"Platnostod" date NULL,
	"MenuID" integer NOT NULL   DEFAULT NEXTVAL(('"menu_menuid_seq"'::text)::regclass)
)
;

CREATE TABLE "Objednavka_jidla"
(
	"Pocet" integer NULL,
	"Objednavka_jidlaID" integer NOT NULL   DEFAULT NEXTVAL(('"objednavka_jidla_objednavka_jidlaid_seq"'::text)::regclass),
	"JidloID" integer NULL
)
;

CREATE TABLE "Obsahuje"
(
	"MenuID" integer NULL,
	"JidloID" integer NULL
)
;

CREATE TABLE "Prebyva_na_adrese"
(
	"AdresaID" integer NULL,
	"UzivatelID" integer NULL
)
;

CREATE TABLE "Rezervace"
(
	"Datumdo" date NULL,
	"Datumod" date NULL,
	"RezervaceID" integer NOT NULL,
	"Objednavka_jidlaID" integer NULL   DEFAULT NEXTVAL(('"rezervace_objednavka_jidlaid_seq"'::text)::regclass),
	"UzivatelID" integer NULL
)
;

CREATE TABLE "Rozvrh"
(
	"Datumdo" date NULL,
	"Datumod" date NULL,
	"Jedostupny" boolean NULL,
	"RozvrhID" integer NOT NULL   DEFAULT NEXTVAL(('"rozvrh_rozvrhid_seq"'::text)::regclass),
	"StulID" integer NULL
)
;

CREATE TABLE "Stul"
(
	"Pocetmist" integer NULL,
	"StulID" integer NOT NULL   DEFAULT NEXTVAL(('"stul_stulid_seq"'::text)::regclass)
)
;

CREATE TABLE "Uzivatel"
(
	"Email" varchar(50) NULL,
	"Jmeno" varchar(50) NULL,
	"Prijmeni" varchar(50) NULL,
	"Telefon" varchar(50) NULL,
	"UzivatelID" integer NOT NULL   DEFAULT NEXTVAL(('"uzivatel_uzivatelid_seq"'::text)::regclass)
)
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE "Adresa" ADD CONSTRAINT "PK_Adresa"
	PRIMARY KEY ("AdresaID")
;

ALTER TABLE "Alergen" ADD CONSTRAINT "PK_Alergen"
	PRIMARY KEY ("AlergenID")
;

ALTER TABLE "Jidlo" ADD CONSTRAINT "PK_Jidlo"
	PRIMARY KEY ("JidloID")
;

ALTER TABLE "Menu" ADD CONSTRAINT "PK_Menu"
	PRIMARY KEY ("MenuID")
;

ALTER TABLE "Objednavka_jidla" ADD CONSTRAINT "PK_Objednavka_jidla"
	PRIMARY KEY ("Objednavka_jidlaID")
;

ALTER TABLE "Rezervace" ADD CONSTRAINT "PK_Rezervace"
	PRIMARY KEY ("RezervaceID")
;

ALTER TABLE "Rozvrh" ADD CONSTRAINT "PK_Rozvrh"
	PRIMARY KEY ("RozvrhID")
;

ALTER TABLE "Stul" ADD CONSTRAINT "PK_Stul"
	PRIMARY KEY ("StulID")
;

ALTER TABLE "Uzivatel" ADD CONSTRAINT "PK_Uzivatel"
	PRIMARY KEY ("UzivatelID")
;

/* Create Foreign Key Constraints */

ALTER TABLE "Je_soucasti" ADD CONSTRAINT "FK_Je_soucasti_Jidlo"
	FOREIGN KEY ("JidloID") REFERENCES "Jidlo" ("JidloID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Je_soucasti" ADD CONSTRAINT "FK_Je_soucasti_Alergen"
	FOREIGN KEY ("AlergenID") REFERENCES "Alergen" ("AlergenID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Je_zarezervovan" ADD CONSTRAINT "FK_Je_zarezervovan_Rezervace"
	FOREIGN KEY ("RezervaceID") REFERENCES "Rezervace" ("RezervaceID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Je_zarezervovan" ADD CONSTRAINT "FK_Je_zarezervovan_Stul"
	FOREIGN KEY ("StulID") REFERENCES "Stul" ("StulID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Objednavka_jidla" ADD CONSTRAINT "FK_Objednavka_jidla_Je_soucasti"
	FOREIGN KEY ("JidloID") REFERENCES "Jidlo" ("JidloID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Obsahuje" ADD CONSTRAINT "FK_Obsahuje_Menu"
	FOREIGN KEY ("MenuID") REFERENCES "Menu" ("MenuID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Obsahuje" ADD CONSTRAINT "FK_Obsahuje_Jidlo"
	FOREIGN KEY ("JidloID") REFERENCES "Jidlo" ("JidloID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Prebyva_na_adrese" ADD CONSTRAINT "FK_Prebyva_na_adrese_Adresa"
	FOREIGN KEY ("AdresaID") REFERENCES "Adresa" ("AdresaID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Prebyva_na_adrese" ADD CONSTRAINT "FK_Prebyva_na_adrese_Uzivatel"
	FOREIGN KEY ("UzivatelID") REFERENCES "Uzivatel" ("UzivatelID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Rezervace" ADD CONSTRAINT "FK_Rezervace_Patri_k"
	FOREIGN KEY ("Objednavka_jidlaID") REFERENCES "Objednavka_jidla" ("Objednavka_jidlaID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Rezervace" ADD CONSTRAINT "FK_Rezervace_si zarezervoval"
	FOREIGN KEY ("UzivatelID") REFERENCES "Uzivatel" ("UzivatelID") ON DELETE No Action ON UPDATE No Action
;

ALTER TABLE "Rozvrh" ADD CONSTRAINT "FK_Rozvrh_Dostupnost_se_ridi_podle"
	FOREIGN KEY ("StulID") REFERENCES "Stul" ("StulID") ON DELETE No Action ON UPDATE No Action
;

/* Create Table Comments, Sequences for Autonumber Columns */

COMMENT ON TABLE "Adresa"
	IS 'Informace o bydlistich jednotlvych uzivatelu'
;

CREATE SEQUENCE adresa_adresaid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Alergen"
	IS 'Kazdy alergen ma svuj identifikator - cislo a nazev'
;

CREATE SEQUENCE alergen_alergenid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Jidlo"
	IS 'Samotne jidlo, atributy cena a jeho nazev'
;

CREATE SEQUENCE jidlo_jidloid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Menu"
	IS 'Urcuje dostupne menu v danem casovem rozmezi'
;

CREATE SEQUENCE menu_menuid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Objednavka_jidla"
	IS 'Vaze se ke konkretnimu jidlu a urcuje jeho pocet v objednavce'
;

CREATE SEQUENCE objednavka_jidla_objednavka_jidlaid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Rezervace"
	IS 'Obsahuje casove udaje kazde rezervaci'
;

CREATE SEQUENCE rezervace_objednavka_jidlaid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Rozvrh"
	IS 'Urcuje dostupnost stolu v danem casovem okne'
;

CREATE SEQUENCE rozvrh_rozvrhid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Stul"
	IS 'Kazdy stul si udrzuje pocet mist k sezeni'
;

CREATE SEQUENCE stul_stulid_seq INCREMENT 1 START 1
;

COMMENT ON TABLE "Uzivatel"
	IS 'Obsahuje kontaktni udaje o existujicich uzivatelich.'
;

CREATE SEQUENCE uzivatel_uzivatelid_seq INCREMENT 1 START 1
;
