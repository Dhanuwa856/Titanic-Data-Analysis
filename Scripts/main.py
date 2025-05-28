import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Data acquisition and testing
# File path
FILE_PATH = "../Data/titanic.csv"

# Create DataFrame
df = pd.read_csv(FILE_PATH)

# Show first 5 rows
print("Show first 5 rows:")
print(df.head())

# Data types and empty values
print("\nData info:")
print(df.info())

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

# 2. Data Cleaning

# Empty values
print('\nEmpty Values:')
print(df.isnull().sum())

# Fill in the blanks with the mean Age Column
df['Age'].fillna(df['Age'].mean())

# Removing unnecessary columns
df.drop(['Name'],axis=1,inplace=True)

# Converting categorical data to numerical
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

print('\nCleaned data:')
print(df.head())


# Lifesaving rates by class
survival_by_class = df.groupby('Pclass')['Survived'].mean()
plt.figure(figsize=(10,6))
plt.bar(survival_by_class.index, survival_by_class.values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.title("Lifesaving rates by class")
plt.xlabel('Class')
plt.ylabel("Lifesaving rates")
plt.xticks([1, 2, 3], labels=['1st', '2nd', '3rd'])
plt.grid(axis='y', linestyle='--')
plt.savefig('../Results/Lifesaving_rates_by_class.png')  # Save the figure
plt.close()

# Age distribution
plt.figure(figsize=(10,6))
plt.hist(df['Age'], bins=20, color='purple', edgecolor='black')
plt.title('Passengers Age distribution')
plt.xlabel('Age')
plt.ylabel('Passengers')
plt.grid(linestyle='--')
plt.savefig('../Results/Passengers_age_distribution.png')
plt.close()

# Fees and lifesaving
plt.figure(figsize=(10,6))
plt.scatter(df['Fare'], df['Age'], c=df['Survived'], cmap='coolwarm', alpha=0.6)
plt.colorbar(label='Survived (1) / Died (0)')
plt.title('Rescue by Fare and Age')
plt.xlabel('Fare')
plt.ylabel('Age')
plt.grid(True)
plt.savefig('../Results/Rescue_by_Fare_and_Age.png')
plt.close()


survival_by_sex = df.groupby('Sex')['Survived'].mean()
plt.figure(figsize=(10,4))
plt.bar(survival_by_sex.index, survival_by_sex.values, color=['blue','pink'])
plt.title("Lifesaving rates by sex")
plt.xlabel("sex")
plt.ylabel("Lifesaving rates")
plt.xticks([0,1], labels=['Male', 'Female'])
plt.grid(axis='y', linestyle='--')
plt.savefig('../Results/Lifesaving_rates_by_sex.png')
plt.close()

# Saving the cleaned data as CSV
df.to_csv('../data/cleaned_titanic_data.csv', index=False)
print("Cleaned data saved!")

