import torch
# 标量
x = torch.tensor(3)
y = torch.tensor(2.0)
print(x)
print(y)
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)

# 向量
v1 = torch.arange(10)
v2 = torch.tensor([1., 2., 3., 5.])

print(v1)
print(v2)
print(len(v1))
print(len(v2))
print(v1.shape)
print(v2.shape)

# 矩阵
A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A)
print(A.T)
B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B)
print(B.T)
print(B == B.T)

X = torch.arange(20, dtype=torch.float32).reshape(5, 4)
Y = X.clone()
print(X)
print(Y)
print(X + Y)
print(X - Y)
print(X / Y)
print(X * Y)

