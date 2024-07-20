'''
#num 만큼 문자열 반복 근데 문제 설명이 좀 잘못된듯
T=int(input())
for i in range(T):
    num, str1=input().split()
    num=int(num)
    for k in range(len(str1)):
        print(str1[k]*num,end="")
    print()

#구구단
gugudan=int(input())
for i in range(1,10): #즉, 1-9
    sum=int(gugudan*i)
    print(gugudan,"*", i,"=",sum)

#시험성적
grade=int(input())
if(grade>=90 and grade<=100): 
    print("A")
elif(grade>=80):
    print("B")
elif(grade>=70):
    print("C")
elif(grade>=60):
    print("D")
else:
    print("F")

#사칙연산
A, B=map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B) #/은 float //은 int
print(A%B)

#작은 수 찾기
N, X=map(int,input().split())
A=[0]*N
A=input().split()
for i in range(N):
    if(int(A[i])<X):
        print(A[i],end=" ")
'''
'''
#덧셈1
T= int(input())
for i in range(T):
    A, B=map(int,input().split())
    print(A+B)
'''
#A+B -4 중요 문제 새로운 개념!!
while True:
    try:
        A, B=map(int,input().split())
        print(A+B)
    except:
        break
#try,except/else/finally
try:
    #예외가 발생할 수 있는 코드
    print(int(A))
except:
    #try 코드에서 오류가 났을 떄 처리한다.
    print("오류났어요")
else:
    #예외가 아예 발생하지 않았을 때
    print("오류 안남")
finally:
    #예외 발생 알빠노? 걍 무조건 실행되는 코드
    print("실행 완료!")