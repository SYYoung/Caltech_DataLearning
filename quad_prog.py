import numpy as np
import cvxopt

from cvxopt import matrix
from cvxopt import solvers

# Define QP parameters (directly)
directly = False
if (directly):
    P = matrix([[1.0, 0.0], [0.0, 0.0]])
    q = matrix([3.0, 4.0])
    G = matrix([[-1.0, 0.0, -1.0, 2.0, 3.0], [0.0, -1.0 -3.0, 5.0, 4.0]])
    h = matrix([0.0, 0.0, -15.0, 100.0, 80.0])

# Define QP parameters (with Numpy)
if not directly:
    P = matrix(np.diag([1,0]), tc='d')
    q = matrix(np.array([3, 4]), tc='d')
    G = matrix(np.array([[-1,0], [0,-1], [-1,-3], [2,5], [3,4]]), tc='d')
    h = matrix(np.array([0, 0, -15, 100, 80]), tc='d')

# construct the QP, invoke solver
sol = solvers.qp(P, q, G, h)

# Extract optimal values and solution
print(sol['x'])
print(sol['primal objective'])

