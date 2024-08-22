-- creates the database hbtn_0d_usa and table states(in the database hbtn_0d_usa) on MySQL server
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_0d_usa database
USE hbtn_0d_usa;
-- create a table on hbtn_0d_usa database
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT NOT NULL, name VARCHAR(256) NOT NULL,PRIMARY KEY(ID));
