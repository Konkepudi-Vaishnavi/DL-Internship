
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


# Check duplicate records

print("\nTotal Duplicate Rows:")
print(df.duplicated().sum())

# Check duplicate Order IDs

print("\nDuplicate Order IDs:")
print(df["OrderID"].duplicated().sum())



# Step 3: Date Format Correction

# Convert Date column into datetime format

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

# Display date column information

print("\nDate Column Information:")
print(df["Date"].dtype)

# Check invalid or missing dates

print("\nInvalid Dates:")
print(df["Date"].isnull().sum())

# Display first 10 dates

print("\nFirst 10 Dates:")
print(df["Date"].head(10))


# Step 4: Numerical Data Validation

# Check numerical column information

print("\nNumerical Column Information:")
print(df[["Quantity", "UnitPrice",
          "ItemsInCart", "TotalPrice"]].info())

# Check statistical summary

print("\nNumerical Data Summary:")
print(df[["Quantity", "UnitPrice",
          "ItemsInCart", "TotalPrice"]].describe())

# Check negative values

print("\nNegative Values:")
print((df[["Quantity", "UnitPrice",
           "ItemsInCart", "TotalPrice"]] < 0).sum())

# Verify TotalPrice calculation

df["CalculatedPrice"] = df["Quantity"] * df["UnitPrice"]

print("\nTotalPrice Validation:")
print((df["TotalPrice"] == df["CalculatedPrice"]).sum())

print("\nIncorrect TotalPrice Records:")
print((df["TotalPrice"] != df["CalculatedPrice"]).sum())


# Validate TotalPrice

calculated_price = (
    df["Quantity"] * df["UnitPrice"]
).round(2)

actual_price = df["TotalPrice"].round(2)

correct_records = (actual_price == calculated_price).sum()
incorrect_records = (actual_price != calculated_price).sum()

print("\nTotalPrice Validation:")
print("Correct Records:", correct_records)
print("Incorrect Records:", incorrect_records)

if incorrect_records == 0:
    print("All TotalPrice records are correct!")



import os

project_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

output_folder = os.path.join(
    project_folder,
    "Cleaned_Data"
)

os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder,
    "cleaned_dataset.xlsx"
)

df.to_excel(output_path, index=False)

print("\nCleaned dataset exported successfully!")
print("Saved location:", output_path)
