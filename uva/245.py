# Determines input read criterion
from sys import stdin
import re
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("245.txt", "r")
else:
 inputSrc = stdin
 
def check_digit(word_,words):
  strng=""
  res = re.findall( r'\w+|[^\s\w]+',word_)
  for word in range(len(res)):
    if res[word].isdigit():
      word1=words[-int(res[word])]
      words.insert(len(words)-1, words.pop(words.index(word1)))
      res[word]=word1
    elif res[word].isalpha():
      words.append(res[word])
  strng="".join(res)
  return words,strng

words=[]
while True:
  lst=[]
  compressed_file=inputSrc.readline().rstrip()
  x=len(compressed_file) - len(compressed_file.lstrip())
  if compressed_file == "0":
    break
  compressed_file=compressed_file.split()
  for i in range(len(compressed_file)):
    words,strng=check_digit(compressed_file[i],words)
    lst.append(strng)
  print (x*" "+" ".join(lst))
  # lst1=[]
  # for i in range(len(compressed_file1)):
  #   count=0
  #   if not compressed_file1[i] == " ":
  #     output+=compressed_file1[i]
  #   else:
  #     count+=1
  #   lst1.append(count)
  # print (lst1)
  # for i in range(len(compressed_file)):
  #   words,strng=check_digit(compressed_file[i],words)
  #   lst.append(strng)
  # print (x*" "+" ".join(lst))
  #
  #
    
  #   words,strng=check_digit(compressed_file[i],words)
  #   lst.append(strng)
  # print (x*" "+" ".join(lst))
