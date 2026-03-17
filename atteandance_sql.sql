CREATE DATABASE IF NOT EXISTS attendance_db;

USE attendance_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    email VARCHAR(100),
    face_embedding LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    date DATE,
    punch_in TIME,
    punch_out TIME,
    status VARCHAR(50),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
);
USE attendance_db;
ALTER TABLE employees ADD COLUMN face_embedding LONGTEXT;
USE attendance_db;
SELECT id, name, department, email, created_at FROM employees;
-- Delete all Rashika duplicates except the last one
SET SQL_SAFE_UPDATES = 1;
SELECT e.name, a.date, a.punch_in, a.punch_out, a.status 
FROM attendance a 
JOIN employees e ON a.employee_id = e.id;
USE attendance_db;

-- Step 1: Disable foreign key check
SET FOREIGN_KEY_CHECKS = 1;

