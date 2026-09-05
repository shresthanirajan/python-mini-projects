import pandas as pd
#1
df = pd.read_csv("training_records.csv")

#2
print(df.head())

#3
print(df.duplicated().sum())

#4
print(df[df.duplicated()])

#5
df = df.drop_duplicates()
print(df)

#6
print(df["dataset"].value_counts())

#7
print(df["model"].value_counts())

# #8
print(df.sort_values(by="accuracy", ascending=False))

# #9. 
print(df.sort_values(by="accuracy", ascending=False)[["model", "accuracy"]])

#10
print(df[
  df["accuracy"] > 0.85]
  [["model"]]
)
