import pandas as pd
import os

# read the csv files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all three files
df = pd.concat([df0, df1, df2], ignore_index=True)

# keep only pink morsel
df = df[df["product"] == "pink morsel"]

# count sales
df["price"] = df["price"].str.replace("$", "", regex=False)
df["price"] = pd.to_numeric(df["price"])
df["sales"] = df["quantity"] * df["price"]

# required fields
df =df[["sales", "date", "region"]]

os.makedirs("output", exist_ok=True)
df.to_csv("output/formatted_sales_data.csv", index=False)


print("Data Processing completed successfully. ")
print(df.head())
print(f"Total Rows : {len(df)}")

