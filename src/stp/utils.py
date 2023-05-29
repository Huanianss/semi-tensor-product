import numpy as np


def sp(A, B):
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


def sp1(A, B):
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
    elif n % p == 0:
        C = leftsp(A, B)
    elif p % n == 0:
        C = leftsp(B.T, A.T).T
    else:
        # for other cases, it will use the kron function to expand them and make their dimensions match
        z = np.lcm(n, p)
        C = np.kron(A, np.eye(z // n)) @ np.kron(B, np.eye(z // p))
        # error('The input arguments do not meet the multiple dimension matching condition.');
    return C


def leftsp(A, B):
    m, n = A.shape
    p, q = B.shape
    k = n // p
    C = np.zeros([m, k * q])
    for i in range(m):
        for j in range(q):
            C[i, j * k:j * k + k] = (np.reshape(A[i, :], [k, p], order='F') @ B[:, j]).T
            # print((np.reshape(A[i, :], [k, p]) @ B[:, j]).T.shape)
    return C


def spn(*args):
    # print(len(args))
    '''
    % SPN    (Left) Semi-tensor product of matrices with arbitrary number of matrices
    %
    %   SPN(A,B,C,...) calculates the (left) semi-tensor product of arbitrary
    %   number of matrices which have the proper dimensions.
    :param args: matrices, A,B,C,...
    :return: stp of A,B,C,...
    '''
    ni = len(args)
    if ni == 0:
        raise Exception('No input arguments.')
    elif ni == 1:
        return args[0]
    elif ni == 2:
        return sp1(args[0], args[1])
    else:
        r = sp1(args[0], args[1])
        for i in range(2, ni):
            r = sp1(r, args[i])
        return r


def rightsp(A, B):
    '''

    :param A: a matrix
    :param B: another matrix
    :return: the Right Semi-tensor Product of A and B
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
        t = np.lcm(n, p)
        C = np.kron(np.eye(t // n), A) @ np.kron(np.eye(t // p), B)
    return C


def rightspn(*args):
    '''
    % SPN    (Right) Semi-tensor product of matrices with arbitrary number of matrices
    %
    %   rightspn(A,B,C,...) calculates the (Right) semi-tensor product of arbitrary
    %   number of matrices which have the proper dimensions.
    :param args: matrices, A,B,C,...
    :return: stp of A,B,C,...
    '''
    ni = len(args)
    if ni == 0:
        raise Exception('No input arguments.')
    elif ni == 1:
        return args[0]
    elif ni == 2:
        return rightsp(args[0], args[1])
    else:
        r = rightsp(args[0], args[1])
        for i in range(2, ni):
            r = rightsp(r, args[i])
        return r



def bt(A, p, r):
    # % BT    Perform block transpose
    # %
    # %   B = BT(A,S,T)
    # %
    # %   Example: a = round(rand(3,4)*10), b = bt(a,1,2)
    # A = np.random.random([3*5, 7*11])  # [pq,rs][22,23]
    # print(A.shape)
    # B = bt(A, p=3, r=7)
    # print(B.shape)
    m, n = A.shape
    if m % p != 0 or n % r != 0:
        raise Exception('The dimensions of the first argument do not meet the conditions of block transpose.')
    q = m // p
    s = n // r
    B = np.zeros([s * p, q * r])
    for i in range(q):
        for j in range(s):
            B[j * p:(j + 1) * p, i * r:(i + 1) * r] = A[i * p:(i + 1) * p, j * r:(j + 1) * r]
            # print(i, j)
    return B




def wij(*args):
    '''
    % WIJ    Produces swap matrix
    %
    %   A = WIJ(N) produces an N^2-by-N^2 swap matrix.
    %   A = WIJ(M,N) produces an MN-by-MN swap matrix.
    # w = wij(3, 2)
    # print(w)
    '''
    if len(args) == 1:
        m = n = args[0]
    else:
        m, n = args[0], args[1]
    d = m * n
    w = np.zeros([d, d])
    idx = np.arange(d).reshape([m, n], order='F').reshape([1, -1])
    idy = np.arange(d)
    w[idx, idy] = 1

    return w




def vr(A):
    # % VR Produce row stacking form of a matrix
    # A = np.random.rand(*[2, 3])
    # B = vr(A)
    # print(A, B)
    return A.reshape([1, -1])





def invvc(*args):
    # % INVVC Inverse of VC
    # %
    # % A = INVVC(X, M) creates an M - row matrix from the vector X.
    # %
    # % Example: a = invvc(1:12)
    # % a = invvc(1:12, 3)

    # x = np.arange(5).reshape([-1, 1])
    # print(x)
    # invvc(x)
    if len(args) == 1:
        x = args[0]
        m = np.ceil(np.sqrt(x.shape[0]))
        m = int(m)
    else:
        x = args[0]
        m = args[1]

    l = x.shape[0]
    if m ** 2 > l and len(args) == 1:
        n = m ** 2 - x.shape[0]
    elif l % m != 0:
        n = m - l % m
    else:
        n = 0

    x = np.concatenate([x, np.zeros([int(n), 1])])
    l = x.shape[0]

    x = x.reshape([m, l // m], order='F')
    return x




def invvr(*args):
    # A = invvr(x, n)
    # % INVVC Inverse of VR
    # %
    # % A = INVVR(X, N) produces an
    # N - row matrix from the vector X.
    # %
    # % Example: a = invvr(1:12)
    # % a = invvr(1:12, 3)

    if len(args) == 1:
        A = invvc(args[0])
    else:
        A = invvc(*args)
    return A.T


def dec2any(a, *args):
    # % DEC2ANY    Convert a decimal number to a k-based number as a vector of a given length
    # %            it will add zeros if len is larger than the valid length of the vector
    # %
    # %   V = DEC2ANY(A)       % convert a decimal number to a binary number as a vector
    # %   V = DEC2ANY(A,K)     % convert a decimal number to a K-based number
    # %   V = DEC2ANY(A,K,LEN) % convert a decimal number to a K-based number of length LEN
    # %
    # %   Example: v = dec2any(11)
    # %            v = dec2any(11,2)
    # %            v = dec2any(11,2,6)
    l_a = len(args)
    if l_a == 0:
        k = 2
        len_ = 0
    elif l_a == 1:
        k = args[0]
        len_ = 0
    elif l_a == 2:
        k = args[0]
        len_ = args[1]

    if a < 0:
        raise Exception('The first input argument must be a non-negative integer')

    if k < 2:
        raise Exception('The second input argumant must be a positive integer')

    if len_ < 0:
        raise Exception('The third input argumant must be a positive integer')
    l = np.ceil(np.log2(a + 0.5) / np.log2(k))
    l = int(l)
    v = np.zeros([1, l])
    # print(a, k, l)
    if a < k:
        v = [a]
    else:
        i = 1
        while (a >= k):
            t = a % k
            a = a // k
            v[0, l - i] = t
            i = i + 1
        v[0, 0] = a

    if len_ > 0 and l < len_:
        v1 = np.zeros([1, len_])
        v1[0, (len_ - l):] = v[0, :]
        v = v1
    return v

def dec2binv(a,*args):
    # % DEC2BINV    Convert a decimal number to a binary vector of a given length
    # %
    # %   Example: v = dec2binv(11)
    # %            v = dec2binv(11,6)
    # v = dec2any(11)
    # v = dec2any(11, 2)
    # v = dec2any(11, 2, 6)
    # print(v)
    # v = dec2binv(11)
    # v = dec2binv(11, 6)
    # print(v)
    if len(args)==0:
        len_=0
    elif  len(args)==1:
        len_=args[0]

    v=dec2any(a,2,len_)
    return v