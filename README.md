# 🚢 Titanic Dataset Analysis

Welcome to the **Titanic Dataset Analysis** project! This project explores the famous Titanic dataset using **Python, Pandas, NumPy, Matplotlib, and Seaborn** to perform **data exploration and visualization**. 📊📉

## 📂 Dataset Files
- **train.csv** - Training dataset with labeled survival information
- **test.csv** - Test dataset without survival labels
- **gender_submission.csv** - Sample submission file

## 🔧 Libraries Used
- `pandas` 🐼 - Data manipulation and analysis
- `numpy` 🔢 - Numerical computing
- `matplotlib.pyplot` 📊 - Visualization library
- `seaborn` 🌊 - Statistical data visualization

## 🚀 Exploratory Data Analysis (EDA) Steps

### 1️⃣ Load Datasets
- Read the CSV files using **pandas**
- Display basic dataset info ✅

### 2️⃣ Check for Missing Values
- Identify missing values in the dataset ⚠️
- Visualize missing values using a **heatmap** 🟡

### 3️⃣ Summary Statistics
- Compute summary statistics for numerical columns 📋

### 4️⃣ Data Visualizations
- **Survival Distribution**: Count plot of survived vs. not survived passengers ⚰️🚶
- **Feature Distributions**:
  - Histograms for `Age` and `Fare` 📊
- **Correlation Heatmap**:
  - Identify correlations between features 🔥
- **Categorical Feature Analysis**:
  - Survival rates by `Pclass`, `Sex`, and `Embarked` 📌
- **Pairplot for Numerical Features**:
  - Visualize relationships between `Survived`, `Age`, `Fare`, and `Pclass` 🎭
- **Boxplots for Outlier Detection**:
  - Check outliers in `Age` and `Fare` 📦
- **Embarkation Port Analysis**:
  - Countplot of passengers by embarkation port ⛵

## 📸 Sample Visualizations
### 🔥 Correlation Heatmap
```python
plt.figure(figsize=(10, 6))
sns.heatmap(train_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Feature Correlation Heatmap')
plt.show()
```

### 📊 Survival Count by Class
```python
sns.countplot(x='Pclass', hue='Survived', data=train_df, palette='coolwarm')
plt.title('Survival Count by Passenger Class')
plt.show()
```

## 🏆 Results & Insights
- Women (`Sex: female`) had a higher survival rate than men 👩‍🚀
- Higher-class passengers (`Pclass: 1`) had a better chance of survival 🏅
- Passengers who paid higher fares (`Fare`) tended to survive more 💰
- Missing values in `Age` and `Embarked` need handling for further analysis ⚠️

## 📌 How to Run the Code
1. Install dependencies:
   ```sh
   pip install pandas numpy matplotlib seaborn
   ```
2. Run the Python script:
   ```sh
   python titanic_analysis.py
---
**Happy Analyzing! 🚀📊**

