


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
-- Find me the top 20 most expensive in Manhattan order by highest price
SELECT TOP 20 
	host_name, name, price, neighbourhood, neighbourhood_group, room_type, minimum_nights, number_of_reviews 
		FROM clean_data.cleaned_airbnb_data WHERE neighbourhood_group LIKE '%Manhattan%' 
		ORDER BY
			price desc;

-- Find the hosts with the most listings from each borough and order by most listings to least listings
SELECT host_id, host_name, COUNT(host_id) as listings_count 
	FROM clean_data.cleaned_airbnb_data 
		GROUP BY neighbourhood_group
		HAVING MAX(listings_count)
			ORDER BY listings_count desc;



