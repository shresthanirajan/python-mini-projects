import pandas as pd
#1
df_models = pd.read_csv("06_left_merge_missing_matches/models.csv")
#2
df_result = pd.read_csv("06_left_merge_missing_matches/result.csv")

#3 #4 
print(df_models.merge(df_result, on="model_id"))

#5
left_merge = (df_models.merge(df_result, on="model_id", how="left"))

#6
print(left_merge[
  left_merge["accuracy"].isna()
])