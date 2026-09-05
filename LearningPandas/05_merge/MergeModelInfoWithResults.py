import pandas as pd
#1
df_model = pd.read_csv("models.csv")
df_result = pd.read_csv("results.csv")
#2
# print(df_model)
# print(df_result)

#3
# print(df_model.merge(df_result, on="model_id"))

#4
merged_df = df_model.merge(df_result, on="model_id")
# print(merged_df)

#5
# print(merged_df[["model_name", "accuracy"]])

#6
print(merged_df[
  merged_df["accuracy"] > 0.88]
  ["model_name"]
)

#7
print(merged_df.sort_values(by="accuracy", ascending=False))

#8
print(merged_df.groupby("model_type")["accuracy"].mean())

#9
