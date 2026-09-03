import pandas as pd
data = {"Model": ["Logistic Regession", "Random Forest", "Decision Tree", "KNN"], "accuracy": [0.84, 0.91, 0.79, 0.86],
        "training_time": [12, 35, 8, 15]}
new_data = {"Model": ["Claude", "Gemeni", "GPT4", "GPT5", "Antropics"],
            "Accuracy": [0.90, 0.30, None , 0.67, 0.85],
            "training_time": [3, 15, 30, None, 5]

}
data_set = pd.DataFrame(data)
new_df = pd.DataFrame(new_data)

# print(data_set)

# print(data_set["accuracy"])

# print(data_set[["Model", "accuracy"]])

# print(data_set["accuracy"] > 0.85)

# print(data_set["training_time"] < 20)

# print(data_set[
#   data_set["training_time"] < 20]
#   [["Model", "accuracy"]]
# )

# print(data_set[
#   (data_set["accuracy"] > 0.85) & (data_set["training_time"] < 20)
# ])

# print(data_set[
#   data_set["accuracy"] > 0.85
# ]
# [

#   ["Model", "accuracy"]
# ]
# )

# #1
# print(data_set[
#   data_set["training_time"] <= 15
# ]

#   [
#     ["Model"]
#   ]
# )

# #2
# print(data_set[
#   data_set["accuracy"] < 0.90
# ]
# [
#   ["Model", "training_time"]
# ]
# )
# #3 
# print(data_set[
#   (data_set["accuracy"] >= 0.80) & (data_set["training_time"] < 15)
# ]
# [["Model"]]
# )

# #4
# print(data_set[
#   (data_set["accuracy"] > 0.90) | (data_set["training_time"] <= 8)
# ]
# [["Model"]])

# #5
# print(data_set[
#   data_set["training_time"] > 10 
# ]
# [["Model"]])

# print(data_set[
#   (data_set["accuracy"] >= 0.80) & (data_set["accuracy"] <= 0.90)
# ])

# print(data_set[
#   data_set["training_time"] < 20

# ]
# [["Model", "accuracy"]])

# print(data_set[
#   (data_set["accuracy"] >= 0.8) & (data_set["training_time"] <= 15)
# ]
# [["Model"]])

#Adding and Updating

# print(data_set)


# data_set["accuracy_percent"] = data_set["accuracy"] * 100

# data_set["training_time"] = data_set["training_time"] * 2

# data_set["efficient"] = (data_set["accuracy"] > 0.85) & (data_set["training_time"] < 40)

# data_set["accuracy_gap"] = 1- data_set["accuracy"]

# data_set["fast_model"] = data_set["training_time"] <= 30

# print(
# data_set[
#   data_set["fast_model"] == True
# ]
# [["Model", "training_time", "fast_model"]]
# )

# data_set["slow_model"] = data_set["training_time"] > 30
# print(data_set[
#   data_set["slow_model"] == True
# ]
# [["Model", "training_time"]])

data_set["performance_score"] = data_set["accuracy"] * 100 - data_set["training_time"]

# print(data_set[
#   data_set["performance_score"] > 60
# ]
# [["Model"]])
               
#print(data_set)

# print(data_set[
#   (data_set["accuracy"] >= 0.85) & (data_set["performance_score"] > 50)
# ]
# [["Model", "accuracy", "performance_score"]])

# print(data_set.sort_values(by="accuracy", ascending=False))

# print(data_set.sort_values(by="training_time") [["Model", "training_time"]])

# print(data_set.sort_values(by="accuracy", ascending=False)[["Model", "accuracy"]])

# print(data_set[
#   data_set["accuracy"] >= 0.85
# ].sort_values(by="performance_score", ascending=False)
# [["Model"]])


# print(data_set[
#   data_set["training_time"] < 40
# ].sort_values(by="training_time")
# [["Model", "training_time"]])


# print(data_set["accuracy"].mean())
# print(data_set["accuracy"].max())

# print(data_set["training_time"].min())
# print(data_set["training_time"].sum())
# print(data_set["Model"].count())

# print(data_set[
#   data_set["accuracy"] > 0.85
# ]["training_time"].mean()
# )

# print(data_set[
#   data_set["training_time"] < 40
# ]["performance_score"].max())


# print(data_set[
#   data_set["performance_score"] > 50
# ]["accuracy"].mean())

# print(data_set[
#   data_set["accuracy"] < 0.90
# ]["training_time"].max())

print(
  new_df[
    new_df["Accuracy"].isna()
  ]
)