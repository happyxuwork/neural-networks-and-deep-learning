# -*- coding: UTF-8 -*-
'''
@author: xuqiang
'''
import numpy as np
import pprint

sizes = [4, 3, 2, 3]
weights = [np.random.randn(x, y)
           for x, y in zip(sizes[:-1], sizes[1:])]
pprint.pprint(weights)


def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))


w = [
    [-1.04386064, 2.46290068, -1.86313879],
    [1.05429339, 0.40807847, -0.98684347]
]
activation = [[2, 1]]
b = [[1, 2, 3]]
z = np.dot(activation, w) + b
test = sigmoid(z)
print(test)
