# NYC Airbnb Dataset Analysis and AB Testing Project

## Overview

This project aims to analyze the 2019 NYC Airbnb dataset, conduct data cleaning and manipulation, perform exploratory data analysis (EDA), and conduct an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn. The analysis is conducted using Python and various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scipy, and Statsmodels. Additionally, the project involves the creation of a machine learning model to predict room types and an SQL database for effective data management.

## Project Objectives

1. **Data Cleaning and Manipulation:** Clean up the dataset for proper use with analysis and machine learning.
2. **Exploratory Data Analysis (EDA):** Conduct EDA to gain insights into the dataset and visualize the relationships between various attributes.
3. **AB Testing:** Perform an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn.
4. **Machine Learning:** Create a machine learning model to predict room types for listings.
5. **SQL Database Creation:** Implement SQL database creation with triggers, transactions, and stored procedures.
6. **Showcasing of Findings:** Use Tableau and Streamlit to visualize and present the insights and findings from the data.

## Dataset Description

The dataset consists of various attributes related to Airbnb listings in NYC, including listing details, host information, location coordinates, pricing, availability, and reviews.

## Project Progress

1. **Data Cleaning and Manipulation:** Completed data cleaning and handling of null values in relevant columns. Unrealistic price listings and listings with no availability were filtered out.
2. **Exploratory Data Analysis (EDA):** Conducted initial EDA to visualize the distribution of quantitative variables and understand relationships between attributes.
3. **AB Testing:** Performed an AB test to compare the distribution of prices between listings in Manhattan and Brooklyn. The test results showed a significant difference, with listings in Manhattan having a higher average price than those in Brooklyn.

## Next Steps

1. **Predicting Room Type for a Listing:** Develop a machine learning model using either a random forest or decision tree classifier to predict the room type for a listing. This new feature is optional on the platform and is currently being inferred from the title. The model will use features such as `host_id`, `name`, `neighborhood`, `neighbourhood group`, `price`, `number of reviews`, `reviews per month`, and `calculated_host_listings_count`. NLP may be required for the model. Once the model is completed, save it for future use.
2. **SQL Database Creation:** Implement SQL database creation with triggers, transactions, and stored procedures.
3. **Generate Visualizations using Tableau:** For in-depth data exploration and visualizations.
4. **Create Streamlit web apps:** To showcase findings and insights from the data.

## Conclusion

The project aims to provide valuable insights into the NYC Airbnb dataset, including factors influencing pricing and booking popularity. By leveraging data analysis, machine learning, SQL databases, and visualization tools, the project aims to deliver actionable insights for Airbnb hosts and stakeholders.
