'''
A,B = input().split()
A=int(A)
B=int(B)
#노가다 위험성 그러므로 A,B=map(int,input().split())
if(A<B):
    print('<')
if(A>B):
    print('>')
if(A==B):
    print('==')

A=input()
A=int(A)
for i in range(1,A+1):
    for j in range(i):
        print("*",end ="")
        #파이썬에서 print는 기본적으로 다음 줄에 출력되므로 end =""을 사용해야한다. 
    print() #다음줄이라는 의미
    '''
    
'''
#최댓값 찾기
a=[0]*9
for k in range(9):
    a[k]=int(input())
max1=max(a)
print(max1)
for i in range(9):
    if(a[i]==max1):
        print(i+1)
'''
A = int(input())
for i in range(A):
    print(i+1)