import numpy as np
import numpy.linalg as la
from scipy.linalg import sqrtm


N = 4
C = 2
m = N * N

P = np.zeros(shape=(N,N))
for i in range(C):
  for j in range(C):
    P[i,j] = 1.0/C
for i in range(C, N):
  P[i,i] = 1.0
print 'P', P

Q = np.zeros(shape=(C,N))
for i in range(C):
  Q[i,i] = 1.0

def unpack(k):
  r = 0
  while True:
    if k < N:
      return r, k
    else:
      k = k - N
      r = r + 1
def nuc(A):
  M = np.dot(A, A.transpose())
  #print 'M', M
  mv = np.max(np.abs(M))
  #print 'mv', mv
  if mv < 1e-4:
    return 0
  M = sqrtm(M + 1e-6 * np.eye(M.shape[0]))
  #print 'sqrt', M
  return np.trace(M)

maxmaxval = 0
for b in range(1<<m):
  A = np.zeros(shape=(N,N))
  for k in range(m):
    i,j = unpack(k)
    A[i,j] = 1 & (b >> k)
    #A[i,j] = 2 * A[i,j] - 1
  print ''
  print 'A:'
  print A
  
  #print ''
  #print 'PA:'
  #print np.dot(P,A)

  dif1 = nuc(A) - nuc(np.dot(P,A))
  dif2 = nuc(np.dot(Q,A)) - nuc(np.dot(Q,np.dot(P,A)))
  print 'dif1', dif1, 'dif2', dif2
  dif1 = np.real(dif1)
  dif2 = np.real(dif2)
  if abs(dif2) < 1e-4:
    continue
  if abs(dif1) < 1e-4:
    print 'INFINITE RATIO'
  ratio = dif2 / dif1

  maxmaxval = max(ratio, maxmaxval)
  print 'ratio', ratio, maxmaxval

print 'maxval', maxmaxval
