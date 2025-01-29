import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
train_path = './train.csv'
test_path = './test.csv'
gender_submission_path = './gender_submission.csv'

train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)
gender_submission_df = pd.read_csv(gender_submission_path)

# Display basic information
print("Train Dataset Info:")
print(train_df.info())
print("\nTest Dataset Info:")
print(test_df.info())

# Check for missing values
print("\nMissing Values in Train Dataset:")
print(train_df.isnull().sum())
print("\nMissing Values in Test Dataset:")
print(test_df.isnull().sum())

# Summary statistics
print("\nTrain Dataset Summary Statistics:")
print(train_df.describe())

# Visualizing missing values
plt.figure(figsize=(10, 5))
sns.heatmap(train_df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
plt.title('Missing Values in Train Dataset')
plt.show()

# Target variable distribution
sns.countplot(x='Survived', data=train_df, palette='coolwarm')
plt.title('Survival Count')
plt.show()

# Feature distributions
num_features = ['Age', 'Fare']
for feature in num_features:
    plt.figure(figsize=(6, 4))
    sns.histplot(train_df[feature], bins=30, kde=True, color='blue')
    plt.title(f'Distribution of {feature}')
    plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(train_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()

# Relationship between categorical features and survival
categorical_features = ['Pclass', 'Sex', 'Embarked']
for feature in categorical_features:
    plt.figure(figsize=(6, 4))
    sns.countplot(x=feature, hue='Survived', data=train_df, palette='coolwarm')
    plt.title(f'Survival Count by {feature}')
    plt.show()

# Pairplot for numerical features
sns.pairplot(train_df[['Survived', 'Age', 'Fare', 'Pclass']], hue='Survived', palette='coolwarm')
plt.show()

# Boxplot for outlier detection
for feature in num_features:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=train_df[feature], color='red')
    plt.title(f'Boxplot of {feature}')
    plt.show()

# Countplot for Embarked feature
sns.countplot(x='Embarked', data=train_df, palette='coolwarm')
plt.title('Passenger Count by Embarkation Port')
plt.show()
