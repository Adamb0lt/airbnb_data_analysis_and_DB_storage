# NYC Airbnb Dataset Analysis and AB Testing Project

## Overview
This project aims to analyze the 2019 NYC Airbnb dataset, conduct data cleaning and manipulation, perform exploratory data analysis (EDA), and conduct an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn. The analysis is conducted using Python and various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scipy, Statsmodels, and Scikit-learn. Additionally, the project involves the creation of a machine learning model to predict room types, generation of visualizations using Tableau, and the development of a Streamlit web application to showcase findings and insights from the data analysis. An SQL database will also be implemented for effective data management.

The dataset used in this project is obtained from Kaggle: [NYC Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).

## Project Objectives

1. **Data Cleaning and Manipulation:** Clean up the dataset for proper use with analysis and machine learning.
2. **Exploratory Data Analysis (EDA):** Conduct EDA to gain insights into the dataset and visualize the relationships between various attributes.
3. **AB Testing:** Perform an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn.
4. **Machine Learning:** Create a machine learning model to predict room types for listings.
5. **SQL Database Creation:** Implement SQL database with schemas for clean and raw data, tables for data storage, and optimized querying with Index. Showcase database capabilities through various SQL queries.
6. **Showcasing of Findings:** Use Tableau and Streamlit to visualize and present the insights and findings from the data.

## Dataset Description
The dataset consists of various attributes related to Airbnb listings in NYC, including listing details, host information, location coordinates, pricing, availability, and reviews.

## Project Progress

1. **Data Cleaning and Manipulation:** Completed data cleaning and handling of null values in relevant columns. Unrealistic price listings and listings with no availability were filtered out.

2. **Exploratory Data Analysis (EDA):** Conducted initial EDA to visualize the distribution of quantitative variables and understand relationships between attributes.

3. **AB Testing:** Performed an AB test to compare the distribution of prices between listings in Manhattan and Brooklyn. The test results showed a significant difference, with listings in Manhattan having a higher average price than those in Brooklyn.

4. **Predicting Room Type for a Listing:** Developed a machine learning model using both Random Forest and Decision Tree classifiers to predict the room type for a listing. The models were trained and evaluated using features such as `host_id`, `name`, `neighborhood`, `neighbourhood group`, `price`, `number of reviews`, `reviews per month`, and `calculated_host_listings_count`. The Random Forest Classifier achieved a higher accuracy score compared to the Decision Tree Classifier.

5. **Generate Visualizations using Tableau:** Completed the creation of comprehensive data visualizations and dashboards using Tableau to further explore and present insights from the dataset.

6. **SQL Database Creation:** Created an SQL database for the NYC Airbnb dataset with separate schemas for clean and raw data. Designed tables for each schema, inserted data, and optimized performance with an Index. Demonstrated database functionality through SQL queries, showcasing features like joins, CTEs, and Window Functions.

7. **Streamlit Web App:** Developed and deployed a Streamlit web application to showcase the findings & insights from the data analysis. The app includes key visualizations and interactive elements to provide an engaging user experience.

You can explore the Streamlit web application and summarized findings from the project here: [Streamlit App - NYC Airbnb Data Visualization](https://airbnb-data-viz-adam.streamlit.app/).

## Conclusion
The project has successfully completed the data cleaning, exploratory analysis, AB testing, machine learning model development, Tableau visualization, SQL database creation, and Streamlit web application stages for the NYC Airbnb dataset. By leveraging various data analysis techniques and tools, the project delivers actionable insights for Airbnb hosts and stakeholders.

Feel free to explore the Streamlit app and reach out if you have any questions or feedback!
