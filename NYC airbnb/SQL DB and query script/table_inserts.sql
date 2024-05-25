/******						For using the correct DB at all times					******/
USE nyc_airbnb;

/******						INSERTS						******/

/*** Important Note:
If the scripts for either table inserts do not work, do the following as an alternative and repeat for each version of the airbnb dataset
1. Go over to the object explorer and select "Databases".
2. Select the "nyc_airbnb" database and then select "tables". Delete the table that produced the error with the insert.
3. Refresh the object explorer connection and then select "Databases" and then left click on the "nyc_airbnb" Database.
4. Left click on the nyc_airbnb database and scroll over to "Tasks" and then scroll over to "Import Flat File" and select that option
5. Find the file path/location where you stored the "cleaned airbnb and the original airbnb" files and enter it into the location.
6. Select the appropriate schema for the dataset
7. Click next to preview the data and then click next again to modify the columns.
8. Enter the exact data types listed within the scripts on the table_creation.sql script for the data types in the Import wizard.
9. Once done, click next and on the summary screen ensure details are correct and then click Finish.
10. Repeat for the other dataset if it needs to be done.
***/


-- INSERT for original data
BULK INSERT raw_data.original_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\AB_NYC_2019.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2,
	KEEPNULLS,
	-- ERRORFILE = 'This is completely optional.If you want, uncomment and create a txt file to store an error log if an error occurs. Example: /user/error_log.txt',
	TABLOCK
);


-- Bulk insert for the clean data
BULK INSERT clean_data.cleaned_airbnb_data
FROM 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\data\cleaned_airbnb_data.csv' -- File path of data
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '/r/n',
	FIRSTROW = 2
	-- ERRORFILE = 'C:\Users\adwal\OneDrive\Desktop\Professional\Projects\Python_SQL_+\Python_SQL_App\NYC airbnb\SQL DB and query script\error_log1.txt',

);