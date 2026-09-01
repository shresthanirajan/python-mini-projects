import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()


# print(data["temp"].mean())
# print(data["temp"].max())

# #Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Tuesday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]


monday_temperture = ((monday.temp * 1.8) + 32)
print(monday_temperture)