import torch

x = torch.tensor(3.0)
y = torch.tensor(9.0)
print(x, y)
print(x + y, x - y, x * y, x / y, x ** y)

v1 = torch.tensor([1., 2., 4., 9.])
v2 = torch.arange(12, dtype=torch.float32)
print(v1)
print(v2)
print(v2[3])
print(len(v1))
print(v2.shape)

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
print(A)
print(A[0, 1])
print(A.T)

B = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
print(B == B.T)

X = torch.arange(24).reshape(2, 3, 4)
print(X)
print(X.sum())

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
B = A.clone()
print(A + B)
print(A * B)

print(A.shape)
print(A.sum())


print(A)
A_sum_axis_0 = A.sum(axis=0)
A_sum_axis_1 = A.sum(axis=1)

print(A_sum_axis_0, A_sum_axis_0.shape)
print(A_sum_axis_1, A_sum_axis_1.shape)

print(A.mean())
print(A.sum() / A.numel())
print(A.mean(axis=0))
print(A.sum(axis=0) / A.shape[0])

print(A.sum(axis=1, keepdim=True))
print(A / A.sum(axis=1, keepdim=True))

print(A)
print(A.cumsum(axis=0))
print(A.cumsum(axis=1))

x = torch.arange(1, 5, dtype=torch.float32)
y = torch.ones(4, dtype=torch.float32)
print(x, y)
print(torch.dot(x, y))
print(torch.sum(x * y))

A = torch.arange(20, dtype=torch.float32).reshape(5, 4)
x = torch.arange(1, 5, dtype=torch.float32)
print(torch.mv(A, x))