# This example is to show how to perform semi-tensor product
import numpy as np
from STP import *

x = np.array([[1, 2, 3, -1]])
y = np.array([[2, 1]]).T
# print(x.shape,y.shape)
r1 = sp(x, y)
print(r1)

x = np.array([[2, 1]])
y = np.array([[1, 2, 3, -1]]).T
r2 = sp(x, y)
print(r2)

x = np.array([[1, 2, 1, 1],
              [2, 3, 1, 2],
              [3, 2, 1, 0]])
y = np.array([[1, -2],
              [2, -1]])
r3 = sp(x, y)
r4 = sp1(x, y)
print(r3)
print(r4)
# r3 = r4 = [3,4,-3,-5;4,7,-5,-8;5,2,-7,-4]

r5 = sp(sp(x, y), y)
r6 = spn(x, y, y)
print('*' * 60)
print(r5)
print(r6)
