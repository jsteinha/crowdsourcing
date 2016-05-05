import cvxopt as cvx
import cvxopt.lapack
import numpy as np
import picos as pic
from random import randint

N = 40
m = (N*(N+1))/2
T = 100

def unpack(k):
  r = 0
  while True:
    if k <= r:
      return r, k
    else:
      k = k - (r+1)
      r = r + 1

maxval = 0
for t in range(T):
  A = np.zeros(shape=(N,N))
  I = np.eye(N)
  for k in range(m):
    i,j = unpack(k)
    u = 2 * randint(0,1) - 1
    A[i,j] = u
    A[j,i] = u
  print ''
  print 'A:'
  print A
  A = pic.new_param('A', A)
  #J = pic.new_param('J', np.ones(shape=(N,N)))
  sdp = pic.Problem()
  P = sdp.add_variable('P',(N,N),'symmetric')
  sdp.add_constraint(P>>0)
  sdp.add_constraint(P<<I)
  sdp.set_objective('max', A | P)
  print sdp
  sdp.solve(verbose = 1, maxit=50)
  val = sdp.obj_value()
  print 'value: {0}'.format(val)

  solution = P.value
  np.set_printoptions(precision=3,threshold='nan',linewidth=1000,suppress=True)
  print 'solution:'
  print solution

  maxval = max(maxval, val)
  print 'maxval', maxval

print 'maxmaxval', maxval
