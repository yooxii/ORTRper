DROP TABLE IF EXISTS `Schedule`;

DROP TABLE IF EXISTS `Test Items`;

DROP TABLE IF EXISTS `Cust`.` Code`;

DROP TABLE IF EXISTS `Product Type`;

CREATE TABLE
    `Schedule` (
        `Job No` BIGINT NOT NULL,
        `QRT` BOOLEAN NOT NULL,
        `Product` VARCHAR(15) NULL,
        `Customer` VARCHAR(20) NULL,
        `Part No` VARCHAR(15) NOT NULL,
        `Stage` VARCHAR(5) NOT NULL,
        `Test Item` VARCHAR(50) NOT NULL,
        `Sample Size` INT NOT NULL,
        `Test Period` INT NOT NULL,
        `Owner` VARCHAR(50) NOT NULL,
        `Start Date` DATE NOT NULL,
        `End Date` DATE NOT NULL,
        `Status` VARCHAR(10) NOT NULL,
        `Upload e-lab` BOOLEAN NULL,
        `Remark` TEXT NULL,
        PRIMARY KEY (`Job No`)
    ) CHARSET = utf8mb4;

ALTER TABLE `Schedule` ADD PRIMARY KEY (`Job No`);

CREATE TABLE
    `Test Items` (
        `No`.`` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Test Item` VARCHAR(50) NOT NULL,
        `Test Period` INT NOT NULL,
        `Owner` VARCHAR(50) NOT NULL,
        `Dispose` VARCHAR(20) NOT NULL,
        `Remark` TEXT NULL
    ) CHARSET = utf8mb4;

CREATE TABLE
    `Cust`.` Code` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Code` VARCHAR(5) NOT NULL,
        `Customer` VARCHAR(20) NOT NULL,
        `product_type` VARCHAR(15) NOT NULL,
        `full_product_type` VARCHAR(25) NOT NULL
    ) CHARSET = utf8mb4;

CREATE TABLE
    `Product Type` (
        `id` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `Code` VARCHAR(5) NOT NULL,
        `Type` VARCHAR(15) NOT NULL
    ) CHARSET = utf8mb4;

ALTER TABLE `Test Items` ADD CONSTRAINT `test items_test period_foreign` FOREIGN KEY (`Test Period`) REFERENCES `Schedule` (`Test Period`);

ALTER TABLE `Cust`.` Code` ADD CONSTRAINT `cust_ code_endcustomer_foreign` FOREIGN KEY (`Customer`) REFERENCES `Schedule` (`Customer`);

ALTER TABLE `Schedule` ADD CONSTRAINT `schedule_product_foreign` FOREIGN KEY (`Product`) REFERENCES `Product Type` (`Type`);

ALTER TABLE `Test Items` ADD CONSTRAINT `test items_owner_foreign` FOREIGN KEY (`Owner`) REFERENCES `Schedule` (`Owner`);

ALTER TABLE `Test Items` ADD CONSTRAINT `test items_test item_foreign` FOREIGN KEY (`Test Item`) REFERENCES `Schedule` (`Test Item`);