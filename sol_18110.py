import sys
input=sys.stdin.readline
N=int(input())
Avg=[]
if N==0:
    print(0)
if(N>0):
    for i in range(N):
        Avg.append(int(input().strip()))
#1. Avg sort
#2. 걍 append하지말고 계차수열(사전)에 더해버린다.
    Avg.sort()
    julsa=round(N*(0.15))
    for j in range(julsa):
        Avg.pop(0) #맨앞
    for k in range(julsa):
        Avg.pop() #맨뒤
    sum=0
    for p in Avg:
        sum+=p
    print(round(sum/len(Avg)))