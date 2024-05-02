# NYC Airbnb Dataset Analysis and AB Testing Project

## Overview
This project aims to analyze the 2019 NYC Airbnb dataset, conduct data cleaning and manipulation, perform exploratory data analysis (EDA), and conduct an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn. The analysis is conducted using Python and various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scipy, Statsmodels, and Scikit-learn. Additionally, the project involves the creation of a machine learning model to predict room types, generation of visualizations using Tableau, and the development of a Streamlit web application to showcase findings and insights from the data analysis. An SQL database will also be implemented for effective data management.

The dataset used in this project is obtained from Kaggle: https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data

## Project Objectives

1.  **Data Cleaning and Manipulation:** Clean up the dataset for proper use with analysis and machine learning.

2.  **Exploratory Data Analysis (EDA):** Conduct EDA to gain insights into the dataset and visualize the relationships between various attributes.

3.  **AB Testing:** Perform an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn.

4.  **Machine Learning:** Create a machine learning model to predict room types for listings.

5.  **SQL Database Creation:** Implement SQL database creation with triggers, transactions, and stored procedures.

6.  **Showcasing of Findings:** Use Tableau and Streamlit to visualize and present the insights and findings from the data.


## Dataset Description
The dataset consists of various attributes related to Airbnb listings in NYC, including listing details, host information, location coordinates, pricing, availability, and reviews.

## Project Progress

1.  **Data Cleaning and Manipulation:** Completed data cleaning and handling of null values in relevant columns. Unrealistic price listings and listings with no availability were filtered out.

2.  **Exploratory Data Analysis (EDA):** Conducted initial EDA to visualize the distribution of quantitative variables and understand relationships between attributes.

3.  **AB Testing:** Performed an AB test to compare the distribution of prices between listings in Manhattan and Brooklyn. The test results showed a significant difference, with listings in Manhattan having a higher average price than those in Brooklyn.

4.  **Predicting Room Type for a Listing:** Developed a machine learning model using both Random Forest and Decision Tree classifiers to predict the room type for a listing. The models were trained and evaluated using features such as `host_id`, `name`, `neighborhood`, `neighbourhood group`, `price`, `number of reviews`, `reviews per month`, and `calculated_host_listings_count`. The Random Forest Classifier achieved a higher accuracy score compared to the Decision Tree Classifier.


## Next Steps

1.  **SQL Database Creation:** Implement SQL database creation with triggers, transactions, and stored procedures to manage the Airbnb dataset efficiently.

2.  **Generate Visualizations using Tableau:** Create in-depth data visualizations and dashboards using Tableau for comprehensive data exploration and insights.

3.  **Create Streamlit Web Apps:** Develop Streamlit web applications to showcase the findings, insights, and predictive models from the data analysis.


## Conclusion
The project has successfully completed the data cleaning, exploratory analysis, AB testing, and machine learning model development stages for the NYC Airbnb dataset. The next steps involve creating an SQL database, generating visualizations using Tableau, and showcasing the findings and predictive models through Streamlit web applications. By leveraging various data analysis techniques and tools, the project aims to deliver actionable insights for Airbnb hosts and stakeholders.
