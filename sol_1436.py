import sys
N=int(sys.stdin.readline())
cnt=0
som=666
while True: #만약에 2면 1666이 나와야함
    if '666' in str(som): #1665일 때 X 1666일 때 cnt=2
        cnt+=1 #cnt=1
    if cnt==N: #1666이므로 프린트해야댐 
        print(som)
        break
    som +=1 #걍 무조건 노가다로 667,668... 비교