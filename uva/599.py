# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
#INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("599.txt", "r")
else:
 inputSrc = stdin
 
num_cases = int(inputSrc.readline().strip())
for c in range(num_cases):
  forest = [-1] * 26
  partition_id = 0
  while True:
    line = inputSrc.readline().strip()
    print (line)
    if line[0] == "*":
      line = inputSrc.readline().strip().split(",")
      
      # Report here
      print (forest)
      print (len(line))
      print (sum(x > 0 for x in forest))
      print (set(forest))
      num_acorns = len(line) - sum(x > 0 for x in forest)
      num_trees = len(set(forest)) - 1
      print("There are {} tree(s) and {} acorn(s).".format(num_trees, num_acorns))
      break
    else:
      print (line[1])
      u = ord(line[1]) - ord('A')
      v = ord(line[3]) - ord('A')
      print (u,v)
      if forest[u] == -1:
        if forest[v] == -1:
          partition_id += 1
          forest[u] = forest[v] = partition_id
        else:
          forest[u] = forest[v]
      else:
        if forest[v] == -1:
          forest[v] = forest[u]
        else:
          temp = forest[u]
          for i in range(len(forest)):
            if forest[i] == temp:
              forest[i] = forest[v]
