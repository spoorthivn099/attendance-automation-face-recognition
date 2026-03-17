CREATE DATABASE attendance_db;

USE attendance_db;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    punch_in TIME,
    punch_out TIME,
    status VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);