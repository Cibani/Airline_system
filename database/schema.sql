CREATE DATABASE musicdb;
USE musicdb;

CREATE TABLE songs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    artist VARCHAR(100),
    album VARCHAR(100),
    genre VARCHAR(50),
    year INT
);
