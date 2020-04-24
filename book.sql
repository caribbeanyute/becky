DROP DATABASE IF EXISTS becky;
CREATE DATABASE becky;
USE becky;



CREATE TABLE `book`
(
    `bookID`      INT    not null auto_increment,
    `title`  varchar(255)  NOT NULL,
    `author`   varchar(255)  NOT NULL,
    `price` varchar(255)  NOT NULL,
    `reorderthres`     varchar(255)  NOT NULL,
    `stoporder`        DATE          NOT NULL,
    `stock`      varchar(1000) NOT NULL UNIQUE,

    PRIMARY KEY (`bookID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `customer`
(
    `custID`      INT    not null auto_increment,
    `username`  varchar(255)  NOT NULL,
    `passwordHash`   varchar(255)  NOT NULL,
    `name` varchar(255)  NOT NULL,
    `email`     varchar(255)  NOT NULL,
    `address`     varchar(255)          NOT NULL,
    `member`      BOOLEAN NOT NULL ,
    PRIMARY KEY (`custID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE `manager`
(
    `manID`      INT    not null auto_increment,
    `username`  varchar(255)  NOT NULL,
    `passwordHash`   varchar(255)  NOT NULL,
    `name` varchar(255)  NOT NULL,
    `email`     varchar(255)  NOT NULL,
    PRIMARY KEY (`manID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

# Need to do tables for order

