import sys
input=sys.stdin.readline
N=int(input())
XY=[]
cnt=[1]*N
for _ in range(N):
    x, y = map(int, input().split())
    XY.append((x, y))
for i in range(N):
    for j in range(N):
        if(XY[i][0]<XY[j][0]) and(XY[i][1]<XY[j][1]):
            cnt[i] +=1
for k in range(N):
    print(cnt[k],end=" ")