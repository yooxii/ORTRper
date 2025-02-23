DROP TABLE IF EXISTS `TSchedule`;

DROP TABLE IF EXISTS `TCheckouts`;

CREATE TABLE
    `TSchedule` (
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
        FOREIGN KEY (`PartNo`) REFERENCES `Checkouts` (`PartNo`)
    );

CREATE TABLE
    `TCheckouts` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `checkout_date` DATE NOT NULL,
        `checkout_no` VARCHAR(20) NOT NULL,
        `PartNo` VARCHAR(15) NOT NULL,
        `TestItem` VARCHAR(50) NULL,
        `checkout_qty` DECIMAL(10, 2) NOT NULL,
        `SN` TEXT NOT NULL,
        `DC` VARCHAR(8) NOT NULL,
        `REV` VARCHAR(10) NOT NULL,
        `Work_Order` VARCHAR(40) NOT NULL,
        `Remarks` TEXT NULL,
        `checkout_status` VARCHAR(20) NULL
    );