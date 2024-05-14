USE nyc_airbnb_sql.sql;

/******						INSERTS						******/
-- INSERT STATEMENTS for original data and cleaned data
BULK INSERT raw_data.original_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\AB_NYC_2019.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2,
	KEEPNULLS,
	-- ERRORFILE = 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\SQL DB and query script\error_log.txt',
	TABLOCK
);

SELECT TOP 100 * FROM raw_data.original_data;
BULK INSERT cleaned_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\cleaned_airbnb_data.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2,
	KEEPNULLS,
	ERRORFILE = 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\SQL DB and query script\error_log1.txt',
	TABLOCK
);


-- Insert for extra tables
INSERT INTO 