import numpy.linalg as la
import numpy as np

N = 5
M = N*(N-1)/2

def unpack(k):
  r = 0
  while True:
    if k < r:
      return r, k
    else:
      k = k - r
      r = r + 1

S = np.zeros(shape=(M,N))
for j in range(M):
  r,c = unpack(j)
  S[j,r] = -1
  S[j,c] = 1

np.set_printoptions(suppress=True)

print S

Sinv = la.pinv(S).transpose()

print Sinv
