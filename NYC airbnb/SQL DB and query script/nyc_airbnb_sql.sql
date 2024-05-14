/******						Database Creation and Usage						******/
-- Create Database
CREATE DATABASE nyc_airbnb;

-- Use Database
USE nyc_airbnb;


/******						Schema Creation for partitioning tables						******/
-- Schemas for separating original and cleaned data
CREATE SCHEMA raw_data;
CREATE SCHEMA clean_data;








/*
TODO: 
- INSERTS OF THE ORIGINAL DATA AND CLEANED DATA
- MAYBE START CREATING TRIGGERS
- UNDERSTAND THE UI A LOT BETTER TO ENSURE FILE IS IN THE RIGHT PLACE
- CLEANING UP SYNTAX FOR CODE
- TEST FUNCTIONALITY WITH JUST TRIGGERS IN PLACE
- TEST SOME QUERIES ON DATA INSERTED IN AND ALSO ON TRIGGERS
- IF POSSIBLE ALSO LOOK INTO STORED PROCEDURES AND TRANSACTIONS
*/







