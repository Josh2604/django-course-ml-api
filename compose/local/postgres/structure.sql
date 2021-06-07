-- CREATE DATABASE admin if not exists;
CREATE TABLE Users (id int, name character varying(30) not null, apells character varying(50) not null, age INT NOT NULL, CONSTRAINT "p_pk" PRIMARY KEY (id));
INSERT INTO Users VALUES(1, 'Juan', 'Alberto Quintero', 24),
(2, 'Juan', 'Antonio', 20),
(3, 'Jose', 'Damian', 30),
(4, 'Oscar', 'Hernandez', 31),
(5, 'Gillermo', 'De la luz', 26),
(6, 'Santiago', 'Gerrero', 27),
(7, 'Armando', 'Damian', 22),
(8, 'Pedro', 'Damian', 29),
(9, 'Berenice', 'Matiaz', 27);
