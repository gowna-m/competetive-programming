# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
INPUT_SRC = FILE
# INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("397.txt", "r")
else:
 inputSrc = stdin

operators =["*","/","+","-"]
eqn = inputSrc.readline().strip()

tmp_eqn=[]
tmp_eqn1=[]
flag=0
while eqn!=None and len(eqn)!=0:
   
  lhs,rhs=eqn.split("=")
  if " " in lhs:
    lhs=lhs.split()
    for m in range(len(lhs)):
      if len(lhs[m]) > 1 and lhs[m][1].isdigit() and lhs[m][0] == "+":
        lhs[m]=lhs[m][1:]
    # print (lhs)
    flag=0
    print (" ".join(lhs) + " =" + rhs)
  else:
    lst=[]
    strn=lhs
    for i in range(0,len(strn)-1):
      if i==0:
        if strn[i] in operators:
          lst.append(strn[0]+strn[1])
        else:
          lst.append(strn[0])
      else:
        if strn[i] in operators and strn[i+1] in operators:
          lst.append(strn[i])
          if strn[i+1] == "-":
            lst.append(strn[i+1]+strn[i+2])
          else:
            lst.append(strn[i+2])
        elif strn[i-1].isdigit() and strn[i] in operators and strn[i+1].isdigit():
          lst.append(strn[i+1])
    lhs=lst
    flag=1
    print (" ".join(lhs)+ " = " + rhs)
  tmp_eqn=lhs.copy()
  idx=0
  n=0
  
  for i in range(1,len(lhs)-1):
    if lhs[i] == operators[0] or lhs[i] == operators[1]:
      if lhs[i] == operators[0]:
        result=int(lhs[i-1])*int(lhs[i+1])
      elif lhs[i] == operators[1]:
        result=int(lhs[i-1])//int(lhs[i+1])
      idx=tmp_eqn.index(lhs[i])
      tmp_eqn[idx+1]=str(result)
      del tmp_eqn[idx-1:idx+1]
      lhs[i],lhs[i+1],lhs[i-1]=str(result),str(result),str(result)
      if flag ==1:
        print (" ".join(tmp_eqn)+ " = "+str(rhs))
      else:
        print (" ".join(tmp_eqn)+ " ="+str(rhs))
      if len(tmp_eqn) <=3:
        if tmp_eqn[1] in operators:
          if tmp_eqn[1] == operators[0]:
            result=int(tmp_eqn[0])*int(tmp_eqn[2])
          elif tmp_eqn[1] == operators[1]:
            result=int(tmp_eqn[0])//int(tmp_eqn[2])
          elif tmp_eqn[1] == operators[2]:
            result=int(tmp_eqn[0])+int(tmp_eqn[2])
          elif tmp_eqn[1] == operators[3]:
            result=int(tmp_eqn[0])-int(tmp_eqn[2])
        if flag == 1:
          print (str(result) + " = " +str(rhs))
        else:
          print (str(result) + " =" +str(rhs))
        break
  tmp_eqn1=tmp_eqn.copy()
  for k in range(1,len(tmp_eqn)-1):
    if tmp_eqn[k] == operators[2] or tmp_eqn[k] == operators[3]:
      if tmp_eqn[k] == operators[2]:
        result=int(tmp_eqn[k-1])+int(tmp_eqn[k+1])
      elif tmp_eqn[k] == operators[3]:
        result=int(tmp_eqn[k-1])-int(tmp_eqn[k+1])
      idx=tmp_eqn1.index(tmp_eqn[k])
      tmp_eqn1[idx+1]=str(result)
      del tmp_eqn1[idx-1:idx+1]
      tmp_eqn[k],tmp_eqn[k+1],tmp_eqn[k-1]=str(result),str(result),str(result)
      if flag == 1:
        print (" ".join(tmp_eqn1)+ " = "+str(rhs))
      else:
        print (" ".join(tmp_eqn1)+ " ="+str(rhs))
      if len(tmp_eqn1) <=3:
        if tmp_eqn1[1] in operators:
          if tmp_eqn1[1] == operators[0]:
            result=int(tmp_eqn1[0])*int(tmp_eqn1[2])
          elif tmp_eqn1[1] == operators[1]:
            result=int(tmp_eqn1[0])//int(tmp_eqn1[2])
          elif tmp_eqn1[1] == operators[2]:
            result=int(tmp_eqn1[0])+int(tmp_eqn1[2])
          elif tmp_eqn1[1] == operators[3]:
            result=int(tmp_eqn1[0])-int(tmp_eqn1[2])
        if flag == 1:
          print (str(result) + " = " +str(rhs))
        else:
          print (str(result) + " =" +str(rhs))
        break

  eqn = inputSrc.readline().strip()
  if eqn!=None and len(eqn)!=0:
    print()
