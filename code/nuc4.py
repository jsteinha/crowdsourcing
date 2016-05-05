import numpy as np
import numpy.linalg as la
from scipy.linalg import sqrtm
from random import randint


def go(N,C):
  m = N * N
  
  P = np.zeros(shape=(N,N))
  I = np.eye(N)
  for i in range(C):
    for j in range(C):
      P[i,j] = 1.0/C
  for i in range(C, N):
    P[i,i] = 1.0
  #print 'P', P
  
  #Q = np.zeros(shape=(C,N))
  #for i in range(C):
  #  Q[i,i] = 1.0
  
  def nuc(A):
    M = np.dot(A, A.transpose())
    #print 'M', M
    mv = np.max(np.abs(M))
    #print 'mv', mv
    if mv < 1e-4:
      return 0
    M = sqrtm(M + 1e-6 * np.eye(M.shape[0]))
    #print 'sqrt', M
    return np.real(np.trace(M))
  
  M = np.zeros(shape=(N,N))
  for i in range(N):
    for j in range(N):
      M[i,j] = randint(0,1)
  ### print ''
  ### print 'M:'
  ### print M
  
  #print ''
  #print 'PA:'
  #print np.dot(P,A)
  
  nuc1 = nuc(np.dot(P,M))
  nuc2 = nuc(np.dot(I-P,M))
  nuc3 = nuc(M)
  ### print nuc1, nuc2, nuc3, nuc1+nuc2

  return (nuc3 - nuc1) / nuc2

minratio = 1
for _ in range(300000):
  ratio = go(5, 2)
  minratio = min(minratio, ratio)
  print 'ratio', ratio, minratio
