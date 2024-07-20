'''
#분해합 존나 모르겠음!!!
M=int(input())
# 원래의 M=N+(N//1)%10+(N//10)%10+(N//100)%10 . . .근데 파이썬은 이렇게 안해도됨!!
for i in range(1,M+1): #1부터 M까지의 분해합을 모두 비교
    num=sum(map(int,str(i))) #[i]아님 (i)를 str화 시키면 각 자릿수가 [0][1][2]...에 저장 그러므로 num=각자릿수총합
    result=num+i #각자릿수 총합 + 숫자 그자체
    if(result == M): #분해합 = 구하기 원하는 수
        print(i) #i는 가장 작은 자연수부터 시작하므로 가장 작은 분해자를 구할 수 있다.
        break
    if(i==M): #끝났으면
        print(0)

#티셔츠 펜 주문
N=int(input())
S,M,L,XL,XXL,XXXL = map(int, input().split()) #int(input.split)는 안됨 map의 중요성
sum1=[S,M,L,XL,XXL,XXXL]
sumT=0
T, P = map(int, input().split())
if(N==(S+M+L+XL+XXL+XXXL)):
    for i in range(6):  #몇묶음 필요할까?
        sumT=sumT+(sum1[i]+T-1)//T
        
        
        #이건 왜 틀렸을까?
        if(sum1[i]<=T): #여기서 sum[i]가 0일 경우를 생각 안함!!!!!
            sumT+=1
        else:
            if(sum1[i]%T!=0):
                sumT=sumT+ sum1[i]//T +1
            else: 
                sumT=sumT+sum[i]//T
        
print(sumT)
print(N//P,N%P)
'''
N=int(input())
grade=list(map(int,input().split())) #map을 이용하여 list에 집어넣는다!
M=max(grade)
for n in range(N): #문제 잘못이해함.. 그냥 최고점을 100점으로 만들어버리는거였음....
    grade[n]=grade[n]/M*100
average=sum(grade)/N
print(average)
