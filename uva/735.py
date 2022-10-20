# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("735.txt", "r")
else:
 inputSrc = stdin
from itertools import permutations

def findPairs(sum_,arr):
  res=[]
  for i in arr:
    total=sum_ - i
    for j in arr:
      total1 = total - j
      for k in arr:
        total2 = total1 - k
        if total2 == 0:
          a=tuple(sorted((i,j,k)))
          res.append(a)
  return set(res)
  
arr=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 45, 48, 50, 51, 54, 57, 60]
while True:
  inp=int(inputSrc.readline().strip())
  if inp<=0:
    print ("END OF OUTPUT")
    break
  output=findPairs(inp,arr)
  if len(output) == 0:
    print ("THE SCORE OF "+str(inp)+" CANNOT BE MADE WITH THREE DARTS.")
  else:
    print ("NUMBER OF COMBINATIONS THAT SCORES "+str(inp)+" IS "+str(len(output))+".")
    # print (len(output))
    out=[]
    for s in output:
      l = list(permutations(s))
      for li in l:
        out.append(li)
    print ("NUMBER OF PERMUTATIONS THAT SCORES "+str(inp)+" IS "+str(len(set(out)))+".")
    
  print ("**********************************************************************")
    # print(len(set(out)))
# findPairs(175,arr)
