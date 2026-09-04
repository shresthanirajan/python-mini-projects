import pandas as pd 
#1
df = pd.read_csv("customer_data.csv")
#2
print(df.head())
#3
print(df.isna().sum())
#4
print(df[
  df["age"].isna()
])
#5
print(df[
  df["income"].isna()
])
#6
df["age"] = df["age"].fillna(df["age"].mean())
#7
df["income"] = df["income"].fillna(df["income"].mean())

#8 Cleaned DataFrame
print(df)

#9 - Average Income After Cleaning
print(df["income"].mean())

#10
print(df[
  df["city"] == "Austin"
])
