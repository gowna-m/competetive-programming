# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("673.txt", "r")
else:
 inputSrc = stdin


def process(string):
  stack = []
  for i in string:
    if i in "([":
        stack.insert(0, i)
        # print (stack)
    else:
      if len(stack) == 0:
        return "No"
      x = stack.pop(0)
      if i == ")" and x != "(":
        return "No"
      elif i == "]" and x != "[":
        return "No"

  if len(stack) > 0:
    return "No"
  return "Yes"
  
n=int(inputSrc.readline().strip())
for i in range(n):
  text=inputSrc.readline().strip()
  print(process(text))
