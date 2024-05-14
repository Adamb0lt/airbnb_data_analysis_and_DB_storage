USE nyc_airbnb;


/******						Table Creation						******/
-- Create table for original data
CREATE TABLE raw_data.original_data (
    id INT PRIMARY KEY,
    [name] NVARCHAR(MAX),
    [host_id] NVARCHAR(MAX),
    [host_name] NVARCHAR(MAX),
    neighbourhood_group NVARCHAR(150),
    neighbourhood NVARCHAR(50),
    latitude NVARCHAR(50),
    longitude NVARCHAR(50),
    room_type NVARCHAR(50),
    price NVARCHAR(50),
    minimum_nights NVARCHAR(150),
    number_of_reviews NVARCHAR(150),
    last_review NVARCHAR(50),
    reviews_per_month NVARCHAR(50),
    calculated_host_listings_count NVARCHAR(50),
    availability_365 NVARCHAR(50)
);

-- Create table for cleaned data
CREATE TABLE clean_data.cleaned_data(
	id INT PRIMARY KEY,
	name NVARCHAR(255),
	host_id NVARCHAR(255),
	host_name NVARCHAR(255),
	neighbourhood_group NVARCHAR(255),
	neighbourhood NVARCHAR(255),
	room_type NVARCHAR(255),
	price NVARCHAR(255),
	number_of_reviews  NVARCHAR(255),
	last_review NVARCHAR(255),
	reviews_per_month  NVARCHAR(255),
	calculated_host_listings_count  NVARCHAR(255),
	availability_365 NVARCHAR(255)
	);

-- Table for storing host information
CREATE TABLE hosts(
	host_id INT PRIMARY KEY, -- PRIMARY KEY
	host_name VARCHAR NOT NULL,
	listings_count INT,
	total_reviews as (SELECT COUNT(number_of_reviews) 
						FROM raw_data.original_data 
							WHERE host_id = raw_data.original_data.host_id
							),
	avg_reviews_per_month AS (SELECT AVG(reviews_per_month) 
								FROM raw_data.original_data.host_id
									WHERE host_id = raw_data.original_data.host_id)
	);


-- Table for storing listings information
CREATE TABLE listings(
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