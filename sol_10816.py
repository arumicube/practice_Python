import sys
N=int(sys.stdin.readline())
n1=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
m1=list(map(int,sys.stdin.readline().split()))
cnt_dict={} #사전(계차 수열 이였나..) 초기화 방법: [] 아니고, {}임
#.count = 시간초과
for num in n1:
    if num in cnt_dict:
        cnt_dict[num] += 1
    else:
        cnt_dict[num] = 1
#이게 어떻게 가능하지...??????

for j in m1:
    if j in cnt_dict:
        print(cnt_dict[j],end=" ")
    else:
        print(0,end=" ")