# Determines input read criterion
from sys import stdin
import collections
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("612.txt", "r")
else:
 inputSrc = stdin

num_datasets=int(inputSrc.readline().strip())
inputSrc.readline().strip()
for n in range(num_datasets):
  string_lst=[]
  string_len,num_strings=list(map(int,inputSrc.readline().strip().split()))
  for i in range(num_strings):
    string=inputSrc.readline().strip()
    string_lst.append(string)
  # print (string_lst)
  dct={}
  for k in range(num_strings):
    a,c,g,t=[],[],[],[]
    cnt=0
    # print (string_lst[k])
    for chr_idx in range(string_len):
      if string_lst[k][chr_idx] == "A":
        a.append(chr_idx)
      if string_lst[k][chr_idx] == "C":
        c.append(chr_idx)
      if string_lst[k][chr_idx] == "G":
        g.append(chr_idx)
      if string_lst[k][chr_idx] == "T":
        t.append(chr_idx)
  
    # print (a,c,g,t)
    lst_c_a=a+c
    lst_g_c_a=a+c+g
    for i in c:
      for l in a:
        if l > i:
          cnt+=1
    for i in g:
      for l in lst_c_a:
        if l > i:
          cnt+=1
    for i in t:
      for l in lst_g_c_a:
        if l > i:
          cnt+=1
    # print (string_lst[k],cnt)
    dct[string_lst[k]]=cnt
  print (dct)
  res=list(dct.values())
  res.sort()
  print (res)
  inv_dict = {value:key for key, value in dct.items()}
  
  duplicates=[item for item, count in collections.Counter(res).items() if count > 1]
  for val in res:
    if val in duplicates:
      print(inv_dict[val])
  # print (dct[9])
  ak=sorted(dct.items(), key=lambda x: x[1])
  print (ak)
  mx = max(dct.values())
  res=[k for k, v in dct.items() if v == mx]
  ak = sorted(dct.items(), key=lambda x: x[1])
  print (ak)
  
  for res in ak:
    print (res[0])
  inputSrc.readline().strip()
  # if n!=num_datasets-1:
  #   print ()
    # for key,value in dct.items
