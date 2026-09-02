import pandas as pd
data = {"Model": ["Logistic Regession", "Random Forest", "Decision Tree", "KNN"], "accuracy": [0.84, 0.91, 0.79, 0.86],
        "training_time": [12, 35, 8, 15]}

data_set = pd.DataFrame(data)

# print(data_set[["Model", "accuracy"]])

# print(data_set[ 
#   data_set["accuracy"] >= 0.85
# ])

# print(data_set[
#   data_set["training_time"] < 20
# ])

# print(data_set[
#   (data_set["training_time"] < 20) & (data_set["accuracy"] > 0.80)
# ])

# print(data_set[
#   (data_set["accuracy"] > 0.90) | (data_set["training_time"] < 10)
# ])

# print(data_set[
#   data_set["accuracy"] > 0.85 & data_set["Model"]
# ])

print(data_set[
  data_set["accuracy"] > 0.85
][["Model", "accuracy"]])

print(data_set[
  data_set["training_time"] < 20]
  [["Model", "training_time"]]
)
print(data_set
  [["Model", "training_time"]]
)
print(data_set
  [["training_time", "training_time"]]
)