# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("488.txt", "r")
else:
 inputSrc = stdin
 
num_tests = int(inputSrc.readline().strip())

for i in range(num_tests):
  inputSrc.readline().strip()
  amp = int(inputSrc.readline().strip())
  freq = int(inputSrc.readline().strip())
  for j in range(freq):
    for t in range(1, amp + 1):
        print(str(t)*t)
    for t in range(amp-1, 0, -1):
        print(str(t)*t)
    if not (i == num_tests - 1 and j == freq - 1):
      print()
