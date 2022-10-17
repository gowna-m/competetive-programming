# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("706.txt", "r")
else:
 inputSrc = stdin
 
edges={"0":[1,2,3,5,6,7],"1":[3,6],"2":[1,3,4,5,7],
"3":[1,3,4,6,7],"4":[2,3,4,6],"5":[1,2,4,6,7],"6":[1,2,4,5,6,7],
"7":[1,3,6],"8":[1,2,3,4,5,6,7],"9":[1,2,3,4,6,7]}

def compute(output,idx,digit,width,edges):
  # print (idx,digit,width)
  start = idx*(width+2) + idx
  for edge in edges[digit]:
    if edge == 1:
      output[0][start+1:start+1+width] = ['-']*width
    elif edge == 2:
      for i in range(1, width+1):
        output[i][start] = "|"
    elif edge == 3:
      for i in range(1, width+1):
        output[i][start+1+width] = "|"
    elif edge == 4:
        output[width+1][start+1:start+1+width] = ['-']*width
    elif edge == 5:
      for i in range(1, width+1):
        output[i + width+1][start] = "|"
    elif edge == 6:
      for i in range(1, width+1):
        output[i + width+1][start+1+width] = "|"
    elif edge == 7:
      output[2*width+2][start+1:start+1+width] = ['-']*width
    
  return output
  
def main():
  s,num=inputSrc.readline().strip().split()
  s=int(s)
  while s!=0 or num!="0":
    num_len=len(num)*(s+2)+len(num)-1
    num_rows=2*s+3
    output = [[" "]*(num_len) for i in range(num_rows)]
    # print (output)
    for k,digit in enumerate(num):
      result=compute(output,k,digit,s,edges)
    print ("\n".join(["".join(r) for r in result])+"\n")
    # print ("\n")
    s,num=inputSrc.readline().strip().split()
    s=int(s)
    
    
if __name__ == "__main__":
    main()
  # print("-----",s,num)
