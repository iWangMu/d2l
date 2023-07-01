import torch
import numpy as np

# 一个轴的张量(tensor), 向量(vector)
x = torch.arange(12)
print(x)
# 张量的shape属性来访问张量（沿每个轴的长度）的形状 
print(x.shape)
print(x.dtype)
# 张量中元素的总数，即形状的所有元素乘积，可以检查它的大小（size）
print(x.numel())
# 要想改变一个张量的形状而不改变元素数量和元素值，可以调用reshape()
# 从向量转换为矩阵
#  幸运的是，我们可以通过-1来调用此自动计算出维度的功能。 即我们可以用x.reshape(-1,4)或x.reshape(3,-1)来取代x.reshape(3,4)
print(x.reshape(3, 4))
print(x.reshape(-1, 6))
print(x.reshape(2, -1))

# 全0张量
print(torch.zeros(2, 3, 4))
# 全1张量
print(torch.ones(2, 3, 4))
# 其中的每个元素都从均值为0、标准差为1的标准高斯分布（正态分布）中随机采样
print(torch.randn(3, 4))
# 我们还可以通过提供包含数值的Python列表（或嵌套列表），来为所需张量中的每个元素赋予确定值。 在这里，最外层的列表对应于轴0，内层的列表对应于轴1。
print(torch.tensor(np.random.randn(3, 4)))
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))


# 按元素（elementwise）运算
# 将标量函数升级为按元素向量运算来生成向量值
x1 = torch.tensor([1.0, 2, 4, 8])
y1 = torch.tensor([2, 2, 2, 2])
print((x1 + y1, x1 - y1, x1 * y1, x1 / y1, x1 ** y1))
# torch.exp()幂运算
print(torch.exp(x1))
# 张量连结（concatenate）在一起
# (3, 4) cat (3, 4)
x2 = torch.arange(12, dtype=torch.float32).reshape(3, 4)
y2 = torch.tensor([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
print(x2, y2)
print(torch.cat((x2, y2), dim=0))
print(torch.cat((x2, y2), dim=1))

# 逻辑运算符
print(x2 == y2)
print(x2 != y2)
print(x2 > y2)
print(x2 >= y2)
print(x2 < y2)
print(x2 <= y2)

print(x2.sum())
print(y2.sum())

"""a
[[0]      [[0, 0]
[1]   =>   [1, 1]
[2]]       [2, 2]]
"""
a = torch.arange(3).reshape(3, 1)
"""b
[[0, 1]]  =>  [[0, 1]
               [0, 1]
               [0, 1]]
"""
b = torch.arange(2).reshape(1, 2)
print(a + b)

X = torch.arange(12, dtype=torch.float32).reshape(3, 4)
print(X)
print(X[-1])
print(X[1:3])
X[1, 2] = 9
print(X)

# 节省内存
x3 = torch.arange(12).reshape(3, 4)
print(id(x3))
y3 = torch.arange(10, 22).reshape(3, 4)
print(id(y3))
# 会分配新的内存
# y3 = x3 + y3
# print(id(y3))
# 
# y3 += x3
# print(id(y3))
y3[:] = x3 + y3
print(id(y3))

L = torch.arange(12).reshape(3, 4)
M = L.numpy()
print(type(L), type(M))
print(id(L), id(M))
print(L, M)
M[0, 1] = 12
print(L, M)

Z = torch.tensor([9.2])
print(Z.item())
print(float(Z))
print(int(Z))


P = torch.arange(4).reshape(2, 1, 2)
Q = torch.arange(6).reshape(2, 3, 1)
print(P)
print(Q)
print(P + Q)
