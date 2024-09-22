import pandas as pd
import matplotlib.pyplot as plt

dataset = "https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv"

def load_dataset():
    df = pd.read_csv(dataset)
    return df

def process_mean(df, col):
    return df[col].mean()

def process_median(df, col):
    return df[col].median()

def process_std(df, col):
    return df[col].std()

def plot_summary_statistics(df):
    columns = ['beer_servings', 'spirit_servings', 'wine_servings']
    mean_values = df[columns].mean()
    median_values = df[columns].median()
    std_dev_values = df[columns].std()

    bar_width = 0.3
    bar_positions = range(len(columns))

    plt.bar(bar_positions, mean_values, width=bar_width, label='Mean')
    plt.bar([p + bar_width for p in bar_positions], median_values, width=bar_width, label='Median')
    plt.bar([p + 2 * bar_width for p in bar_positions], std_dev_values, width=bar_width, label='Standard Deviation')
    plt.title('Comparison of Alcohol Servings by Type')
    plt.ylabel('Servings')
    plt.xlabel('Alcohol Type')
    plt.xticks([p + bar_width for p in bar_positions], columns)
    plt.legend()
    plt.show()

def main():
    df = load_dataset() 
    columns = ['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    
    for col in columns:
        print(f"Column: {col}")
        print(f"Mean: {process_mean(df, col):.2f}")
        print(f"Median: {process_median(df, col):.2f}")
        print(f"Standard Deviation: {process_std(df, col):.2f}")
        print()
    
    plot_summary_statistics(df)
        
if __name__ == "__main__":
    main()