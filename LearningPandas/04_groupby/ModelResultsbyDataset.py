import pandas as pd

#1
df = pd.read_csv("experiment_results.csv")

#2
print(df.head())

#3
print(df.groupby("dataset")["accuracy"].mean())

# #4
print(df.groupby("dataset")["training_time"].mean())

# #5
print(df.groupby("dataset")["accuracy"].max())

# #6
print(df.groupby("dataset")["model"].count())

#7
print(df[df["dataset"] == "Dataset_B"])

#8
print(df.sort_values(by="accuracy", ascending=False))

#9
print(df[["model", "dataset", "accuracy"]])

#10
print(df[
  df["training_time"] < 30
]["accuracy"].mean())