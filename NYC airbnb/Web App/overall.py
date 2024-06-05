import streamlit as st

# Title and Subheader
st.title('NYC Airbnb Dataset Analysis and AB Testing Project')
st.subheader('Visualizations Overview')

# Introduction
st.write("""
Welcome to the NYC Airbnb Dataset Analysis and AB Testing Project! This project involves analyzing the 2019 NYC Airbnb dataset to uncover insights and patterns in the data, conduct an AB test, and create predictive models. Visualizations play a crucial role in this project, helping to present findings and insights in an easily understandable manner.

## Visualization Components

### Tableau Visualizations
We have utilized Tableau to create comprehensive visualizations and dashboards that delve into various aspects of the dataset, such as:
- **Distribution of Prices:** Explore the price distribution across different neighborhoods and room types.
- **Geographical Insights:** Visualize the geographic distribution of listings, highlighting popular areas and price variations.
- **Availability and Reviews:** Analyze the availability of listings and the distribution of review scores across different neighborhoods.

These Tableau visualizations are designed to provide a deeper understanding of the data and reveal trends and patterns that might not be immediately apparent through raw data analysis.

### Streamlit Visualizations
In addition to Tableau, we have developed a Streamlit web application to showcase key visualizations directly within this platform. The Streamlit app includes:
- **Price Distribution Comparison:** A visualization of the price distribution between listings in Manhattan and Brooklyn, which is a focal point of our AB testing.
- **Room Type Predictions:** Visual representations of the predictions made by our machine learning models, showing the distribution of predicted room types.
- **EDA Insights:** Interactive charts and graphs that provide insights into various attributes of the dataset, such as the relationship between price and number of reviews, or the distribution of listings by neighborhood.

## How to Navigate
- Use the sidebar to navigate through different sections of the app.
- Explore the visualizations and interact with the charts to gain a deeper understanding of the data.
- Check out the predictive models and their results to see how we leveraged machine learning in this project.

We hope these visualizations help you gain valuable insights into the NYC Airbnb dataset and appreciate the complexity and richness of the data.

### About the Project
This project was conducted using Python and various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scipy, Statsmodels, and Scikit-learn. An SQL database was implemented for effective data management, and Tableau was used for creating visual dashboards. The final step involves creating this Streamlit web app to present our findings and insights in an interactive and user-friendly manner.

Feel free to explore and reach out if you have any questions or feedback!

**Note:** The dataset used in this project is obtained from [Kaggle: NYC Airbnb Open Data](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data).
""")

# Sidebar
st.sidebar.title('Navigation')
st.sidebar.write('Use the options below to explore different sections of the project:')
st.sidebar.radio('Sections', ['Introduction', 'Price Distribution', 'Room Type Predictions', 'EDA Insights'])
