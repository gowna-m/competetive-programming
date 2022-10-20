# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("750.txt", "r")
else:
 inputSrc = stdin
 

def isSafe(board, row, col):
	for i in range(col):
		if (board[row][i]):
			return False
	i = row
	j = col
	while i >= 0 and j >= 0:
		if(board[i][j]):
			return False
		i -= 1
		j -= 1

	i = row
	j = col
	while j >= 0 and i < 8:
		if(board[i][j]):
			return False
		i = i + 1
		j = j - 1

	return True

def solveNQUtil(board, col):
  if (col == 8):
    v = []
    for i in board:
      for j in range(len(i)):
          if i[j] == 1:
            v.append(j+1)
    result.append(v)
    return True

  res = False
  for l in range(8):
    if (isSafe(board,l , col)):
      board[l][col] = 1
      res = solveNQUtil(board, col + 1) or res
      board[l][col] = 0
  return res

def solveNQ(n):
  result.clear()
  board = [[0 for o in range(n)]for m in range(n)]
  solveNQUtil(board, 0)
  result.sort()
  return result

while True:
  result = []
  inp=inputSrc.readline().strip()
  if len(inp) == 0:
    break
  num_datasets=int(inp)
  print ("SOLN      COLUMN")
  for _ in range(num_datasets):
    inputSrc.readline().strip()
    r,c=list(map(int,inputSrc.readline().strip().split()))
    n = 8
    res = solveNQ(n)
    # print (res)
    
    print (" #     "+" ".join(str(p+1) for p in range(n)))
    print ()
    cnt=0
    for k in range(len(res)):
      
      if res[k][0] == r:
        cnt=cnt+1
        print (" "+str(cnt)+"     "+" ".join(str(g) for g in res[k]))
        
    print ()
