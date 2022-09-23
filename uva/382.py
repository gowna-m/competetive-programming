# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("382.txt", "r")
else:
 inputSrc = stdin
  

integers=list(map(int,inputSrc.readline().strip().split()))
# print (integers)
print ("PERFECTION OUTPUT")
for n in integers:
  if n == 0:
    break
  tmp=n//2
  sum_=0
  for i in range(1,tmp+1):
    if n % i == 0:
      sum_+=i
      
  if (sum_ == n):
    print (str(n).rjust(5)+"  PERFECT")
  elif sum_ < n:
    print (str(n).rjust(5)+"  DEFICIENT")
  else:
    print (str(n).rjust(5)+"  ABUNDANT")
print ("END OF OUTPUT")
