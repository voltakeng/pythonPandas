import pandas as pd 
import numpy as np 

# from list
data_ls = [10,20,30,"Iphone",True] 
data = pd.Series(data_ls)
print(data)
print("#######################")

# from tuple
data_tp = (40,50,60,"Python")
data = pd.Series(data_tp)
print(data)
print("#######################")

# from numpy
ndata = np.array([1,2,3,"KG","Apple",True])
data = pd.Series(ndata)
print(data)
print("#######################")

# adjust index number
items = ["มะม่วง", "กล้วย", "องุ่น"]
index = [10,20,30]
print(pd.Series(items))
data = pd.Series(items, index)
print(data)
print("#######################")

# from dictionary
colors = {"green":"เขียว", "red":"แดง", "yellow":"เหลือง"}
data = pd.Series(colors)
print(data)
print("#######################")
