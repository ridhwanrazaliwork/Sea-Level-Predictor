import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df["CSIRO Adjusted Sea Level"]
    x = df["Year"]


    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    rs = linregress(x, y)
    x1 = pd.Series([i for i in range (1880, 2051)])
    y1 = rs.slope*x1 + rs.intercept
    plt.plot(x1, y1, "r")

    # Create second line of best fit
    df1 = df.loc[df['Year'] >= 2000]
    dfx = df1['Year']
    dfy = df1['CSIRO Adjusted Sea Level']
    rs2 = linregress(dfx, dfy)
    x2 = pd.Series([i for i in range (2000, 2051)])
    y2 = rs2.slope*x2 + rs2.intercept
    plt.plot(x2, y2, "blue")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()