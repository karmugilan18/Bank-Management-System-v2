-- Bank Management System v2
-- Database Schema — Lesson 4

CREATE DATABASE IF NOT EXISTS bank_management;
USE bank_management;

CREATE TABLE customers (
    customer_id   INT AUTO_INCREMENT PRIMARY KEY,
    full_name     VARCHAR(100) NOT NULL,
    phone         VARCHAR(15)  NOT NULL UNIQUE,
    address       VARCHAR(255),
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE accounts (
    account_id     INT AUTO_INCREMENT PRIMARY KEY,
    account_number VARCHAR(20)    NOT NULL UNIQUE,
    customer_id    INT            NOT NULL,
    account_type   ENUM('savings', 'current') NOT NULL,
    balance        DECIMAL(12, 2) DEFAULT 0.00,
    created_at     DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    transaction_id   INT AUTO_INCREMENT PRIMARY KEY,
    account_id       INT            NOT NULL,
    transaction_type ENUM('deposit', 'withdrawal') NOT NULL,
    amount           DECIMAL(12, 2) NOT NULL,
    timestamp        DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);