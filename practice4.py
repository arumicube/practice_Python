'''
#A+B -5
while True:
    A,B=map(int,input().split())
    if(A==0 and B==0):
        break
    print(A+B)

#아스키 코드 출력
ASCII=input()
print(ord(ASCII))
#아스키 코드 사용법 ord("A") or chr(65)

#몇번째 문자열 출력
str1=input()
strnum=int(input())
print(str1[strnum-1])

#num개 숫자 입력 후 각자릿수의 합
num=int(input())
sumNum=int(input())
sum=0
for i in range(num):
    divide=sumNum%10
    sum += divide
    sumNum //=10
print(sum)

#최대최소구하기
num=int(input())
str1=[0]*num
str1=list(map(int,input().split()))

max=str1[0]
min=str1[0]
for i in range(num):
    if(str1[i]>max):
        max=str1[i]
    if(str1[i]<min):
        min=str1[i]
print(min,max)

#45분 일찍 알람맞추기
A, B=map(int,input().split())
if(B<45):
    B +=15
    if(A==0):
        A=23
    else:
        A-=1
elif(B>45):
    B -=45
else:
    B=0
        
print(A,B)
'''