import pandas as pd

df_models = pd.read_csv("AIExperimentPerformancePipeline/models.csv")
df_results = pd.read_csv("AIExperimentPerformancePipeline/experiment_results.csv")
# print(df_models)

df_models = pd.read_csv("AIExperimentPerformancePipeline/models.csv")
df_results = pd.read_csv("AIExperimentPerformancePipeline/experiment_results.csv")
print(df_models)

print(df_results)

print(df_results.duplicated().sum())

df_models = pd.read_csv("AIExperimentPerformancePipeline/models.csv")
df_results = pd.read_csv("AIExperimentPerformancePipeline/experiment_results.csv")

