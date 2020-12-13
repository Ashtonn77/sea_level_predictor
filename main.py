import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  df = pd.read_csv('epa-sea-level.csv')
  x_1 = df['Year']
  y_1 = df['CSIRO Adjusted Sea Level']

  plt.scatter(x_1, y_1)

  x = pd.Series([int(i) for i in range(1880, 2050)])
  slope, intercept, r_value, p_value, stderr = linregress(x_1, y_1)
  plt.plot(x, intercept + x * slope, color="blue")


  year_2000_df = df[df["Year"] >= 2000]
  slope, intercept, r_value, p_value, stderr = linregress(year_2000_df["Year"], year_2000_df["CSIRO Adjusted Sea Level"])
  x = pd.Series([int(i) for i in range(2000, 2050)])
  plt.plot(x, intercept + x * slope, color="red")


  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")

    
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()