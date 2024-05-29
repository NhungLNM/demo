from collections import defaultdict
from pathlib import Path
import sqlite3
import altair as alt
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import numpy as np
import geopandas as gpd
from matplotlib.colors import LinearSegmentedColormap
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import plotly.express as px
import streamlit as st
import pandas as pd
import os
"C:\Users\USER\Documents\athlete_events.xlsx"
# Print current working directory
print("Current Working Directory:", os.getcwd())

# List files in the specified directory
print("Files in Directory:", os.listdir('/mount/src/demo/'))

# Define the path to the Excel file
file_path = '/mount/src/Documents/athlete_events.xlsx'

# Check if the file exists and read it
if os.path.exists(file_path):
    athlete_events = pd.read_excel(file_path)
    print("File read successfully.")
else:
    print(f"File not found: {file_path}")

athlete_events = pd.read_excel(r'C:\Users\USER\Documents\athlete_events.xlsx')



# PLOT 1

selected_sports = ["Athletics", "Badminton", "Boxing", "Cycling", "Gymnastics", "Swimming"]
my_data = athlete_events[(athlete_events['Year'] == 2016) & (athlete_events['Sport'].isin(selected_sports))]

sport_counts = my_data['Sport'].value_counts(normalize=True) * 100

fig = px.pie(values=sport_counts, names=sport_counts.index, title='Distribution of Athletes in Selected Sports (2016)', hole=0.1)
fig.update_traces(textposition='inside', textinfo='percent+label')

st.plotly_chart(fig)
