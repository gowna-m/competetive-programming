# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("713.txt", "r")
else:
 inputSrc = stdin
num_tests = int(inputSrc.readline().strip())

for i in range(num_tests):
  line = inputSrc.readline().strip().split()
  a, b = line[0], line[1]
  # print (a[::-1],b[::-1])
  # print (int(a[::-1]),int(b[::-1]))
  c = str(int(a[::-1]) + int(b[::-1]))
  # print (c)
  c = c.rstrip("0")
  print(c[::-1])
