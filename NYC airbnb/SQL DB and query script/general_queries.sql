/******						For using the correct DB at all times					******/
USE nyc_airbnb;



/******						Index for speeding up collection of information						******/
CREATE INDEX relevant_fields
on clean_data.cleaned_airbnb_data(	
	host_id, 
	host_name, 
	neighbourhood_group, 
	neighbourhood,	
	room_type,	
	price,	
	minimum_nights,	
	number_of_reviews, 
	last_review, 
	reviews_per_month,	
	calculated_host_listings_count,	
	availability_365
	);

/******						Queries for business needs						******/
-- 1. Find the top 20 most expensive listings in Manhattan. Order them by highest price to lowest price
SELECT TOP 20 
	host_name, 
	name, 
	price, 
	neighbourhood, 
	neighbourhood_group, 
	room_type, 
	minimum_nights, 
	number_of_reviews 
FROM 
	clean_data.cleaned_airbnb_data WHERE neighbourhood_group LIKE '%Manhattan%' 
ORDER BY
	price desc;


-- 2. Find all listings within the Bronx and create a new column that identifies the avg price of a bronx listing and another column that classifies whether the price of the listing is above average or not
SELECT 
	host_id, 
	host_name, 
	name, 
	room_type, 
	price,
	AVG(price) OVER (partition by neighbourhood_group) as avg_listing_price_bx,
	CASE
		WHEN price > AVG(price) OVER (partition by neighbourhood_group) THEN 'Above average'
		ELSE 'Not above average'
	END AS 'price_category'
FROM 
	clean_data.cleaned_airbnb_data
WHERE 
	neighbourhood_group = 'Bronx';


-- 3. We have the cleaned and raw_data. I do not know the substitute values given for NULLS in the clean dataset.
--	  Therefore, I would like to see all rows from the clean dataset that had host names as NULL in the original_dataset.
--	  I do not want to see the NULL values within the other columns
SELECT 
	cleaned_airbnb_data.* 
FROM 
	clean_data.cleaned_airbnb_data 
LEFT JOIN
	raw_data.original_data
ON 
	 clean_data.cleaned_airbnb_data.id = raw_data.original_data.id
WHERE original_data.host_name IS NULL;

-- 4. For the borough of Brooklyn, I would like to see a comparison between the price of the current listing and the listing that recieved its last review before it
SELECT 
	id,
	name,
	host_id,
	host_name,
	neighbourhood,
	neighbourhood_group,
	room_type,
	price,
	LAG(price) OVER (PARTITION BY neighbourhood_group order by reviews_per_month asc) AS price_of_listing_with_monthly_review_rate_below
FROM 
	clean_data.cleaned_airbnb_data
WHERE 
	neighbourhood_group = 'Brooklyn';



-- 5.(Bonus): If the calculated listings column was not apart of the dataset. Find a way to find the hosts with the most listings from each borough and order by most listings to least listings
WITH listing_borough_count AS
(
	SELECT
		neighbourhood_group,
		host_id, 
		host_name, 
		COUNT(*) as listings_count,
		ROW_NUMBER() OVER (PARTITION BY neighbourhood_group ORDER BY COUNT(*) DESC) AS rank
	FROM 
		clean_data.cleaned_airbnb_data
	GROUP BY 
		neighbourhood_group, 
		HOST_ID, 
		HOST_NAME
)
SELECT 
	host_id, 
	host_name, 
	neighbourhood_group,
	listings_count
FROM 
	listing_borough_count
WHERE 
	rank = 1
ORDER BY
	listings_count desc;



