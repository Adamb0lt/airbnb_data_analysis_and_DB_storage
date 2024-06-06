import streamlit as st
import streamlit.components.v1 as components

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
    st.title('NYC Airbnb Dataset Analysis and AB Testing Project')
    st.subheader('Visualizations Overview')

    st.write("""
    Welcome to the NYC Airbnb Dataset Analysis and AB Testing Project! This project involves analyzing the 2019 NYC Airbnb dataset to uncover insights and patterns in the data, conduct an AB test, and create predictive models. Visualizations play a crucial role in this project, helping to present findings and insights in an easily understandable manner.

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

elif section == 'Density of Listings per Borough':
    st.title('Density of Listings per Borough')
    st.write("""
    This visualization shows the density of Airbnb listings across the five boroughs of NYC. It helps to understand which areas have the highest concentration of listings.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717625554744' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Densityoflistingsperborough&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;Densityoflistingsperborough' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Densityoflistingsperborough&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717625554744');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, height=600
    )

elif section == 'Average Number of Reviews per Neighborhood Group':
    st.title('Average Number of Reviews per Neighborhood Group')
    st.write("""
    This bar chart depicts the average number of reviews for listings in each borough of NYC.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717625634031' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;Avgnumberofreviewsperneighborhoodgroup&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717625634031');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, height=600
    )

elif section == 'Average Price of Listings per Neighborhood Group':
    st.title('Average Price of Listings per Neighborhood Group')
    st.write("""
    This bar chart compares the average prices of Airbnb listings across the different boroughs of NYC.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717624063517' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;AvgPriceperneighborhoodgroup&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717624063517');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, height=600
    )

elif section == 'Number of Listings within each Manhattan Neighborhood':
    st.title('Number of Listings within each Manhattan Neighborhood')
    st.write("""
    This heatmap details the number of Airbnb listings in each neighborhood in Manhattan.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717626012585' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;NumberoflistingswithineachManhattanneighborhood&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717626012585');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, height=600
    )

elif section == 'Comparison of Average Listing Prices per Neighborhood in Manhattan':
    st.title('Comparison of Average Listing Prices per Neighborhood in Manhattan')
    st.write("""
    This bubble chart compares the average prices of Airbnb listings across different neighborhoods in Manhattan.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717625840566' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;ComparisonsofavglistingpricesperneighborhoodinManhattan&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717625840566');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, width= 800, height=600
    )

elif section == 'Percentage of Different Room Types in Manhattan Listings':
    st.title('Percentage of Different Room Types in Manhattan Listings')
    st.write("""
    This pie chart shows the distribution of different room types in Manhattan's Airbnb listings.
    """)

    components.html(
        """
        <div class='tableauPlaceholder' id='viz1717626091605' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;20&#47;2019NYCAirbnbDataViz&#47;PercentageofdifferentroomtypesinallManhattanListings&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1717626091605');                    var vizElement = divElement.getElementsByTagName('object')[0];                    vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';                    var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>
        """, height=600
    )
