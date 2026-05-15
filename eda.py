# Importing libraries
import pandas as pd               # Used for data analysis and handling tables
import seaborn as sns             # Used for creating attractive graphs
import matplotlib.pyplot as plt   # Used for plotting graphs


# Loading the Netflix dataset
df = pd.read_csv("netflix_titles.csv")    # pd.read_csv() reads the CSV file and stores the data inside 'df'

# Displaying first 5 rows of dataset
print("FIRST 5 ROWS OF DATASET")
print(df.head())     # head() shows first 5 records, helps us understand dataset structure

# Checking dataset shape
print("\nDATASET SHAPE")
print(df.shape)      # shape returns :(number of rows, number of columns)

# Checking missing values
print("\nMISSING VALUES")
print(df.isnull().sum())   # isnull() checks empty values, sum() counts total missing values in each column


# Counting Movies and TV Shows
print("\nMOVIES VS TV SHOWS")
print(df['type'].value_counts())    # value_counts() counts categories in 'type' column

# Displaying column names
print("\nCOLUMN NAMES")
print(df.columns)          # columns shows all dataset column names

# Checking data types of columns
print("\nDATA TYPES")
print(df.dtypes)           # dtypes shows whether data is text (object) or numerical (int64) 

# Displaying full dataset information
print("\nDATASET INFORMATION")
print(df.info())         # info() gives: total rows, non-null values ,memory usage ,data types

# Creating graph for Movies vs TV Shows
sns.countplot(x='type', data=df)     # countplot() creates bar graph, x='type' uses type column

# Adding graph title
plt.title("Movies vs TV Shows on Netflix")
# Displaying graph
plt.show()


# Creating histogram for release year trend
plt.figure(figsize=(12,6))    # figure(figsize) changes graph size

sns.histplot(df['release_year'], bins=30)   # histplot() creates histogram, bins=30 divides data into groups

# Adding graph title
plt.title("Netflix Content Release Trend")

# Displaying graph
plt.show()


# Top 10 countries producing Netflix content
top_countries = df['country'].value_counts().head(10)  # value_counts() counts country frequency, head(10) selects top 10 countries

# Creating bar graph for top countries
plt.figure(figsize=(12,6))
sns.barplot(                    # Creates a horizontal bar graph
    x=top_countries.values,     # x-axis -counts
    y=top_countries.index       # y-axis- country names
)

# Adding graph title
plt.title("Top 10 Countries Producing Netflix Content")
# Displaying graph
plt.show()