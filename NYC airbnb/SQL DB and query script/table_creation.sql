/******						For using the correct DB at all times					******/
USE nyc_airbnb;


/******						Table Creation						******/
-- Table for the raw/original_data
CREATE TABLE raw_data.original_data (
    id INT PRIMARY KEY,
    name NVARCHAR(MAX),
    host_id INT,
    host_name NVARCHAR(50),
    neighbourhood_group NVARCHAR(50),
    neighbourhood NVARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    room_type NVARCHAR(50),
    price INT,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month FLOAT,
    calculated_host_listings_count INT,
    availability_365 INT
);

-- Table for the clean data
CREATE TABLE clean_data.cleaned_airbnb_data (
    id INT PRIMARY KEY,
    name NVARCHAR(MAX),
    host_id INT,
    host_name NVARCHAR(50),
    neighbourhood_group NVARCHAR(50),
    neighbourhood NVARCHAR(50),
    latitude FLOAT,
    longitude FLOAT,
    room_type NVARCHAR(50),
    price INT,
    minimum_nights INT,
    number_of_reviews INT,
    last_review DATE,
    reviews_per_month FLOAT,
    calculated_host_listings_count INT,
    availability_365 INT
);
