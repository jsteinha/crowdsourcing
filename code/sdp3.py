import cvxopt as cvx
import cvxopt.lapack
import numpy as np
import picos as pic
from random import randint

N = 6
m = N * (N-1) / 2

def unpack(k):
  r = 1
  while True:
    if k < r:
      return r, k
    else:
      k = k - r
      r = r + 1

maxmaxval = 0
for b in range(1<<m):
  A = np.zeros(shape=(N,N))
  I = np.eye(N)
  mu = 1.3
  for k in range(m):
    i,j = unpack(k)
    A[i,j] = 1 & (b >> k)
    A[j,i] = 1 & (b >> k)
  print ''
  print 'A:'
  print A
  A = pic.new_param('A', A)
  J = pic.new_param('J', np.ones(shape=(N,N)))
  sdp = pic.Problem()
  Bp = sdp.add_variable('B+',(N,N),'symmetric')
  Bm = sdp.add_variable('B-',(N,N),'symmetric')
  sdp.add_constraint(Bp>=0)
  sdp.add_constraint(Bm<=0)
  sdp.add_constraint(A-Bp-Bm << mu * I)
  sdp.set_objective('min', J | Bp)
  print sdp
  sdp.solve(verbose = 1, maxit=50)
  print 'value: {0}'.format(sdp.obj_value())

  solution = Bp.value
  np.set_printoptions(precision=3,threshold='nan',linewidth=1000,suppress=True)
  print 'solution:'
  print np.array(solution)

  maxval = np.max(np.array(solution))
  maxmaxval = max(maxval, maxmaxval)
  print 'maxval', maxval, maxmaxval

print 'maxmaxval', maxmaxval
