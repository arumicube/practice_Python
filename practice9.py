'''
import sys
input=sys.stdin.readline
#위의 코드를 사용해야 시간이 단축된다고 한다..
#이렇게 안하면 sort했을 때 시간초과로 실패
num=int(input())
arr=[0]*num
for i in range(num):
    arr[i]=int(input())
arr.sort()
for j in range(num):
    print(arr[j])


#이름과 나이 나이순으로 정렬하기
num=int(input())
str1=[]
for i in range(num):
    #str1[i]=list(map(str,input().split())) #str1[i]를 또 리스트로 나누어서 정렬 즉, 2차원,3차원.... 가능해짐
    #이렇게 쓰면 불법임!! (인데스 에러) 밑처럼 써야함
    str1.append(list(map(str,input().split())))
    #append는 파이썬 리스트(list)의 메서드로, 리스트의 끝에 새로운 요소를 추가할 때 사용됩니다. 
    #이 메서드는 리스트를 수정하며, 리스트의 크기를 증가시킵니다.
str1.sort(key=lambda x : int(x[0])) 
#sort(key=??)는 key값을 기준으로 정렬한다. 즉, 밑과 같다.
#lambda x : <> 는 함수와 마찬가지로 x는 인수, <>의 내용을 기준으로 정렬한다는 뜻이다.
for j in range(num):
    print(str1[j][0],str1[j][1])


#벌집 퀴즈
#1층에 1개 2층에 6개(7호) 3층에 12개(19호) 4층에 18개(37호) ---
#수열 식을 구해야한다.
#이산수학 식에 의하면 점화관계식 a=3n(n+1)+1이다. 또는 An+1=An+6*n
floor=1
num=int(input())
while True:
    if(floor==1):
        num=num-(floor-1)*6-1
    else:
        num=num-(floor-1)*6
    if(num>0):
        floor+=1
    elif(num==0):
        break
    else:
        break
print(floor)
'''
def Factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*Factorial(n-1)

num=int(input())
Fac=Factorial(num)
cnt=0
while (Fac%10 == 0):
    cnt+=1
    Fac=Fac//10
print(cnt)