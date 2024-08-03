#요세푸스 순열
#(7,3) = <3,6,2,7,5,1,4>
# 1. pop함수 사용하면 되지 않을까?
import sys
N,K=map(int,sys.stdin.readline().split())
arr=[]
arr2=[]
arr = list(range(1, N + 1))
'''
같은 표현이지만 비효율적
for i in range(N):
    arr.append(i+1)
'''
index=0
print("<",end="")
for j in range(N):
    index = (index + K - 1) % len(arr) #index= 지금 있는 위치
    #K번째니까 3이면 0,1,2 2번자리에 있어야하므로 마이너스1
    #근데 N에서 대가 끊겨버리므로 N과의 나머지 즉 8번쨰 자리면 1번째 자리
    arr2.append(arr.pop(index))
for k in range(N-1):
    print(arr2[k],end=", ")
print(arr2[N-1],end=">")