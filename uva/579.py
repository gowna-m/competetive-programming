# Determines input read criterion
from sys import stdin
JUDGE = 0
FILE = 1
# INPUT_SRC = FILE
INPUT_SRC = JUDGE
if INPUT_SRC == FILE:
 inputSrc = open("579.txt", "r")
else:
 inputSrc = stdin
 
def main():
  while True:
    clock=inputSrc.readline().strip()
    if clock=="0:00":
        break
    h,m=[int(v) for v in clock.split(':')]
    h_angle = h*30+m*0.5
    m_angle = m*6
    diff_angle = abs(h_angle - m_angle)
    result=diff_angle if diff_angle <=180 else 360-diff_angle
    print ("{:.3f}".format(result))

if __name__ == '__main__':
    main()
