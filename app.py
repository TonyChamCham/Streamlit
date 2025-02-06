#import
import os
import pandas as pd
import plotly.express as px
import streamlit as st


st.title("Vizualisation of CO2 Most Emitting Countries")
st.header("Part 1: Bar graph vizualisation")
st.write("In this section, we will vizualise where in the World are located the most emitting countries along the years (1960~2011)")
# st.markdown("*Further resources [here](https://altair-viz.github.io/gallery/selection_histogram.html)*")

st.write("Please define the dates range for the analysis...")
slider = st.slider("Years of CO2 production", 1960, 2011, (1985, 2000))
start_year, end_year = slider
st.write("...and the number of countries you would like to display.")
num_field = st.radio("Number of displayed countries", [1, 3, 5, 10, 25, 50, 100])

# Load dataset
filepath = os.path.join('input', 'CO2_per_capita.csv')
df = pd.read_csv(filepath, sep=';')

# Function to find top n countries producing CO2
def top_n_emitters(df, start_year=2008, end_year=2011, nb_displayed=10):
    """
    Function to filter dataframe per years range
    """
    #years filter
    timeframed_df = df[(df['Year'] > start_year) & (df['Year'] < end_year)]
    #do the mean for each country
    top_emitters = timeframed_df.groupby('Country Name')['CO2 Per Capita (metric tons)'].mean().sort_values(ascending=False)
    print(top_emitters)
    #sort the values and keep nb_displayed
    top_emitters_n = top_emitters.head(nb_displayed).reset_index()
    #create the fig
    fig = px.bar(top_emitters_n, x='Country Name', y='CO2 Per Capita (metric tons)')
    #return the fig
    return fig.show()
    

st.write("Create the plot!")
# Bar plot creation
top_n_emitters(df, start_year=start_year, end_year=end_year, nb_displayed=num_field)