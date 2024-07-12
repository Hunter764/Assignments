drop database Salesdb;

create database Salesdb;

use Salesdb;

CREATE DATABASE SALES_DB;
USE SALES_DB;


CREATE TABLE productlines (
    productLine VARCHAR(50) PRIMARY KEY,
    textDescription VARCHAR(4000),
    htmlDescription MEDIUMTEXT,
    image MEDIUMBLOB
);

CREATE TABLE products (
    productCode VARCHAR(15) PRIMARY KEY,
    productName VARCHAR(70) NOT NULL,
    productLine VARCHAR(50),
    productScale VARCHAR(10) NOT NULL,
    productVendor VARCHAR(50) NOT NULL,
    productDescription TEXT NOT NULL,
    quantityInStock SMALLINT NOT NULL,
    buyPrice DECIMAL(10, 2) NOT NULL,
    MSRP DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (productLine) 
    REFERENCES productlines(productLine)
);

CREATE TABLE employees (
    employeeNumber INT PRIMARY KEY,
    lastName VARCHAR(50) NOT NULL,
    firstName VARCHAR(50) NOT NULL,
    extension VARCHAR(10) NOT NULL,
    email VARCHAR(100) NOT NULL,
    officeCode VARCHAR(10),
    reportsTo INT,
    jobTitle VARCHAR(50) NOT NULL,
    FOREIGN KEY (officeCode) 
    REFERENCES offices(officeCode),
    FOREIGN KEY (reportsTo) 
    REFERENCES employees(employeeNumber)
);

CREATE TABLE offices (
    officeCode VARCHAR(10) PRIMARY KEY,
    city VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    addressLine1 VARCHAR(50) NOT NULL,
    addressLine2 VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50) NOT NULL,
    postalCode VARCHAR(15) NOT NULL,
    territory VARCHAR(10) NOT NULL
);

CREATE TABLE customers (
    customerNumber INT PRIMARY KEY,
    customerName VARCHAR(50) NOT NULL,
    contactLastName VARCHAR(50) NOT NULL,
    contactFirstName VARCHAR(50) NOT NULL,
    phone VARCHAR(50) NOT NULL,
    addressLine1 VARCHAR(50) NOT NULL,
    addressLine2 VARCHAR(50),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50),
    postalCode VARCHAR(15),
    country VARCHAR(50) NOT NULL,
    salesRepEmployeeNumber INT,
    creditLimit DECIMAL(10, 2),
    FOREIGN KEY (salesRepEmployeeNumber) 
    REFERENCES employees(employeeNumber)
);

CREATE TABLE orders (
    orderNumber INT PRIMARY KEY,
    orderDate DATE NOT NULL,
    requiredDate DATE NOT NULL,
    shippedDate DATE,
    status_ VARCHAR(15) NOT NULL,
    comments TEXT,
    customerNumber INT,
    FOREIGN KEY (customerNumber) 
    REFERENCES customers(customerNumber)
);

CREATE TABLE orderDetails (
    orderNumber INT,
    productCode VARCHAR(15),
    quantityOrdered INT NOT NULL,
    priceEach DECIMAL(10, 2) NOT NULL,
    orderLineNumber SMALLINT NOT NULL,
    PRIMARY KEY (orderNumber, productCode),
    FOREIGN KEY (orderNumber) 
    REFERENCES orders(orderNumber),
    FOREIGN KEY (productCode) 
    REFERENCES products(productCode)
);

CREATE TABLE payments (
    customerNumber INT,
    checkNumber VARCHAR(50) PRIMARY KEY,
    paymentDate DATE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customerNumber) 
    REFERENCES customers(customerNumber)
);

show tables;

ALTER TABLE orders
RENAME COLUMN status to status_;

INSERT INTO productLines (productLine, textDescription, htmlDescription, image) VALUES
('Classic Cars', 'Detailed replicas of classic cars', '<p>Detailed replicas of classic cars</p>', NULL),
('Motorcycles', 'Scale models of motorcycles', '<p>Scale models of motorcycles</p>', NULL),
('Planes', 'Model planes including biplanes and jets', '<p>Model planes including biplanes and jets</p>', NULL),
('Ships', 'Replica ships and boats', '<p>Replica ships and boats</p>', NULL),
('Trains', 'Model trains and accessories', '<p>Model trains and accessories</p>', NULL);


