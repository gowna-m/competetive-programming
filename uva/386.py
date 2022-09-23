import math

def is_perfect_cube(number):
  number = abs(number)
  return round(number ** (1 / 3)) ** 3 == number
  
for i in range(6,201):
  ot_lst=[]
  cube1=i*i*i
  for j in range(3,i):
    cube2=j*j*j
    for k in range(j+1,i):
      cube3=k*k*k
      diff=cube1-cube2-cube3
      if diff <=1:
        break
      if is_perfect_cube(diff):
        res=round(diff ** (1 / 3))
        a=tuple(sorted((j,k,res)))
        ot_lst.append(a)
  result=list(set(ot_lst))
  result.sort()
  # print (result)
  if len(result) != 0:
    for x in result:
      print ("Cube = " +str(i)+", Triple = ("+str(x[0])+","+str(x[1])+"," +str(x[2])+ ")")
