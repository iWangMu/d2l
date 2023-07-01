# import os
# os.makedirs(os.path.join(".", "data"), exist_ok=True)
# data_file = os.path.join(".", "data", "house_tiny.csv")
# with open(data_file, "w") as f:
#     f.write("NumRooms, Alley, Price\n")
#     f.write("NA, Pave, 127500\n")
#     f.write("2, NA, 106000\n")
#     f.write("4, NA, 178100\n")
#     f.write("NA, NA, 140000\n")

import os
import pandas as pd
import torch

data_file = os.path.join(".", "data", "house_tiny.csv")
data = pd.read_csv(data_file)
print(data)
# 位置索引iloc拆分数据
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2:]
print(inputs)
print(outputs)
# 使用均值替换inputs的NaN值
inputs = inputs.fillna(inputs.mean())
print(inputs)
# 设置巷子类型的值，存在为1，不存在为0
inputs = pd.get_dummies(inputs, dummy_na=True)
inputs = inputs.iloc[:, 0:-1]
print(inputs)

x, y = torch.tensor(inputs.values), torch.tensor(outputs.values)
print(x)
print(y)