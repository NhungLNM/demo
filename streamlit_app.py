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
import os


# Read the Excel file
file_path = r"C:\Users\admin\OneDrive\文档\GitHub\Python\Athlete_events.xlsx"
try:
    athlete_events = pd.read_excel(file_path)
except FileNotFoundError as e:
    st.error(f"File not found error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")

# Display the data
st.write(athlete_events)
import streamlit as st
import pandas as pd

# Define the URL of the Excel file on GitHub
file_url = "https://github.com/kimduyenn/Python/raw/main/Athlete_events.xlsx"

# Read the Excel file
try:
    athlete_events = pd.read_excel(file_url)
except Exception as e:
    st.error(f"An error occurred while reading the Excel file: {e}")

# Display the data
st.write(athlete_events)
