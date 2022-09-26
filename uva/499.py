# Determines input read criterion
from sys import stdin
from collections import Counter
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("499.txt", "r")
else:
 inputSrc = stdin

while True:
  line=inputSrc.readline().strip()
  if len(line) == 0:
    break
    
  line = line.replace(' ','')
  res = Counter(line)
  max_value = max(res.values())
  keys_=[k for k,v in res.items() if v == max_value]
  # print (keys_)
  upper=""
  lower=""
  if len(keys_) > 1:
    for i in range(len(keys_)):
      if ord(keys_[i]) >=65 and ord(keys_[i]) <= 90:
        upper+=keys_[i]
      else:
        lower+=keys_[i]
    print (upper,lower)
    print ("".join(sorted(upper)+sorted(lower))+ " "+ str(max_value))
  else:
    print ("".join(keys_)+ " "+ str(max_value))
  # print ("Count of all characters in"+  str(res))
  # print ("".join(keys_))
  # print ("".join(sorted("".join(keys_),key=str.upper)) + " "+ str(max_value))
