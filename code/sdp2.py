import cvxopt as cvx
import cvxopt.lapack
import numpy as np
import picos as pic
from random import randint

sdp = pic.Problem()
N = 5
M = 3

X = sdp.add_variable('X',(2*(M+N)+1,2*(M+N)+1),'symmetric')
sdp.add_constraint(X>>0)
sdp.add_constraint(X[0,0]<=1)
sdp.add_constraint(X>=0)
for i in range(N+M):
  sdp.add_constraint(X[i+1,i+1]==X[i+1,0])
  sdp.add_constraint(X[i+1,i+1]==X[i+1,i+N+M+1])
  sdp.add_constraint(X[i+N+M+1,i+N+M+1]==X[i+N+M+1,0])
for i in range(M):
  sdp.add_constraint(X[i+N+M+1,i+N+M+1]==1)
  for j in range(M,N+M):
    sdp.add_constraint(X[i+1,j+N+M+1]==0)
diagC = np.array([0] + [1] * M + [0]*(2*N+M))
C = pic.new_param('C',np.diag(diagC))
diagD = np.array([0] + [0] * M + [1] * N + [0] * (N+M))
D = pic.new_param('D',np.diag(diagD))
sdp.add_constraint(D|X >= 2);
sdp.set_objective('max', C | X)

print sdp
sdp.solve(verbose = 1, maxit=50)

print 'value: {0}'.format(sdp.obj_value())

solution = X.value

np.set_printoptions(precision=3,threshold='nan',linewidth=1000,suppress=True)
print 'solution:'
print np.array(solution)
