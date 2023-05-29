# % This example is to show the usage of STP class.
# % Many useful methods are overloaded for STP class, thus you can use STP object as double.
import numpy as np
from STP import *

x = np.array([[1, 2, 1, 1],
              [2, 3, 1, 2],
              [3, 2, 1, 0]])
y = np.array([[1, -2],
              [2, -1]])

# % Covert x and y to STP class
a = STP(x)
b = STP(y)

c0 = spn(x, y, y)
c = a @ b @ b
print(c0, c.double())
print(type(c))
print('len: ', len(c))

# import torch
# a=torch.rand([4,5])
# torch.Tensor
# print(a.dtype)
# # a=a.numpy()
# b=np.int8(a)
# print(b)