INSERT INTO products (productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES
('S10_1678', '1969 Harley Davidson Ultimate Chopper', 'Motorcycles', '1:10', 'Min Lin Diecast', 'This replica features rotating wheels and handle bars.', 7933, 48.81, 95.70),
('S10_1949', '1952 Alpine Renault 1300', 'Classic Cars', '1:10', 'Classic Metal Creations', 'Turnable front wheels; steerable.', 7305, 98.58, 214.30),
('S10_2016', '1996 Moto Guzzi 1100i', 'Motorcycles', '1:10', 'Highway 66 Mini Classics', 'Two-piece wheels; steel rims; working kick stand.', 6625, 68.99, 118.94),
('S10_4698', '2003 Harley-Davidson Eagle Drag Bike', 'Motorcycles', '1:10', 'Red Start Diecast', 'Detailed model; working suspension.', 5582, 91.02, 193.66),
('S10_4757', '1972 Alfa Romeo GTA', 'Classic Cars', '1:10', 'Classic Metal Creations', 'Detailed interior; steerable wheels.', 3251, 85.68, 146.99);


INSERT INTO offices (officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory) VALUES
('1', 'San Francisco', '+1 650 219 4782', '100 Market Street', 'Suite 300', 'CA', 'USA', '94080', 'NA'),
('2', 'Boston', '+1 215 837 0825', '1550 Court Place', 'Suite 100', 'MA', 'USA', '02107', 'NA'),
('3', 'NYC', '+1 212 555 3000', '523 East 53rd Street', 'apt. 5A', 'NY', 'USA', '10022', 'NA'),
('4', 'Paris', '+33 14 723 4404', '43 Rue Jouffroy D\'abbans', NULL, 'Paris', 'France', '75017', 'EMEA'),
('5', 'Tokyo', '+81 33 224 5000', '4-1 Kioicho', 'Chiyoda-Ku', 'Tokyo', 'Japan', '102-8578', 'Japan');


INSERT INTO employees (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle) VALUES
(1002, 'Murphy', 'Diane', 'x5800', 'dmurphy@classicmodelcars.com', '1', NULL, 'President'),
(1056, 'Patterson', 'Mary', 'x4611', 'mpatter@classicmodelcars.com', '1', 1002, 'VP Sales'),
(1076, 'Firrelli', 'Jeff', 'x9273', 'jfirrelli@classicmodelcars.com', '1', 1002, 'VP Marketing'),
(1088, 'Bondur', 'Anthony', 'x5408', 'abondur@classicmodelcars.com', '1', 1056, 'Sales Manager (APAC)'),
(1102, 'Bow', 'Leslie', 'x5428', 'lbow@classicmodelcars.com', '2', 1056, 'Sales Manager (EMEA)');


INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit) VALUES
(103, 'Atelier graphique', 'Schmitt', 'Carine', '40.32.2555', '54, rue Royale', NULL, 'Nantes', NULL, '44000', 'France', 1088, 21000.00),
(112, 'Signal Gift Stores', 'King', 'Jean', '7025551838', '8489 Strong St.', NULL, 'Las Vegas', 'NV', '83030', 'USA', 1102, 71800.00),
(114, 'Australian Collectors, Co.', 'Ferguson', 'Peter', '03 9520 4555', '636 St Kilda Road', 'Level 3', 'Melbourne', 'Victoria', '3004', 'Australia', 1076, 117300.00),
(119, 'La Rochelle Gifts', 'Labrune', 'Janine', '40.67.8555', '67, rue des Cinquante Otages', NULL, 'Nantes', NULL, '44000', 'France', 1088, 118200.00),
(121, 'Baane Mini Imports', 'Bergulfsen', 'Jonas', '07-98 9555', 'Erling Skakkes gate 78', NULL, 'Stavern', NULL, '4110', 'Norway', 1056, 81700.00);


INSERT INTO orders (orderNumber, orderDate, requiredDate, shippedDate, status_, comments, customerNumber) VALUES
(10100, '2023-01-10', '2023-01-13', '2023-01-11', 'Shipped', 'Delivered on time', 103),
(10101, '2023-02-05', '2023-02-12', '2023-02-06', 'Shipped', 'Delayed due to weather', 112),
(10102, '2023-03-18', '2023-03-25', NULL, 'In Process', NULL, 114),
(10103, '2023-04-22', '2023-04-30', '2023-04-23', 'Shipped', 'Customer requested late delivery', 119),
(10104, '2023-05-14', '2023-05-21', NULL, 'On Hold', 'Awaiting payment', 121);


INSERT INTO orderDetails (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) VALUES
(10100, 'S10_1678', 30, 95.70, 1),
(10101, 'S10_1949', 50, 214.30, 2),
(10102, 'S10_2016', 27, 118.94, 3),
(10103, 'S10_4698', 15, 193.66, 4),
(10104, 'S10_4757', 45, 146.99, 5);


INSERT INTO payments (customerNumber, checkNumber, paymentDate, amount) VALUES
(103, 'HQ336338', '2023-01-15', 21000.00),
(112, 'JM555123', '2023-02-10', 71800.00),
(114, 'BK987654', '2023-03-20', 117300.00),
(119, 'NR111222', '2023-04-25', 118200.00),
(121, 'LL543210', '2023-05-18', 81700.00);
