# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("344.txt", "r")
else:
 inputSrc = stdin
 
roman_numerals={1:"i",2:"ii",3:"iii",4:"iv",5:"v",6:"vi",7:"vii",8:"viii",9:"ix",10:"x",20:"xx",30:"xxx",40:"xl",50:"l",60:"lx",70:"lxx",80:"lxxx",90:"xc",100:"c"}

while True:
  num_prefix_pages=int(inputSrc.readline().strip())
  if num_prefix_pages == 0:
    break
  page=""
  for i in range(1,num_prefix_pages+1):
    if i % 10 > 0 and i // 10 > 0:
      div = i // 10
      page+=str(roman_numerals[div * 10]) + str(roman_numerals[i % 10])
    else:
      page+=roman_numerals[i]
  print (str(num_prefix_pages)+": "+str(page.count("i"))+" i,"+" "+str(page.count("v"))+" v,"+" "+str(page.count("x"))+" x,"+" "+str(page.count("l"))+" l,"+" "+str(page.count("c"))+" c")
    
