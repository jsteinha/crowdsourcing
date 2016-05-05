import numpy as np
import numpy.linalg as la
from scipy.linalg import sqrtm
from random import randint, random

import cvxopt as cvx
import cvxopt.lapack
import picos as pic
from picos.tools import trace

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

def adv(r,k):
  M = np.zeros(shape=(2*k*r,k*r))
  for j in range(r):
    for i2 in range(k):
      for j2 in range(k):
        for i in range(r):
          M[k*i+i2,k*j+j2] = 1
        M[k*(j+r)+i2,k*j+j2] = 1
  return M

def samp(M,p):
  I,J = M.shape
  Ms = np.zeros(shape=(I,J))
  for i in range(I):
    for j in range(J):
      if random() < p:
        Ms[i,j] = M[i,j] / p
      else:
        Ms[i,j] = 0
  return Ms

r = 4
k = 10
M = adv(r,k)
mu = r*k/3
print M
N1 = M.shape[0]
N2 = M.shape[1]
Ms = samp(M,11.0/N2)
print Ms

A = pic.new_param('A', Ms)
J = pic.new_param('J', np.ones(shape=(N1,N2)))
sdp = pic.Problem()
#M = sdp.add_variable('M',(N,N))
#W1 = sdp.add_variable('W1',(N,N),'symmetric')
#W2 = sdp.add_variable('W2',(N,N),'symmetric')
#sdp.add_constraint([[W1,M],[M.T,W2]]>>0)
U = sdp.add_variable('U',(N1+N2,N1+N2),'symmetric')
Mr = U[0:N1,N1:N1+N2]
W1 = U[0:N1,0:N1]
W2 = U[N1:N1+N2,N1:N1+N2]
sdp.add_constraint(U>>0)
sdp.add_constraint(Mr>0)
sdp.add_constraint(Mr<J)
sdp.set_objective('max', (A | Mr) - 0.5 * mu * (trace(W1)+trace(W2)))
print sdp
sdp.solve(verbose = 1, maxit=50)
val = sdp.obj_value()
print 'value: {0}'.format(val)

solution = Mr.value
print 'solution:'
print solution
