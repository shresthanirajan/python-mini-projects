import pandas as pd

#1
df = pd.read_csv("08_CleanandExportModelData/model_cleanup.csv")
#2
print(df)
#3 Rename
df = df.rename(columns={
  "acc": "accuracy",
  "train_time": "training_time"
})

#4
df = df.drop(columns=["notes"])
print(df)
#5
df["accuracy_percent"] = df["accuracy"] * 100

#6
df = df.sort_values("accuracy", ascending=False)
print(df)

#7
df.to_csv("cleaned_model_data.csv", index=False)