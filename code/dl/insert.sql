/* Inserting meals */

INSERT INTO "Jidlo" ("Cena", "Nazev") VALUES (125, 'Čevabčiči s vařeným bramborem, cibulkou a hořčicí');
INSERT INTO "Jidlo" ("Cena", "Nazev") VALUES (125, 'Špagety Aglio-Olio se sušeným tomatem a rukolou');
INSERT INTO "Jidlo" ("Cena","Nazev") VALUES (135, 'Kuřecí stripsy s bramborovou kaší');
INSERT INTO "Jidlo" ("Cena","Nazev") VALUES(145, 'Trhaný salát s červenou čočkou a vepřovou panenkou');
INSERT INTO "Jidlo" ("Cena", "Nazev") VALUES (145,'Brokolicové muffiny s grilovaným lososem');


/* Inserting tables */

INSERT INTO "Stul" ("Pocetmist") VALUES(2);
INSERT INTO "Stul" ("Pocetmist") VALUES(2);
INSERT INTO "Stul" ("Pocetmist") VALUES(4);
INSERT INTO "Stul" ("Pocetmist") VALUES(4);
INSERT INTO "Stul" ("Pocetmist") VALUES(6);
INSERT INTO "Stul" ("Pocetmist") VALUES(6);
INSERT INTO "Stul" ("Pocetmist") VALUES(8);
INSERT INTO "Stul" ("Pocetmist") VALUES(10);
INSERT INTO "Stul" ("Pocetmist") VALUES(2);
INSERT INTO "Stul" ("Pocetmist") VALUES(3);

/* Inserting table schedules */

INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2000-01-01 00:00:00.001', '3000-01-01 00:00:00.001', '1', 3);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-21 00:00:00.001', '2021-04-22 00:00:00.001', '1', 1);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-21 00:00:00.001', '2021-04-22 00:00:00.001', '0', 2);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-21 19:00:00.001', '2021-04-21 21:00:00.001', '1', 4);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-01 15:30:00.001', '2021-04-10 16:00:00.001', '1', 5);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-20 00:00:00.001', '2021-04-24 00:00:00.001', '1', 6);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-22 00:00:00.001', '2021-04-01 23:00:00.001', '0', 1);
INSERT INTO "Rozvrh" ("Datumdo", "Datumod", "Jedostupny", "StulID") VALUES ('2021-04-22 00:00:00.001', '2021-04-22 12:00:00.001', '1', 2);

/* Inserting alergens */

INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (1, 'Lepek');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (2, 'Korýši');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (3, 'Vejce');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (4, 'Ryby');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (5, 'Arašídy');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (6, 'Sója');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (7, 'Mléko');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (8, 'Skořápkové plody');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (9, 'Celer');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (10, 'Hořčice');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (11, 'Sezam');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (12, 'Oxid siřičitý a siřičitany');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (13, 'Vlčí bob');
INSERT INTO "Alergen" ("Cislo", "Nazev") VALUES (14, 'Měkkýši');
