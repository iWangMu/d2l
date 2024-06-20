import random
import matplotlib.pyplot as plt
import torch

"""
w = [2, 
     -3.4]
b = 4.2
e服从均值为0的正态分布, 标准差是0.01
"""
def synthetic_data(w, b, num_examples):
    """ y = wx + b + e """
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape(-1, 1)

true_w = torch.tensor([2, -3.4])
true_b = 4.2

features, labels = synthetic_data(true_w, true_b, 1000)
print(features[0])
print(labels[0])

plt.scatter(features[:, 1].detach().numpy(), labels.detach().numpy(), 1)
plt.show()
