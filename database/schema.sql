CREATE DATABASE IF NOT EXISTS airline_db;
USE airline_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role ENUM('USER', 'ADMIN') DEFAULT 'USER',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    from_city VARCHAR(50) NOT NULL,
    to_city VARCHAR(50) NOT NULL,
    departure_date DATE NOT NULL,
    arrival_date DATE NOT NULL,
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    seats_available INT DEFAULT 100,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    flight_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('CONFIRMED', 'CANCELLED') DEFAULT 'CONFIRMED',
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (flight_id) REFERENCES flights(id) ON DELETE CASCADE
);

-- Sample data
INSERT INTO users (username, password, email, role) VALUES 
('admin', 'admin123', 'admin@airline.com', 'ADMIN'),
('user1', 'pass123', 'user1@airline.com', 'USER');

INSERT INTO flights (flight_number, from_city, to_city, departure_date, arrival_date, departure_time, arrival_time, price, seats_available) VALUES 
('AA101', 'New York', 'Los Angeles', '2024-10-15', '2024-10-15', '08:00:00', '11:00:00', 299.99, 50),
('AA102', 'London', 'Paris', '2024-10-16', '2024-10-16', '09:30:00', '11:30:00', 150.00, 30);
