[![CI](https://github.com/nogibjj/Ailina_Aniwan_Mini_Project_2/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Ailina_Aniwan_Mini_Project_2/actions/workflows/cicd.yml)
# IDS706 - Mini Project 3 - Ailina Aniwan

## Alcohol Consumption Data Analysis

### Project Overview

This project analyzes global alcohol consumption using the **drinks.csv** dataset from [FiveThirtyEight](https://github.com/fivethirtyeight/data). It uses Python with **Polars** for statistical analysis and **Matplotlib** for data visualization to explore the consumption of beer, spirits, and wine across different countries.

### Data Source

The dataset is sourced from [FiveThirtyEight’s alcohol consumption dataset](https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv). It includes the following columns:
- **country**: The country name.
- **beer_servings**: Average beer servings per capita.
- **spirit_servings**: Average spirit servings per capita.
- **wine_servings**: Average wine servings per capita.
- **total_litres_of_pure_alcohol**: Total litres of pure alcohol consumed per capita.

### Analysis and Calculations

#### **1. Descriptive Statistics**
- **Mean**: The average number of servings.
- **Median**: The middle value in the data.
- **Standard Deviation**: The variability in servings across countries.

These statistics provide insights into the overall trends and distribution of alcohol consumption.

Here are the summarized statistics for each category:

- **Beer Servings**:
  - Mean: 106.16
  - Median: 76.00
  - Standard Deviation: 101.14
- **Spirit Servings**:
  - Mean: 80.99
  - Median: 56.00
  - Standard Deviation: 88.28
- **Wine Servings**:
  - Mean: 49.45
  - Median: 8.00
  - Standard Deviation: 79.70
- **Total Litres of Pure Alcohol**:
  - Mean: 4.70
  - Median: 4.20
  - Standard Deviation: 3.77

These results were calculated using Polars and represent the central tendency and dispersion measures for alcohol consumption metrics by beverage type across various countries.

#### **2. Data Visualization**

**grouped bar chart** was created to compare the mean, median, and standard deviation for beer, spirits, and wine. This visualization helps identify the central tendencies and spread of alcohol consumption across different categories.

![Data Visualiztion](figure.png)

According to the chart:

- **Beer Servings**: Beer has the highest mean and median servings, with relatively low variability (standard deviation).
- **Spirit Servings**: Spirits show high variability, as the standard deviation is almost equal to the mean, indicating greater inconsistency in consumption across countries.
- **Wine Servings**: Wine has the lowest mean and median, but a relatively large standard deviation, indicating that while average consumption is low, there are significant outliers.


