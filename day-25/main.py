# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
#
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240511.csv")
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_count)



