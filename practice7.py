'''
A, B=map(int,input().split())
if(A>=B):
    A,B=B,A
A1=A
while True: #최대공약수
    #3과 6일 경우를 생각하여 A1-=1을 뒤에 배치
    if(B%A1==0 and A%A1==0):
        print(A1)
        break
    A1 -=1
    if(A1==1):
        print(1)
        break
A2=A//A1
B2=B//A1
print(A1*A2*B2) #최소공배수
'''
'''
#위의 방법은 너무 비효율적임 공식을 써주겠음
A, B=map(int,input().split())
if(A>=B):
    A,B=B,A

def gcd(x,y):
    while y: #즉, y가 0만 아니면 성립
        x,y=y,x%y 
        # if 3,6 -> 6,3 -> 3,0 ->y=0이므로 x=3 외우셈 ㅋㅋ
        # if 7,5 -> 5,2 -> 2,1 -> 1,0 -> y=0이므로 x=1
    return x
gcd_value=gcd(A,B)
print(gcd_value)
print((A*B)//gcd_value) #최소공배수 공식임 외우셈 3*6=18/3 =6, 24*18//6=24*3= 72 오 ㅋㅋ 외우셈 공식임 
'''
'''
#시간초과로 실패
N=int(input())
num=list(map(int,input().split()))

cnt=0
div=2
for i in range(N):
    while True:
        if(num[i]==1):
            break
        if(num[i]%2==0):
            break
        div+=1
        if(num[i]%div==0):
            break #continue 하면 while문이 div++되지 않고 무한반복되므로 빠져나오는 break 필요
    if div==num[i]:
        cnt +=1
print(cnt)
'''
'''
#올바른 소수 판별법
import math
N = int(input())
num = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if num[i] == 1:
        continue
    is_prime = True #1이 아니면 일단 소수로 친다.
    for j in range(2, int(math.sqrt(num[i]))+1): #2부터 어떤 수의 제곱근까지만 계산하면 된다.
        #참고:https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-1978-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0python
        if num[i] % j == 0:
            is_prime = False
            break
    if is_prime: #true가 유지된다면
        cnt += 1

print(cnt)
'''
#부녀회장 문제 2775번
#참고:https://ooyoung.tistory.com/89
#문제 이해부터! T=2 (2개 가구) 
# 1 3(1층 3호) 0층 1+2+3호
# 2 3(2층 3호) 1층 1+2+3호
T=int(input())
#f0의 초기화는 매번 필요함
for i in range(T):
    floor=int(input())
    Ho=int(input())
    f0=[x for x in range(1,Ho+1)] #헐.. 즉, f0[0]=1이라는 소리임..!
    #헷갈리지말기!!!!!
    for j in range(floor): #2층이면 1층의 사람들만/ 근데 1층은 0층이 필요하므로 초기화 필요
        for k in range(1,Ho): #1~Ho 3호라면 1~2까지
            f0[k] += f0[k-1] #1층은 1,3,6(3+3),10(4+6),15
    print(f0[-1])