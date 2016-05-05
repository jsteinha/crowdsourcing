import cvxopt as cvx
import cvxopt.lapack
import numpy as np
import picos as pic
from random import randint

sdp = pic.Problem()
N = 60
#plus = [(0,1),(0,2),(0,4),(2,3),(2,4),(5,6),(6,7),(6,8),(5,9),(6,9),(8,9)]
#minus = [(0,5),(0,7),(1,8),(2,7),(3,9),(4,6),(0,8)]
plus = []
minus = []
m = 3
for i in range(N/2):
  # m from each row
  for _ in range(m):
    j = randint(0,N/2-1)
    while (j,i) in plus or (i,j) in plus:
      j = randint(0,N/2-1)
    plus.append((i,j))

    j = randint(0,N/2-1)
    while (j+N/2,i+N/2) in plus or (i+N/2,j+N/2) in plus:
      j = randint(0,N/2-1)
    plus.append((i+N/2,j+N/2))

    j = randint(0,N/2-1)
    while (j+N/2,i) in minus or (i,j+N/2) in minus:
      j = randint(0,N/2-1)
    minus.append((i,j+N/2))
print plus
print minus

X = sdp.add_variable('X',(2*N+1,2*N+1),'symmetric')
sdp.add_constraint(X>>0)
sdp.add_constraint(X[2*N,2*N]<=1)
sdp.add_constraint(X>=0)
for i in range(N):
  sdp.add_constraint(X[i,i]==X[i,2*N])
  sdp.add_constraint(X[i,i]==X[i,i+N])
  sdp.add_constraint(X[i+N,i+N]==X[i+N,2*N])
for (i,j) in plus:
  sdp.add_constraint(X[i,i]==X[i,j+N])
for (i,j) in minus:
  sdp.add_constraint(X[i,j+N]==0)
diag = np.array([1]*N + [0]*(N+1))
C = pic.new_param('C',np.diag(diag))
print X
print C
sdp.set_objective('max', C | X)

print sdp
sdp.solve(verbose = 1, maxit=50)

print 'value: {0}'.format(sdp.obj_value())

solution = X.value

np.set_printoptions(precision=2,threshold='nan',linewidth=1000,suppress=True)
print 'solution:'
print np.array(solution)
