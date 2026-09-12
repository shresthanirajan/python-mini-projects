import pandas as pd

#1
df_models = pd.read_csv("AIExperimentPerformancePipeline/models.csv")
df_results = pd.read_csv("AIExperimentPerformancePipeline/experiment_results.csv")

#2
print(df_models.head())
print(df_results.head())

#3
print(df_results.duplicated().sum())

#4
df_results = df_results.drop_duplicates()
print(df_results)

#5
df_results["accuracy"] = df_results["accuracy"].fillna(
  df_results["accuracy"].mean()
)

#6
df_merged = pd.merge(df_models, df_results, on="model_id")
print(df_merged)

#7

df_merged = pd.merge(df_results, df_models, on="model_id", how="left")
print(df_merged["model_name".isna()])
print(df_merged["model_name".isna()])






