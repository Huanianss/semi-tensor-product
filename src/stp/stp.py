# % STP/STP    Semi-tensor product (STP) class constructor.
# %  m = STP(a)    creates an STP object from the matrix A.
import numpy as np
class STP:
    '''

    '''

    def __init__(self, *args):
        '''

        '''
        ni = len(args)
        if ni == 0:
            self.c = []
        elif isinstance(args[0], STP):
            # print('is STP')
            self = args[0]
        elif isinstance(args[0], (float, int,bool,complex,np.ndarray)):
            self.c = args[0]
        else:
            raise Exception(r'Conversion to "STP" from ', type(args[0]), ' is not allowed.')
        # self.c = args[0]

    def sp(self, A, B):
        '''

        :param A: a matrix
        :param B: another matrix
        :return: the Semi-tensor Product of A and B
        '''
        # print(A.dims)
        # if A.ndim==1:
        #     A=A
        if A.ndim > 2 or B.ndim > 2:
            raise Exception("Input arguments must be 2-D.")

        n = A.shape[1]
        p = B.shape[0]
        if n == p:
            C = A @ B
        else:
            z = np.lcm(n, p)
            C = np.kron(A, np.eye(z // n)) @ np.kron(B, np.eye(z // p))
        return C
    def __matmul__(self, other):
        return STP(self.sp(self.c, other.c))
    def __add__(self, other):
        if not isinstance(other, STP):
            other = STP(other)
        return STP( (self.c+ other.c))
    def __sub__(self, other):
        if not isinstance(other,STP):
            other=STP(other)

        return STP((self.c - other.c))
    def __mul__(self, other):
        if not isinstance(other,STP):
            other=STP(other)
        return STP((self.c * other.c))




    def __str__(self):
        return str(self.c)
    def double(self):
        return self.c
    def __len__(self):
        return max(self.c.shape)

    def shape(self):
        return self.c.shape
    def size(self):
        return self.shape()
    def T(self):
        self.c=self.c.T
        return self
    def __pow__(self, power, modulo=None):
        self.c=self.c**power
        return self
    def __eq__(self, other):
        return self.c==other.c
    def __neg__(self):
        # self.c=-self.c
        # return self
        return STP(-self.c)
    def __pos__(self):
        return self
    def __getitem__(self, item):
        return STP(self.c[item])

if '__main__'==__name__:
    b = STP(np.random.random([2,3]))
    # print(b.c)
    # c = STP(b)
    # print(type(1.0))
    print(b)
    b.T()
    print(b)
    print(b**2)
    print(b==b-1)
    print(-b)
    print(+b)
    print(b[0:2,0:1])
    a=b
    # a=b[0:2,0:1]


    np.abs(1)