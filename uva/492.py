# Determines input read criterion
from sys import stdin
from string import punctuation
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("492.txt", "r")
else:
 inputSrc = stdin

vowels=["a","e","i","o","u"]
consonants=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
punctuations='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

inp=inputSrc.readline().strip()
while inp!=None and len(inp)!=0:
  result=""
  inp=inp.split()
  for i in range(len(inp)):
    if inp[i].isalpha():
      if inp[i][0].isupper():
        if inp[i][0].lower() in vowels:
          result+=inp[i] + "ay"
        else:
          result+=inp[i][1:]+inp[i][0]+"ay"
    
      elif inp[i][0].islower():
        if inp[i][0] in vowels:
          result+=inp[i] + "ay"
        else:
          result+=inp[i][1:]+inp[i][0]+"ay"
    elif inp[i] in punctuations:
      result+=inp[i]
    else:
      if inp[i][-1] in punctuations:
        if inp[i][0].isupper():
          if inp[i][0].lower() in vowels:
            result+=inp[i][:len(inp[i])-1] + "ay" + inp[i][-1]
          else:
            result+=inp[i][:len(inp[i])-1]+inp[i][0]+"ay"+inp[i][-1]
      
        elif inp[i][0].islower():
          if inp[i][0] in vowels:
            result+=inp[i][:len(inp[i])-1] + "ay" + inp[i][-1]
          else:
            result+=inp[i][:len(inp[i])-1]+inp[i][0]+"ay"+inp[i][-1]
      else:
        if inp[i][0].isupper():
          if inp[i][0].lower() in vowels:
            result+=inp[i] + "ay"
          else:
            result+=inp[i][1:]+inp[i][0]+"ay"
      
        elif inp[i][0].islower():
          if inp[i][0] in vowels:
            result+=inp[i] + "ay"
          else:
            result+=inp[i][1:]+inp[i][0]+"ay"
        else:
          result+=inp[i]

    result+=" "
  
  print (result)
  inp=inputSrc.readline().strip()
  
