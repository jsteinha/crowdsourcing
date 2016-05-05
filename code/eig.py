import numpy as np
import numpy.linalg as la
from random import randint
n = 100
d = 10
A = np.zeros(shape=(n,n))
B = np.zeros(shape=(n,n))
for i in range(n):
  A[i,i] = 1.0
  B[i,i] = 1.0
  for _ in range(d):
    j = randint(0,n-1)
    A[i,j] = A[j,i] = 1.0
  for j in range(n):
    if i != j:
      B[i,j] = d * 2.0 / n
#print A
A = np.matrix(A)
B = np.matrix(B)
X = A.transpose() * la.inv(B) * A
Y = 2.0 * B
eigs = map(float,la.eig(X)[0])
print min(eigs), max(eigs)
