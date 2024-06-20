import torch

x = torch.tensor([1.0, 2.0, 4.0, 9.0])
y = torch.arange(12.0, dtype=torch.float32)
print(x)
print(y)
print(len(x))
print(y.shape)

A = torch.arange(12.0, dtype=torch.float32).reshape(3, 4)
print(A)
print(A.sum())
print(A.sum(axis=0))
print(A.sum(axis=1))
print(A.sum(axis=[0, 1]))

print(A.mean())
print(A.sum() / A.numel())
print(A.mean(axis=0))
print(A.sum(axis=0) / A.shape[0])

print(A.sum(axis=0, keepdims=True)) # tensor([[12., 15., 18., 21.]])
"""
tensor([[1.5000],
        [5.5000],
        [9.5000]])
"""
print(A.mean(axis=1, keepdims=True))
""" 通过广播计算
tensor([[0.0000, 0.0667, 0.1111, 0.1429],
        [0.3333, 0.3333, 0.3333, 0.3333],
        [0.6667, 0.6000, 0.5556, 0.5238]])
"""
print(A / A.sum(axis=0, keepdims=True))
"""沿轴0累计和
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  6.,  8., 10.],
        [12., 15., 18., 21.]])
"""
print(A.cumsum(axis=0))
"""沿轴1累计和
tensor([[ 0.,  1.,  3.,  6.],
        [ 4.,  9., 15., 22.],
        [ 8., 17., 27., 38.]])
"""
print(A.cumsum(axis=1))

X = torch.tensor([[1, 2, 3], [2, 0, 4], [3, 4, 5]])
Y = X.T
print(X)
print(Y)
print(X == Y)


x = torch.arange(1, 6, dtype=torch.float32)
y = torch.tensor([1.0, 2.0, 3.0, 5.0, 8.0])
print(torch.dot(x, y))   # tensor(74.)
print(torch.sum(x * y))


"""torch.Size([3, 4])
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
"""
A = torch.arange(12.0).reshape(3, 4)
# tensor([4., 3., 2., 1.])
x = torch.tensor([4.0, 3.0, 2.0, 1.0])
print(A)
print(x)  
print(torch.mv(A, x))  # tensor([10., 50., 90.])

x = torch.tensor([])