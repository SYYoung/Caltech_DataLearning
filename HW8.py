import numpy as np
import cvxopt

from cvxopt import matrix
from cvxopt import solvers


def loadFile(fname):
    y = []
    x = []
    with open(fname) as f:
        for line in f:
            myInput = list(map(float, line.split()))
            y.append(int(myInput[0]))
            x.append(myInput[1:])
    return np.array(x), np.array(y)

def polyKernel(x, m, n, Q):
    t1 = 1 + np.dot(x[m,:], x[n,:])
    return t1**Q

# Define QP parameters (directly)
Q = 2
def buildMatrixP(x, y):
    dim = len(y)
    quadCoef = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            quadCoef[i][j] = y[i] * y[j] * polyKernel(x, i, j, Q)

    return quadCoef

def quadProgram(X, Y):
    directly = False
    if (directly):
        P = matrix([[1.0, 0.0], [0.0, 0.0]])
        q = matrix([3.0, 4.0])
        G = matrix([[-1.0, 0.0, -1.0, 2.0, 3.0], [0.0, -1.0 -3.0, 5.0, 4.0]])
        h = matrix([0.0, 0.0, -15.0, 100.0, 80.0])

    # Define QP parameters (with Numpy)
    if not directly:
        N = len(Y)
        C = 0.01
        P = matrix(buildMatrixP(X, Y), tc='d')

        q1 = np.zeros(N) - 1
        q = matrix(q1, tc='d')

        # build -I
        g1 = np.eye(N) * -1
        g2 = np.eye(N)
        g3 = np.vstack((g1, g2))
        G = matrix(g3, tc='d')

        h1 = np.zeros((N, 1))
        h2 = np.zeros((N, 1)) + C
        h3 = np.vstack((h1, h2))
        h = matrix(h3, tc='d')

        A1 = Y.copy().reshape((1, N))
        A = matrix(A1, tc='d')
        b = matrix(np.zeros(1))

    # construct the QP, invoke solver
    #sol = solvers.qp(P, q, G, h)
    sol = solvers.qp(P, q, G, h, A, b)

    # Extract optimal values and solution
    #print(sol['x'])
    #print(sol['primal objective'])
    return sol['x']

THRESHOLD = 1.0e-7
def getPlane(alpha, X, Y):
    dim = len(Y)
    t1 = alpha * Y.reshape((dim, 1))
    t2 = t1 * X
    w = np.sum(t2, axis=0)
    # calculate b
    dim = len(alpha)
    for i in range(dim):
        if alpha[i] > THRESHOLD:
            t1 = np.dot(w, X[i,:]) * Y[i]
            b = (1 - t1) / Y[i]
            break
    return w, b

def modifyY(group1, Y):
    newY = Y.copy()
    newY[Y != group1] = -1
    newY[Y == group1] = 1

    return newY

def getEstimate(X, w, b):
    val = np.array(X @ w + b)
    val[val > 0] = 1
    val[val < 0] = -1
    return val

#fileName = "test_feature.txt"
#fileName = "features.test.txt"
fileName = "features.train.txt"
X, Y = loadFile(fileName)
#groups = [0, 2, 4, 6, 8]
#groups = [1, 3, 5, 7, 9]
groups = [1]
Ein_all = {}
for group1 in groups:
    Y1 = modifyY(group1, Y)
    alpha = quadProgram(X, Y1)
    w, b = getPlane(alpha, X, Y1)
    estY = getEstimate(X, w, b)
    Ein = 1 - sum(Y1 == estY) / len(Y)
    print("group 1 = " + str(group1) + " , Ein = " + str(Ein))
    Ein_all[str(group1)] = Ein

print(Ein_all)

