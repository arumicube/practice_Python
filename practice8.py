'''
#펠린드롬수

while True:
    pel=input() #string인 상태
    is_pel=True
    if(int(pel)==0):
        break
    for i in range(len(pel)//2):
        if pel[i]!=pel[len(pel)-1-i]:
            is_pel=False
    if(is_pel):
        print("yes")
    if is_pel==False:
        print("no")

#이항계수 n!/((n-k)!k!) 즉 조합
def Factorial(p):
    result=1
    if(p==0 or p==1):
        return 1
    else:
        result = p*Factorial(p-1) #p* 를 틀림!! 까먹지 말기 result *=Fac 아님!!
    return result

N,K=map(int,input().split())
if(K<=N and N<=10):
    nCk=Factorial(N)//(Factorial(N-K)*Factorial(K))
    print(nCk)
'''
#-------------------------------------#
import sys
input=sys.stdin.readline #이건 또 뭐야.. 근데 이거 없으면 채점이 걍 안됨.... 
#----------------모름------------------#
#참고 https://kill-xxx.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0

N=int(input())
num=[0]*(10000+1) #최대 입력수
#for i in range(N):
#    num[i]=int(input()) 뒤에서 input을 해줄거기 때문에 피료없
# num.sort() #알아서 정렬 파이썬 사랑해 근데 메모리 초과 오류!
for j in range(N):
    num[int(input())] +=1 #입력받은 값의 인덱스를 +1로 저장
    #그럼 5 5 일때는..?
for k in range(len(num)):
    if(num[k]!=0): #즉, 1이면
        for q in range(num[k]): #인덱스의 숫자만큼 개수 출력
            print(k)

'''
#참고 https://www.daleseo.com/sort-bubble/
for k in range(N):
    for q in range(N-k-1): #버블 솔트 구현 (gpt 베낌) 외우기!!
        #이미 정렬된 부분은 무시 하므로 k=0일 떄(시작) 0~8
        if num[q]>num[q+1]: #결국 제일 큰 값이 뒤로 갈수밖에 없다. (정렬됨)
            num[q],num[q+1]=num[q+1], num[q]
''' #버블정렬도 메모리 초과라고...?

