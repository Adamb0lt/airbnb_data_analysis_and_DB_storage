CREATE DATABASE nyc_airbnb;
USE nyc_airbnb;

DROP DATABASE nyc_airbnb;


-- Info on hosts and their overall performance. 
-- Triggers, Stored Procedures and Transactions will be needed for table
CREATE TABLE nyc_airbnb.hosts(
	host_id UNIQUE INT, -- PRIMARY KEY
	host_name VARCHAR NOT NULL,
	listings_count INT,
	total_reviews INT,
	avg_ reviews_per_month
	);

-- Seems like simple table for now. Don't see where I will need to update anything here
CREATE TABLE nyc_airbnb.listings(
	id UNIQUE INT PRIMARY KEY,
	host_id INT,
	host_name VARCHAR(50) NOT NULL,
	latitude DECIMAL, 
	longitude DECIMAL,
	listing_name VARCHAR(50) NOT NULL,
	neighborhood_group VARCHAR(30) NOT NULL,
	neighborhood VARCHAR(30) NOT NULL,
	room_type VARCHAR(30),
	price DECIMAL NOT NULL,
	number_of_reviews NOT NULL,
	last_review DATE,
	reviews_per_month DECIMAL,
	availability_365 INT
	);

CREATE TABLE nyc_airbnb.clean_data();-- probs just rely on inserting data for this like with OG dataset.

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







