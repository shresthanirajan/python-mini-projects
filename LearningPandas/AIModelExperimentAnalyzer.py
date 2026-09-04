import pandas as pd
#1
df = pd.read_csv("model_results.csv")
#2
print(df)

#3
print(df.head())

# #4
print(df[["model", "accuracy"]])

# #5
# print(df["accuracy"].mean())
# #6
# print(df["accuracy"].max())
# #7
# print(df[df["accuracy"] > 0.85]
#       [["model"]])
# #8
# print(df[df["training_time"] < 30]
#       ["model"])
# #9
# print(df.sort_values(by="accuracy", ascending=False))

# #10
# df["accuracy_percent"] = df["accuracy"] * 100
print(df["accuracy"] > 0.70)

