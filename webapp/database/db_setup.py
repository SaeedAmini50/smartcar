CREATE TABLE customer (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    customer_last_name VARCHAR(50) NOT NULL,
    customer_number VARCHAR(15) UNIQUE,
    customer_date DATE DEFAULT CURRENT_DATE,
    password VARCHAR(100) NOT NULL
);
