# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("514.txt", "r")
else:
 inputSrc = stdin

while True:
  inp=inputSrc.readline().strip()
  # print (inp)
  if inp == "0":
    break
  n = int(inp)
  in_seq = [i+1 for i in range(n)]
  l=inputSrc.readline().strip()
  # print (l)
  while l!="0":
    out_seq = list(map(int,l.split()))
    # print (out_seq)
    allowed=True
    out_=0
    in_=0
    stack=[]
    while out_< n:
      if in_ < n and in_seq[in_] == out_seq[out_]:
        # print ("hhhhhhhhhhhhhhh",in_)
        in_+=1
        out_+=1
        
      elif len(stack) > 0 and stack[-1] == out_seq[out_]:
        # print ("qqqqqqqqqqqqq",stack)
        stack.pop()
        out_+=1
      else:
        if in_ < n:
          stack.append(in_seq[in_])
          # print (stack)
          in_+= 1
        else:
          allowed=False
          break
    
    if allowed:
      print ("Yes")
    else:
      print ("No")
    l=inputSrc.readline().strip()
  print()
