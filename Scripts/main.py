import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Data acquisition and initial exploration
# File path
FILE_PATH = "../Data/titanic.csv"

# Create DataFrame
df = pd.read_csv(FILE_PATH)

# Show first 5 rows
print("Show first 5 rows:")
print(df.head())

# Data types and missing values
print("\nData info:")
print(df.info())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# 2. Data Cleaning

# Handling missing values
print('\nMissing Values:')
print(df.isnull().sum())

# Fill missing values in the 'Age' column with the mean
df['Age'].fillna(df['Age'].mean(), inplace=True)  # Added inplace=True to reflect changes in the DataFrame

# Dropping unnecessary columns
df.drop(['Name'], axis=1, inplace=True)

# Converting categorical data (e.g., 'Sex') to numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print('\nCleaned data:')
print(df.head())

# Visualizations

# Survival rates by class
survival_by_class = df.groupby('Pclass')['Survived'].mean()
plt.figure(figsize=(10, 6))
plt.bar(survival_by_class.index, survival_by_class.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Survival Rates by Class")
plt.xlabel('Class')
plt.ylabel("Survival Rate")
plt.xticks([1, 2, 3], labels=['1st', '2nd', '3rd'])
plt.grid(axis='y', linestyle='--')
plt.savefig('../Results/Survival_Rates_by_Class.png')  # Save the figure
plt.close()

# Age distribution
plt.figure(figsize=(10, 6))
plt.hist(df['Age'], bins=20, color='purple', edgecolor='black')
plt.title('Passengers Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.grid(linestyle='--')
plt.savefig('../Results/Passengers_Age_Distribution.png')
plt.close()

# Fare vs. Age by Survival
plt.figure(figsize=(10, 6))
plt.scatter(df['Fare'], df['Age'], c=df['Survived'], cmap='coolwarm', alpha=0.6)
plt.colorbar(label='Survived (1) / Died (0)')
plt.title('Survival by Fare and Age')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.grid(True)
plt.savefig('../Results/Survival_by_Fare_and_Age.png')
plt.close()

# Survival rates by sex
survival_by_sex = df.groupby('Sex')['Survived'].mean()
plt.figure(figsize=(10, 4))
plt.bar(survival_by_sex.index, survival_by_sex.values, color=['blue', 'pink'])
plt.title("Survival Rates by Sex")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.xticks([0, 1], labels=['Male', 'Female'])
plt.grid(axis='y', linestyle='--')
plt.savefig('../Results/Survival_Rates_by_Sex.png')
plt.close()

# Saving the cleaned data as CSV
df.to_csv('../Data/cleaned_titanic_data.csv', index=False)
print("Cleaned data saved!")
