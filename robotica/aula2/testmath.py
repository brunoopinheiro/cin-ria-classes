#! /home/bopj/repos/cin-ria-classes/robotica/aula2/.venv/bin/python3


import numpy as np
from numpy.linalg import inv

a = np.array([3, 2, 1])
b = np.array([2, 2, 3])
m = np.array([[1, 2, 3], [4, 12, 6], [9, 8, 7]])
n = np.array([[5, 6, 7], [8, 9, 1], [2, 4, 4]])

c = m @ a
print(c)

d = inv(m) @ b
print(d)

e = inv(m) @ n @ a
print(e)
