-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `metal_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `metal_db`;

DROP TABLE IF EXISTS `Albums`;
CREATE TABLE `Albums` (
  `albumID` int NOT NULL AUTO_INCREMENT,
  `album_name` varchar(100) DEFAULT NULL,
  `artist_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  UNIQUE KEY `albumID` (`albumID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Albums` (`albumID`, `album_name`, `artist_name`) VALUES
(1,	'Black Sabbath',	'Black Sabbath'),
(2,	'Crystal Logic',	'Manilla Road'),
(3,	'Overkill',	'Motorhead');

DROP TABLE IF EXISTS `Names`;
CREATE TABLE `Names` (
  `nameID` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `fav_songID` int NOT NULL,
  PRIMARY KEY (`nameID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Names` (`nameID`, `first_name`, `fav_songID`) VALUES
(1,	'Gary',	1),
(2,	'Khalid',	7),
(3,	'Bob',	3),
(4,	'Larry',	6),
(7,	'Tom',	0);

DROP TABLE IF EXISTS `Songs`;
CREATE TABLE `Songs` (
  `songID` int NOT NULL AUTO_INCREMENT,
  `song_title` varchar(100) NOT NULL,
  `albumID` int NOT NULL,
  `artist_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`songID`),
  KEY `albumID` (`albumID`),
  CONSTRAINT `Songs_ibfk_1` FOREIGN KEY (`albumID`) REFERENCES `Albums` (`albumID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Songs` (`songID`, `song_title`, `albumID`, `artist_name`) VALUES
(1,	'Black Sabbath ',	1,	'Black Sabbath '),
(2,	'The Wizard ',	1,	'Black Sabbath'),
(3,	'Behind the Wall of Sleep ',	1,	'Black Sabbath'),
(4,	'N.I.B. ',	1,	'Black Sabbath'),
(5,	'Evil Woman',	1,	'Black Sabbath'),
(6,	'Sleeping Village ',	1,	'Black Sabbath'),
(7,	'Warning ',	1,	'Black Sabbath'),
(8,	'Necropolis',	2,	'Manilla Road'),
(9,	'Crystal Logic',	2,	'Manilla Road'),
(10,	'Feeling Free Again',	2,	'Manilla Road'),
(11,	'The Riddle Master ',	2,	'Manilla Road'),
(12,	'The Ram',	2,	'Manilla Road'),
(13,	'The Veils of Negative Existence',	2,	'Manilla Road'),
(14,	'Dreams of Eschaton',	2,	'Manilla Road'),
(15,	'Overkill',	3,	'Motorhead'),
(16,	'Stay Clean',	3,	'Motorhead'),
(17,	'(I Won\'t) Pay Your Price',	3,	'Motorhead'),
(18,	'I\'ll Be Your Sister',	3,	'Motorhead'),
(19,	'Capricorn',	3,	'Motorhead'),
(20,	'No Class',	3,	'Motorhead'),
(21,	'Damage Case',	3,	'Motorhead'),
(22,	'Tear Ya Down',	3,	'Motorhead'),
(23,	'Metropolis',	3,	'Motorhead'),
(24,	'Limb From Limb',	3,	'Motorhead');

-- 2020-10-08 11:06:20

