import pandas as pd

#1
df = pd.read_csv("07_Specific_Experiment_Data/experiment_selection.csv")
#2
print(df)

#3
print(df.loc[2])

#4
print(df.iloc[0])

#5
print(df.loc[1:3])

#6
print(df.iloc[0:3])

#7
print(df.loc[
         1:3
      , ["model", "accuracy"]
      ]
)

#8

print(df.iloc[
  0:3, 0:1
])
