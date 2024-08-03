import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    # 이건 안됨: arr[i][0],arr[i][1]=map(int,sys.stdin.readline().split())
    #젠장 또 append야
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x, y))
arr.sort(key=lambda x:x[1])
arr.sort(key=lambda x:x[0]) #걍 11651 이랑 반대로 정렬, 그리고 정렬하려는 조건의 반대로 하면 됨!
for j in range(N):
    print(arr[j][0],end=" ")
    print(arr[j][1])