import streamlit as st
import streamlit.components.v1 as components

# CSS for centering and responsiveness
# CSS for centering and responsiveness
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
    .centered div {
        max-width: 100%;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title('Navigation')
section = st.sidebar.radio('Sections', [
    'Introduction',
    'Density of Listings per Borough',
    'Average Number of Reviews per Neighborhood Group',
    'Average Price of Listings per Neighborhood Group',
    'Number of Listings within each Manhattan Neighborhood',
    'Comparison of Average Listing Prices per Neighborhood in Manhattan',
    'Percentage of Different Room Types in Manhattan Listings'
])

if section == 'Introduction':
    st.title('Visualizations from the NYC Airbnb Dataset Analysis and AB Testing Project')
    st.subheader('Visualizations Overview')

    st.write("""
    Welcome to the NYC Airbnb Dataset Analysis and AB Testing Project! This project involves analyzing the 2019 NYC Airbnb dataset to uncover insights and patterns in the data, conduct an AB test, and create predictive models. This portion of the project focuses on visualizations, presenting summarized findings and insights in an easily understandable manner.

    ## Visualization Components

    ### Tableau Visualizations
    We have utilized Tableau to create comprehensive visualizations and dashboards that delve into various aspects of the dataset, such as:
    - **Density of Listings per Borough:** A map visualization showing the density of listings across the five boroughs of NYC.
    - **Average Number of Reviews per Neighborhood Group:** A bar chart depicting the average number of reviews for listings in each borough.
    - **Average Price of Listings per Neighborhood Group:** A bar chart comparing the average prices of listings across the boroughs.
    - **Number of Listings within Each Manhattan Neighborhood:** A heatmap detailing the number of listings in each neighborhood in Manhattan.
    - **Comparison of Average Listing Prices per Neighborhood in Manhattan:** A bubble chart comparing average prices across different Manhattan neighborhoods.
    - **Percentage of Different Room Types in Manhattan Listings:** A pie chart showing the distribution of room types in Manhattan.

    These Tableau visualizations are designed to provide a deeper understanding of the data and reveal trends and patterns that might not be immediately apparent through raw data analysis.

    ## How to Navigate
    - Use the sidebar to navigate through different sections of the app.
    - Explore the visualizations and interact with the charts to gain a deeper understanding of the data.
    - Check out the predictive models and their results to see how we leveraged machine learning in this project.

    We hope these visualizations help you gain valuable insights into the NYC Airbnb dataset and appreciate the complexity and richness of the data.

    ### About the Project
    This project was conducted using Python and various libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scipy, Statsmodels, and Scikit-learn. A SQL database was implemented for effective data management, and Tableau was used for creating visual dashboards. The final step involves creating this Streamlit web app to present our findings and insights in an interactive and user-friendly manner.

    The rest of the project, which includes Data Cleaning and Manipulation, Exploratory Data Analysis (EDA), AB Testing, Machine Learning, and SQL Database Creation, can be found on the following GitHub repository: [Airbnb Data Analysis and DB Storage](https://github.com/Adamb0lt/airbnb_data_analysis_and_DB_storage.git). This repository includes:
    - **Data Cleaning and Manipulation:** Clean up the dataset for proper use with analysis and machine learning.
    - **Exploratory Data Analysis (EDA):** Conduct EDA to gain insights into the dataset and visualize the relationships between various attributes.
    - **AB Testing:** Perform an AB test to determine if there is a significant difference in the distribution of prices between listings in Manhattan and Brooklyn.
    - **Machine Learning:** Create a machine learning model to predict room types for listings.
    - **SQL Database Creation:** Implement SQL database with schemas for clean and raw data, tables for data storage, and optimized querying with Index. Showcase database capabilities through various SQL queries.

    Feel free to explore and reach out if you have any questions or feedback!

    **Note:** The dataset used in this project is obtained from [Kaggle: NYC Airbnb Open Data](https://www.kaggle.com/dgomonov/new-york-city-airbnb-open-data).
    """)


elif section == 'Density of Listings per Borough':
    st.title('Density of Listings per Borough')
    st.write("""
    This visualization shows the density of Airbnb listings across the five boroughs of NYC. It helps to understand which areas have the highest concentration of listings.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717717158020' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Densityoflistingsperborough&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;Densityoflistingsperborough' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Densityoflistingsperborough&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717717158020');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width =900, height=675
    )

elif section == 'Average Number of Reviews per Neighborhood Group':
    st.title('Average Number of Reviews per Neighborhood Group')
    st.write("""
    This bar chart depicts the average number of reviews for listings in each borough of NYC.
    """)
    st.markdown('<div class="centered">', unsafe_allow_html=True)
    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717625634031' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717625634031');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width =900, height=650
    )
    st.markdown('</div>', unsafe_allow_html=True)

elif section == 'Average Price of Listings per Neighborhood Group':
    st.title('Average Price of Listings per Neighborhood Group')
    st.write("""
    This bar chart compares the average prices of Airbnb listings across the different boroughs of NYC.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717624063517' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717624063517');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width =900, height=650
    )

elif section == 'Number of Listings within each Manhattan Neighborhood':
    st.title('Number of Listings within each Manhattan Neighborhood')
    st.write("""
    This heatmap details the number of Airbnb listings in each neighborhood in Manhattan.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717626012585' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717626012585');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """,width =900, height=650
    )

elif section == 'Comparison of Average Listing Prices per Neighborhood in Manhattan':
    st.title('Comparison of Average Listing Prices per Neighborhood in Manhattan')
    st.write("""
    This bubble chart compares the average prices of Airbnb listings across different neighborhoods in Manhattan.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717625840566' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717625840566');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width =900, height=650
    )

elif section == 'Percentage of Different Room Types in Manhattan Listings':
    st.title('Percentage of Different Room Types in Manhattan Listings')
    st.write("""
    This pie chart shows the distribution of different room types in Manhattan's Airbnb listings.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717626091605' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717626091605');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width =900, height=650
    )
