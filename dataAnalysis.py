# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a theme for seaborn
sns.set_theme()

# Task 1: Load and Explore the Dataset
try:
    # Load dataset
    file_path = "monthsales.csv"  # Replace with your dataset path
    df = pd.read_csv(file_path)
    
    # Display the first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Check structure and missing values
    print("\nDataset Info:")
    df.info()
    
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # Clean missing values (example: fill with mean or drop rows with NaN)
    df.fillna(df.mean(numeric_only=True), inplace=True)
    print("\nMissing values handled.")
except FileNotFoundError:
    print("Error: The specified file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# Task 2: Basic Data Analysis
try:
    # Compute basic statistics
    print("\nBasic Statistics:")
    print(df.describe())

    # Perform groupings
    if 'Category' in df.columns:  # Replace 'Category' with a categorical column name
        group_mean = df.groupby('Category').mean()
        print("\nMean values for each group:")
        print(group_mean)

        # Example finding: mean of a specific column per category
        if 'NumericalColumn' in df.columns:  # Replace 'NumericalColumn' with a numerical column name
            print("\nMean of NumericalColumn per Category:")
            print(group_mean['NumericalColumn'])
except Exception as e:
    print(f"An error occurred during analysis: {e}")

# Task 3: Data Visualization
try:
    # Line chart (replace 'TimeColumn' and 'ValueColumn' with appropriate column names)
    if 'TimeColumn' in df.columns and 'ValueColumn' in df.columns:
        plt.figure(figsize=(10, 6))
        plt.plot(df['TimeColumn'], df['ValueColumn'], marker='o')
        plt.title('Trend Over Time')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.grid(True)
        plt.show()

    # Bar chart
    if 'Category' in df.columns and 'NumericalColumn' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Category', y='NumericalColumn', data=df)
        plt.title('Average NumericalColumn per Category')
        plt.xlabel('Category')
        plt.ylabel('Average Value')
        plt.show()

    # Histogram
    if 'NumericalColumn' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df['NumericalColumn'], kde=True, bins=30)
        plt.title('Distribution of NumericalColumn')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.show()

    # Scatter plot
    if 'NumericalColumn1' in df.columns and 'NumericalColumn2' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='NumericalColumn1', y='NumericalColumn2', data=df)
        plt.title('Scatter Plot of NumericalColumn1 vs NumericalColumn2')
        plt.xlabel('NumericalColumn1')
        plt.ylabel('NumericalColumn2')
        plt.show()
except Exception as e:
    print(f"An error occurred during visualization: {e}")
