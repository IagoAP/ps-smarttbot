create database smarttbot;

use smarttbot;

CREATE TABLE candles (moeda VARCHAR(20), periodicidade TINYINT, horario DATETIME, open DOUBLE, low DOUBLE, high DOUBLE, close DOUBLE);
INSERT INTO candles VALUES ('Bitcoin', 1, NOW() , 2, 1, 4, 3);
INSERT INTO candles VALUES ('Monero', 5, NOW() , 3, 4, 1, 2);