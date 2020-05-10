-- Adminer 4.7.6 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `becky`;
CREATE DATABASE `becky` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `becky`;

DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `alembic_version` (`version_num`) VALUES
('2218c5c46b85');

DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
  `bookID` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `price` double NOT NULL,
  `reorderthres` int NOT NULL,
  `stoporder` tinyint(1) NOT NULL,
  `stock` int NOT NULL,
  PRIMARY KEY (`bookID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

INSERT INTO `book` (`bookID`, `title`, `author`, `price`, `reorderthres`, `stoporder`, `stock`) VALUES
(1,	'A World Of Prose',	'Author Authorson',	45,	3,	0,	30),
(2,	'Secret Agent Handbook',	'Mark Haddon',	300,	4,	0,	30),
(3,	'World Book',	'Mark Manson',	32,	3,	0,	323),
(4,	'Clifford the Big Red Dog',	'Clifford Authors',	70,	12,	0,	30),
(5,	'Test Book',	'Tst Author',	20,	2,	0,	480);

DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `cID` int NOT NULL AUTO_INCREMENT,
  `custID` int DEFAULT NULL,
  `bookID` int DEFAULT NULL,
  PRIMARY KEY (`cID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `cart` (`cID`, `custID`, `bookID`) VALUES
(15,	1,	1),
(17,	1,	3);

DROP TABLE IF EXISTS `items`;
CREATE TABLE `items` (
  `itID` int NOT NULL,
  `ordID` int NOT NULL,
  `bookID` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `author` varchar(255) NOT NULL,
  `price` double NOT NULL,
  PRIMARY KEY (`itID`),
  KEY `ix_items_ordID` (`ordID`),
  CONSTRAINT `items_ibfk_1` FOREIGN KEY (`ordID`) REFERENCES `order` (`ordID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `ordID` int NOT NULL AUTO_INCREMENT,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `cust` varchar(255) NOT NULL,
  PRIMARY KEY (`ordID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS `promotions`;
CREATE TABLE `promotions` (
  `pID` int NOT NULL AUTO_INCREMENT,
  `percoff` float NOT NULL,
  PRIMARY KEY (`pID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) DEFAULT NULL,
  `pwd_hash` varchar(200) DEFAULT NULL,
  `urole` varchar(80) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `member` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `user_chk_1` CHECK ((`member` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- Manager Login admin / admin , user login smithcleon/ smithcleon

INSERT INTO `user` (`id`, `username`, `pwd_hash`, `urole`, `name`, `email`, `address`, `member`) VALUES
(1,	'smithcleon',	'pbkdf2:sha256:150000$m2qqAqeU$3a8cffa714869f2a7cefe56a3f8d35166cef5fd1b5289f50bc3fc02f5f3524f3',	'cust',	'Cleon Mullings',	'smithcleon@gmail.com',	'sun city',	1),
(2,	'admin',	'pbkdf2:sha256:150000$G1oa5LGH$c26345d1f71d3da9dccf400cb86e29879e146300955c385dfe7c373b3a4cad10',	'manager',	'Admin',	'Admin',	'Admin',	1);

-- 2020-05-10 01:02:05