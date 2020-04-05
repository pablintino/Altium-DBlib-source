DROP TABLE IF EXISTS t_DiodesTVS;


create table t_DiodesTVS
(
    `componentlink2description` VARCHAR(100) DEFAULT NULL,
    `componentlink2url`         VARCHAR(250) DEFAULT NULL,
    `componentlink3description` VARCHAR(100) DEFAULT NULL,
    `componentlink3url`         VARCHAR(250) DEFAULT NULL,
    `componentlink4description` VARCHAR(100) DEFAULT NULL,
    `componentlink4url`         VARCHAR(250) DEFAULT NULL,
    `componentlink5description` VARCHAR(100) DEFAULT NULL,
    `componentlink5url`         VARCHAR(250) DEFAULT NULL,
    `componentlink6description` VARCHAR(100) DEFAULT NULL,
    `componentlink6url`         VARCHAR(250) DEFAULT NULL,
    `footprintpath2`            VARCHAR(100) DEFAULT NULL,
    `footprintref2`             VARCHAR(100) DEFAULT NULL,
    `footprintpath3`            VARCHAR(100) DEFAULT NULL,
    `componentlink1url`         VARCHAR(250) DEFAULT NULL,
    `footprintref3`             VARCHAR(100) DEFAULT NULL,
    `Type`                      VARCHAR(127) DEFAULT NULL,
    `UnidirectionalChannels`    VARCHAR(127) DEFAULT NULL,
    `BidirectionalChannels`     VARCHAR(127) DEFAULT NULL,
    `VoltageReverseStandoffTyp` VARCHAR(127) DEFAULT NULL,
    `VoltageBreakdownMin`       VARCHAR(127) DEFAULT NULL,
    `VoltageClampingMaxIpp`     VARCHAR(127) DEFAULT NULL,
    `CurrentPeakPulse101000µs`  VARCHAR(127) DEFAULT NULL,
    `PowerPeakPulse`            VARCHAR(127) DEFAULT NULL,
    `PowerLineProtection`       VARCHAR(127) DEFAULT NULL,
    `Applications`              VARCHAR(127) DEFAULT NULL,
    `CapacitanceFrequency`      VARCHAR(127) DEFAULT NULL,
    `OperatingTemperature`      VARCHAR(127) DEFAULT NULL,
    `MountingType`              VARCHAR(127) DEFAULT NULL,
    `PartStatus`                VARCHAR(127) DEFAULT NULL,
    `PackageCase`               VARCHAR(127) DEFAULT NULL,
    `componentlink1description` VARCHAR(100) DEFAULT NULL,
    `supplier6`                 VARCHAR(100) DEFAULT NULL,
    `lastupdated`               DATETIME ON UPDATE CURRENT_TIMESTAMP,
    `archived`                  BIT          DEFAULT 0,
    `value`                     VARCHAR(100) DEFAULT NULL,
    `comment`                   VARCHAR(100) DEFAULT NULL,
    `manufacturerpartno`        VARCHAR(100) NOT NULL,
    `manufacturer`              VARCHAR(100) NOT NULL,
    `description`               VARCHAR(200) DEFAULT NULL,
    `price`                     VARCHAR(100) DEFAULT NULL,
    `lifecycle`                 VARCHAR(100) DEFAULT NULL,
    `series`                    VARCHAR(100) DEFAULT NULL,
    `footprintref`              VARCHAR(100) DEFAULT NULL,
    `footprintpath`             VARCHAR(100) DEFAULT NULL,
    `symbolref`                 VARCHAR(100) DEFAULT NULL,
    `symbolpath`                VARCHAR(100) DEFAULT NULL,
    `SupplierDevicePackage`     VARCHAR(127) DEFAULT NULL,
    `devicepackage`             VARCHAR(100) DEFAULT NULL,
    `packaging`                 VARCHAR(100) DEFAULT NULL,
    `minimumorder`              INT          DEFAULT 0,
    `supplier1`                 VARCHAR(100) DEFAULT NULL,
    `supplier1partno`           VARCHAR(150) DEFAULT NULL,
    `supplier2`                 VARCHAR(100) DEFAULT NULL,
    `supplier2partno`           VARCHAR(150) DEFAULT NULL,
    `supplier3`                 VARCHAR(100) DEFAULT NULL,
    `supplier3partno`           VARCHAR(150) DEFAULT NULL,
    `supplier4`                 VARCHAR(100) DEFAULT NULL,
    `supplier4partno`           VARCHAR(150) DEFAULT NULL,
    `supplier5`                 VARCHAR(100) DEFAULT NULL,
    `supplier5partno`           VARCHAR(150) DEFAULT NULL,
    `supplier6partno`           VARCHAR(150) DEFAULT NULL,
    INDEX (`lastupdated`),
    INDEX (`archived`),
    INDEX (`manufacturerpartno`),
    PRIMARY KEY (`manufacturerpartno`, `manufacturer`)
);

