'''검증수 구하기
number =input().split()
for k in range(5):
    number[k]=int(number[k])
sum=0
for i in range(len(number)):
    sum +=(number[i]*number[i])
sum = sum%10
print(sum)
#의문점: 대체 map은 어디에 쓰이는거지 string에는 못쓰나...? 뭔소리지 공부
'''

''' 사용된 숫자 개수 맞추기
A=int(input())
B=int(input())
C=int(input())
mul = A*B*C
#len은 int에서 불가능
def jaritsu(n):
    ans =0
    while n:
        # 0일 때 0 의 자리수가 나와야하므로
        n //=10 #이때 n이 false라면 실패 굿
        ans +=1
    return ans
cnt=[0]*10
jari =jaritsu(mul)
for i in range(jari):
    p=int(mul%10)
    cnt[p] +=1
    mul //=10
for j in range(10):
    print(cnt[j])
    '''
    
''' A+B-C
A=input()
B=input()
C=input()
print(int(A)+int(B)-int(C))
print(int(A+B)-int(C)) # -(뺴기)의 경우 문자열에서 빠지는게 아니고 '수'로밖에 계산이 안된다.
'''
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")
print("      |")
print("      |")
#중요!! \을 출력하려면 \\ 필요함 이거는 금액권(W) 기호와 같다.
#중요!! "을 출력하려면 \" 필요함 즉 백슬래쉬(W)
