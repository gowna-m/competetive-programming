# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("727.txt", "r")
else:
 inputSrc = stdin

operators = set(['+', '-', '*', '/', '(', ')'])
priority = {'+':1, '-':1, '*':2, '/':2, '^':3}
n=int(inputSrc.readline().strip())
inputSrc.readline().strip()
for i in range(n):
  stack=[]
  postfix=""
  infix=inputSrc.readline().strip()
  # print (infix)
  while len(infix) != 0:
    if infix not in operators:
      postfix+=infix
    elif infix == "(":
        stack.append(infix)
    elif infix == ")":
      while stack and stack[-1]!= '(':
        postfix+=stack.pop()
      stack.pop()
    else:
      while stack and stack[-1]!='(' and priority[infix]<=priority[stack[-1]]:
          postfix += stack.pop()
      stack.append(infix)
    infix=inputSrc.readline().strip()
  while stack:
    postfix+=stack.pop()
  print (postfix)
  print ()
 
      
    
    
  
