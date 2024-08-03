import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    # 이건 안됨: arr[i][0],arr[i][1]=map(int,sys.stdin.readline().split())
    #젠장 또 append야
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:x[1])
for j in range(N):
    print(arr[j][0],end=" ")
    print(arr[j][1])