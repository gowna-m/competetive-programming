# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("729.txt", "r")
else:
 inputSrc = stdin

from itertools import permutations
import operator
num_datasets=int(inputSrc.readline().strip())
inputSrc.readline().strip()
for _ in range(num_datasets):
  inp=list(map(int,inputSrc.readline().strip().split()))
  n,h=inp[0],inp[1]
  s=""
  for i in range(n):
    if i<n-h:
      s+="0"
    else:
      s+="1"
  perm =  [''.join(p) for p in permutations(s)]
  # print ()
  dct={}
  for out in set(perm):
     binary_2_dec=int(out, 2)
     dct[out]=binary_2_dec
    
  sorted_d = sorted(dct.items(), key=operator.itemgetter(1))
  # print (sorted_d)
  for d in sorted_d:
    print (d[0])
    
