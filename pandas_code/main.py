import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250101.csv")

color_data = data["Primary Fur Color"].to_list()

color_dict = {}

for color in color_data:
    if pandas.notna(color):
        if color_dict.__contains__(color):
            color_dict[color] = color_dict[color] + 1
        else:
            color_dict[color] = 1

dataframe = pandas.DataFrame(list(color_dict.items()), columns=["Fur Color", "Count"])
dataframe.to_csv("Squirrel_color_statistics.csv")