DROP VIEW IF EXISTS Diodes_TVS;

CREATE VIEW Diodes_TVS AS
SELECT `Applications`              AS `Applications`,
       `BidirectionalChannels`     AS `Bidirectional Channels`,
       `CapacitanceFrequency`      AS `Capacitance @ Frequency`,
       `comment`                   AS `Comment`,
       `componentlink1description` AS `ComponentLink1Description`,
       `componentlink1url`         AS `ComponentLink1URL`,
       `componentlink2description` AS `ComponentLink2Description`,
       `componentlink2url`         AS `ComponentLink2URL`,
       `componentlink3description` AS `ComponentLink3Description`,
       `componentlink3url`         AS `ComponentLink3URL`,
       `componentlink4description` AS `ComponentLink4Description`,
       `componentlink4url`         AS `ComponentLink4URL`,
       `componentlink5description` AS `ComponentLink5Description`,
       `componentlink5url`         AS `ComponentLink5URL`,
       `componentlink6description` AS `ComponentLink6Description`,
       `componentlink6url`         AS `ComponentLink6URL`,
       `CurrentPeakPulse101000µs`  AS `Current - Peak Pulse (10/1000µs)`,
       `description`               AS `Description`,
       `devicepackage`             AS `Device Package`,
       `footprintpath`             AS `Footprint Path`,
       `footprintpath2`            AS `Footprint Path 2`,
       `footprintpath3`            AS `Footprint Path 3`,
       `footprintref`              AS `Footprint Ref`,
       `footprintref2`             AS `Footprint Ref 2`,
       `footprintref3`             AS `Footprint Ref 3`,
       `lastupdated`               AS `LastUpdated`,
       `lifecycle`                 AS `Lifecycle Status`,
       `manufacturer`              AS `Manufacturer`,
       `manufacturerpartno`        AS `Part Number`,
       `minimumorder`              AS `Minimum Order`,
       `MountingType`              AS `Mounting Type`,
       `OperatingTemperature`      AS `Operating Temperature`,
       `PackageCase`               AS `Package / Case`,
       `packaging`                 AS `Packaging`,
       `PartStatus`                AS `Part Status`,
       `PowerLineProtection`       AS `Power Line Protection`,
       `PowerPeakPulse`            AS `Power - Peak Pulse`,
       `price`                     AS `Price`,
       `series`                    AS `Series`,
       `supplier1`                 AS `Supplier 1`,
       `supplier1partno`           AS `Supplier Part Number 1`,
       `supplier2`                 AS `Supplier 2`,
       `supplier2partno`           AS `Supplier Part Number 2`,
       `supplier3`                 AS `Supplier 3`,
       `supplier3partno`           AS `Supplier Part Number 3`,
       `supplier4`                 AS `Supplier 4`,
       `supplier4partno`           AS `Supplier Part Number 4`,
       `supplier5`                 AS `Supplier 5`,
       `supplier5partno`           AS `Supplier Part Number 5`,
       `supplier6`                 AS `Supplier 6`,
       `supplier6partno`           AS `Supplier Part Number 6`,
       `SupplierDevicePackage`     AS `Supplier Device Package`,
       `symbolpath`                AS `Library Path`,
       `symbolref`                 AS `Library Ref`,
       `type`                      AS `Type`,
       `UnidirectionalChannels`    AS `Unidirectional Channels`,
       `value`                     AS `Value`,
       `VoltageBreakdownMin`       AS `Voltage - Breakdown (Min)`,
       `VoltageClampingMaxIpp`     AS `Voltage - Clamping (Max) @ Ipp`,
       `VoltageReverseStandoffTyp` AS `Voltage - Reverse Standoff (Typ)`
FROM t_DiodesTVS t;