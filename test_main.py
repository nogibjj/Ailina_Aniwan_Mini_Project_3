import pandas as pd
from main import process_mean, process_median, process_std

def test_statistics():
    data = {
        'beer_servings': [50, 60, 70],
        'spirit_servings': [80, 90, 100],
        'wine_servings': [20, 30, 40]
    }
    df = pd.DataFrame(data)

    print("Testing 'beer_servings' statistics...")
    expected_mean_beer = 60
    expected_median_beer = 60
    expected_std_beer = 10
    print(f"Expected mean: {expected_mean_beer:.2f}, "
          f"Calculated mean: {process_mean(df, 'beer_servings'):.2f}")
    print(f"Expected median: {expected_median_beer:.2f}, "
          f"Calculated median: {process_median(df, 'beer_servings'):.2f}")
    print(f"Expected standard deviation: {expected_std_beer:.2f}, "
          f"Calculated standard deviation: {process_std(df, 'beer_servings'):.2f}")
    print()

    print("Testing 'spirit_servings' statistics...")
    expected_mean_spirit = 90
    expected_median_spirit = 90
    expected_std_spirit = 10
    print(f"Expected mean: {expected_mean_spirit:.2f}, "
          f"Calculated mean: {process_mean(df, 'spirit_servings'):.2f}")
    print(f"Expected median: {expected_median_spirit:.2f}, "
          f"Calculated median: {process_median(df, 'spirit_servings'):.2f}")
    print(f"Expected standard deviation: {expected_std_spirit:.2f}, "
          f"Calculated standard deviation: {process_std(df, 'spirit_servings'):.2f}")
    print()

    print("Testing 'wine_servings' statistics...")
    expected_mean_wine = 30
    expected_median_wine = 30
    expected_std_wine = 10
    print(f"Expected mean: {expected_mean_wine:.2f}, "
          f"Calculated mean: {process_mean(df, 'wine_servings'):.2f}")
    print(f"Expected median: {expected_median_wine:.2f}, "
          f"Calculated median: {process_median(df, 'wine_servings'):.2f}")
    print(f"Expected standard deviation: {expected_std_wine:.2f}, "
          f"Calculated standard deviation: {process_std(df, 'wine_servings'):.2f}")

if __name__ == "__main__":
    test_statistics()
