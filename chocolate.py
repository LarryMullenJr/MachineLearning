import pandas as pd

#Load the dataset
df = pd.read_csv('/Users/mattdumouchel/Downloads/flavors_of_cacao.csv')

#Display the first few rows of the dataset
df.head()

#Check for missing values
print(df.isnull().sum())

#Drop rows with missing values
df = df.dropna()

#Confirm the rows with missing values are dropped
print(df.isnull().sum())

#Count of the tuples in the dataset
print("Number of tuples:", len(df))

#Count of unique company names
unique_companies = df["Company (Maker-if known)"].nunique()
print("Number of unique company names:", unique_companies)

#Count of reviews in 2013
reviews_2013 = df[df['Review Date'] == 2013].shape[0]
print("Number of reviews in 2013:", reviews_2013)

#Count of missing values in the BeanType column
missing_beantype = df['Bean Type'].isnull().sum()
print("Number of missing values in Bean Type:", missing_beantype)

#Histogram of ratings
import matplotlib.pyplot as plt

# Plot histogram of ratings
plt.hist(df['Rating'], bins=20, edgecolor='black')
plt.title('Histogram of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()

#Scatter plot of Cocoa Percent vs Rating
df['Cocoa Percent'] = df['Cocoa Percent'].str.replace('%', '').astype(float)

# Plot scatter plot
plt.scatter(df['Cocoa Percent'], df['Rating'], alpha=0.1)
plt.title('Cocoa Percent vs Rating')
plt.xlabel('Cocoa Percent')
plt.ylabel('Rating')
plt.show()

#Normalize the ratings column
from sklearn.preprocessing import MinMaxScaler

# Normalize the ratings
scaler = MinMaxScaler()
df['Normalized Ratings'] = scaler.fit_transform(df[['Rating']])

# Display the normalized ratings
print(df[['Rating', 'Normalized Ratings']].head())

#Encode the company names and locations
from sklearn.preprocessing import LabelEncoder

# Encode the company names
label_encoder = LabelEncoder()
df['Company_encoded'] = label_encoder.fit_transform(df['Company (Maker-if known)'])

# Display the encoded company names
print(df[['Company (Maker-if known)', 'Company_encoded']].head())

