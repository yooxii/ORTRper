DROP TABLE IF EXISTS `Schedule`;

DROP TABLE IF EXISTS `TestItems`;

DROP TABLE IF EXISTS `CustCode`;

DROP TABLE IF EXISTS `ProductType`;

DROP TABLE IF EXISTS `Claims`;

CREATE TABLE
    `Schedule` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `JobNo` INTEGER NOT NULL,
        `QRT` BOOLEAN NOT NULL,
        `Product` VARCHAR(15) NULL,
        `Customer` VARCHAR(20) NULL,
        `PartNo` VARCHAR(15) NOT NULL,
        `Stage` VARCHAR(5) NOT NULL,
        `TestItem` VARCHAR(50) NOT NULL,
        `SampleSize` INTEGER NOT NULL,
        `TestPeriod` INTEGER NOT NULL,
        `Owner` VARCHAR(50) NOT NULL,
        `StartDate` DATE NOT NULL,
        `EndDate` DATE NOT NULL,
        `Status` VARCHAR(10) NOT NULL,
        `Upload_e-lab` BOOLEAN NULL,
        `Remark` TEXT NULL,
        FOREIGN KEY (`Product`) REFERENCES `ProductType` (`Type`),
        FOREIGN KEY (`PartNo`) REFERENCES `Claims` (`PartNo`)
    );

CREATE TABLE
    `TestItems` (
        `No` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `TestItem` VARCHAR(50) NOT NULL,
        `TestPeriod` INTEGER NOT NULL,
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
        `product_type` VARCHAR(15) NOT NULL,
        `full_product_type` VARCHAR(25) NOT NULL,
        FOREIGN KEY (`Customer`) REFERENCES `Schedule` (`Customer`)
    );

CREATE TABLE
    `ProductType` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `Code` VARCHAR(5) NOT NULL,
        `Type` VARCHAR(15) NOT NULL
    );

CREATE TABLE
    `Claims` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `claim_date` DATE NOT NULL,
        `claim_no` VARCHAR(20) UNIQUE  NOT NULL,
        `PartNo` VARCHAR(15) NOT NULL,
        `claim_qty` DECIMAL(10, 2) NOT NULL,
        `TestItem` VARCHAR(50) NULL,
        `SN` TEXT NOT NULL,
        `DC` VARCHAR(8) NOT NULL,
        `REV` VARCHAR(10) NOT NULL,
        `Work_Order` VARCHAR(40) NOT NULL,
        `claim_status` VARCHAR(20) NULL,
        `Remarks` TEXT NULL
    );