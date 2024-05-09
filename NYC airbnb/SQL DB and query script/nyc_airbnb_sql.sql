-- Create Database
CREATE DATABASE nyc_airbnb;

-- Use Database
USE nyc_airbnb;

CREATE TABLE original_data(
	id INT PRIMARY KEY,
	name VARCHAR(50),	
	host_id INT,	
	host_name VARCHAR(50),	
	neighbourhood_group VARCHAR(50),	
	neighbourhood VARCHAR(50),	
	latitude DECIMAL(8,5),	
	longitude DECIMAL(8,5),	
	room_type VARCHAR(50),	
	price smallmoney,	
	minimum_nights tinyint,	
	number_of_reviews smallint,	
	last_review datetime,
	reviews_per_month decimal,	
	calculated_host_listings_count tinyint,	
	availability_365 smallint
);

-- less attributes that original table with no null values
CREATE TABLE cleaned_data(
	id INT,
	name VARCHAR(50),	
	host_id INT,	
	host_name VARCHAR(50),	
	neighbourhood_group VARCHAR(50),	
	neighbourhood VARCHAR(50),	
	room_type VARCHAR(50),	
	price smallmoney,	
	number_of_reviews smallint,	
	last_review datetime,
	reviews_per_month decimal,	
	calculated_host_listings_count tinyint,	
	availability_365 smallint,
	FOREIGN KEY (id) REFERENCES original_data(id)
);


DROP TABLE original_data;



-- INSERT STATEMENTS for original data and cleaned data
BULK INSERT original_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\AB_NYC_2019.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2,
	KEEPNULLS,
	ERRORFILE = 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\SQL DB and query script\error_log.txt',
	TABLOCK
);

BULK INSERT cleaned_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\AB_NYC_2019.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2,
	KEEPNULLS,
	ERRORFILE = 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\SQL DB and query script\error_log1.txt',
	TABLOCK
);

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







