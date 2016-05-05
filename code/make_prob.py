f = open('prob.txt', 'w')
C = 8
N = 24
for i in range(C/2):
  f.write("1")
  for j in range(1,N):
    f.write(" 1")
  f.write("\n")
for i in range(C/2,C):
  f.write("0")
  for j in range(1,N):
    f.write(" 1")
  f.write("\n")
for i in range(C,N):
  f.write("1")
  for j in range(1,N):
    f.write(" 0")
  f.write("\n")
f.close()
