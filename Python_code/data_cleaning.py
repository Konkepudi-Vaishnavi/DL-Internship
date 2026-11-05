
import pandas as pd
import os

# Get the main project folder
base_path = os.path.dirname(os.path.dirname(__file__))

# Read the Excel dataset
file_path = os.path.join(
    base_path,
    "Dataset",
    "Dataset for Data Analytics.xlsx"
)

df = pd.read_excel(file_path)

print("Dataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("Duplicate records:", df.duplicated().sum())

df = df.drop_duplicates()

print("After removing duplicates:")
print(df.duplicated().sum())

# Check missing values
print("Missing Values:")
print(df.isnull().sum())


# Handle missing values
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')


# Verify missing values
print("Missing Values After Cleaning:")
print(df.isnull().sum())
