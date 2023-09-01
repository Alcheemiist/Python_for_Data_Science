import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def plot_data(income_data: pd.DataFrame, life_expectancy_data: pd.DataFrame):

    # Extract 1900 data
    income_1900 = income_data[['country', '1900']]
    life_expectancy_1900 = life_expectancy_data[['country', '1900']]

    # Merge datasets based on country
    merged_data = pd.merge(income_1900, life_expectancy_1900, on='country', how='inner')

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(merged_data['1900_x'], merged_data['1900_y'], color='blue')
    plt.title('1900')
    plt.xlabel('Gross domestique product')
    plt.ylabel('Life Expectancy')
    plt.show()


def main():
    plot_data(load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv"), load("life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
