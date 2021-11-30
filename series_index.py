import pandas as pd 

colors = {"green":"เขียว", "red":"แดง", "yellow":"เหลือง"}

print(pd.Series(colors)["green"])
print(pd.Series(colors)[1])
print("###############################")

data = pd.Series(colors)
print(data["yellow"])
print(data[2])
print("###############################")

