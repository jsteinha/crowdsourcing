import cvxopt as cvx
import cvxopt.lapack
import numpy as np
import picos as pic
from picos.tools import trace
from random import randint, random
from numpy.linalg import eig

np.set_printoptions(precision=3,threshold='nan',linewidth=1000,suppress=True)
f = open('prob.txt', 'r')
mu = 3.0
p = 0.3
mat = []
for line in f:
  row = line.rstrip("\n").split()
  mat.append(map(float,row))
A = np.matrix(mat)
print 'A:'
print A
print ''
N = A.shape[0]
if N != A.shape[1]:
  raise Exception('matrix is not square')
for i in range(N):
  for j in range(N):
    if random() < p:
      A[i,j] = A[i,j] / p
    else:
      A[i,j] = 0
print 'Ar:'
print A
print ''

I = np.eye(N)
A = pic.new_param('A', A)
J = pic.new_param('J', np.ones(shape=(N,N)))
sdp = pic.Problem()
#M = sdp.add_variable('M',(N,N))
#W1 = sdp.add_variable('W1',(N,N),'symmetric')
#W2 = sdp.add_variable('W2',(N,N),'symmetric')
#sdp.add_constraint([[W1,M],[M.T,W2]]>>0)
U = sdp.add_variable('U',(2*N,2*N),'symmetric')
M = U[0:N,N:2*N]
W1 = U[0:N,0:N]
W2 = U[N:2*N,N:2*N]
sdp.add_constraint(U>>0)
sdp.add_constraint(M>0)
sdp.add_constraint(M<J)
sdp.set_objective('max', (A | M) - mu * (trace(W1)+trace(W2)))
print sdp
sdp.solve(verbose = 1, maxit=50)
val = sdp.obj_value()
print 'value: {0}'.format(val)

solution = M.value
print 'solution:'
print solution

D, P = eig(solution)
D = np.real(D)
P = np.real(P)
print 'D:'
print D
print 'P:'
print P
