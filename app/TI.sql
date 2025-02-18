DROP TABLE IF EXISTS `TestItems`;

DROP TABLE IF EXISTS `CustCode`;

DROP TABLE IF EXISTS `ProductType`;

DROP TABLE IF EXISTS `CheckoutTIs`;

CREATE TABLE
    `TestItems` (
        `No` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `TestItem` VARCHAR(50) NOT NULL,
        `TestPeriod` FLOAT NOT NULL,
        `Owner` VARCHAR(50) NOT NULL,
        `Dispose` VARCHAR(20) NOT NULL,
        `Remark` TEXT NULL,
        FOREIGN KEY (`TestPeriod`) REFERENCES `Schedule` (`TestPeriod`),
        FOREIGN KEY (`Owner`) REFERENCES `Schedule` (`Owner`),
        FOREIGN KEY (`TestItem`) REFERENCES `Schedule` (`TestItem`)
    );

CREATE TABLE
    `CustCode` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `Code` VARCHAR(5) NOT NULL,
        `Customer` VARCHAR(20) NOT NULL,
        `product_type` VARCHAR(15) NULL,
        `full_product_type` VARCHAR(25) NULL,
        FOREIGN KEY (`Customer`) REFERENCES `Schedule` (`Customer`)
    );

CREATE TABLE
    `ProductType` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `Code` VARCHAR(5) NOT NULL,
        `Type` VARCHAR(15) NOT NULL
    );

CREATE TABLE
    `CheckoutTIs` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `TI` VARCHAR(10) NOT NULL
    );