import numpy as np
import numpy.linalg as la
from scipy.linalg import sqrtm
from random import randint


def nuc(A):
  M = np.dot(A, A.transpose())
  #print 'M', M
  mv = np.max(np.abs(M))
  #print 'mv', mv
  if mv < 1e-4:
    return 0
  M = sqrtm(M + 1e-9 * np.eye(M.shape[0]))
  #print 'sqrt', M
  return np.real(np.trace(M))
  
def sv(A):
  M = np.dot(A, A.transpose())
  #print 'M', M
  mv = np.max(np.abs(M))
  #print 'mv', mv
  if mv < 1e-4:
    return 0 
  M = sqrtm(M + 1e-9 * np.eye(M.shape[0]))
  #print 'sqrt', M
  return la.eig(M)

def MM(A):
  M = np.dot(A, A.transpose())
  #print 'M', M
  mv = np.max(np.abs(M))
  #print 'mv', mv
  if mv < 1e-4:
    return 0 
  M = sqrtm(M + 1e-9 * np.eye(M.shape[0]))
  #print 'sqrt', M
  return M


def go(N,C,V):
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
  
  A = np.zeros(shape=(N,N))
  for i in range(C/2):
    for j in range(0, N):
      A[i,j] = V
  for i in range(C/2,C):
    for j in range(1,N):
      A[i,j] = V
  for i in range(C,N):
    A[i,0] = 1.0
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
  ratio = dif2 / dif1
  
  print 'ratio', ratio
  return ratio

#go(4, 2, 0.05)
#N = 500
#Ctape = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 30, 40, 50, 80, 100, 150, 200, 250]
#rtape = []
#for C in Ctape:
#  rtape.append(1.0/go(N,C))
#import matplotlib.pyplot as plt
#plt.plot(Ctape, rtape)
#plt.savefig('plot.pdf')

boundary = []
for a in range(1,30):
  b = 6
  #for b in range(1,11):
  for c in range(max(1,a/2-2),100):
    X = np.zeros(shape=(a+1+c,3*b/2))
    Y = np.zeros(shape=(a+1+c,3*b/2))
    for i in range(a):
      for j in range(3*b/2):
        X[i,j] = 1
        Y[i,j] = 1
    for j in range(b,3*b/2):
      X[a,j] = 1
    for j in range(3*b/2):
      Y[a,j] = 1
    for i in range(a+1,a+1+c):
      for j in range(b):
        X[i,j] = 1
        Y[i,j] = 1
    #print X
    #print Y
    xn = nuc(X)
    yn = nuc(Y)
    print a,b,c, 'xn', xn, 'yn', yn
    if yn > xn:
      print a,c
      boundary.append((a,c))
      break
