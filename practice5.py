'''
#음계
Piano=[0]*8
Piano=input().split()
for i in range(8):
    Piano[i]=int(Piano[i])
#Piano.sort() 와 Piano.reverse()는 정렬을 직접 수정해서.. 반환값이 없음. 
#나의 오류1: sortPiano=Piano.sort()
#나의 오류2: rePiano=sortPiano.reverse()
sortPiano=[1,2,3,4,5,6,7,8]
rePiano=[8,7,6,5,4,3,2,1]
if(Piano == sortPiano):
    print("ascending")
elif(Piano == rePiano):
    print("descending")
else:
    print("mixed")

#42로 나눈 서로 다른 나머지의 개수
num=[0]*10
DivideNum=[0]*42 #0-41
cnt=0
for i in range(10):
    num[i]=int(input())
    div42=num[i]%42
    if(DivideNum[div42]==0):
        DivideNum[div42] = 1
for j in range(42):
    if(DivideNum[j]==1):
        cnt +=1
print(cnt)

#연속된 O의 개수로 점수 내기
num=int(input())
cnt=0
for i in range(num):
    OX=input() #OX[0]=H, OX[1]=E,OX[2]=L ~~ string는 한글자씩 배열에 저장, list는 한단어씩 배열에 저장
    if(OX[0]=='O'):
        grade=1
        cnt=1
    else:
        grade=0
    for j in range(1,len(OX)): #파이썬은 범위가 정확해야해서 임의의 80개 이런건 XX!!
        if(OX[j]=='O'):
            if(OX[j-1]=='O'):
                cnt+=1
                grade = grade+cnt
            if(OX[j-1]=='X'):
                cnt=1
                grade=grade+cnt
        if(OX[j]=='X'):
            cnt=0
    print(grade)

#호텔 방배정
T=int(input())
house=0
for t in range(T):
    H, W, N=map(int,input().split())
    if(N>=H):
        if(N%H !=0 ):
            house=(N%H)*100+(N//H)+1
        if(N%H==0):
            house=H*100+ (N//H) #얘한테는 +1 아님 주의!!!
    if(N<H):
        house=N*100+1
    print(house)
    
'''
''' 너무 복잡하게 생각한 것(실패)
#visited=[[0]*H]*W 필요 없을 것 같은데?
distance=[[0]*H]*W #이차원 배열 선언 방법
house=[[0]*H]*W
for h in range(H):
    for w in range(W):
        distance[h][w]=w+1
        house[h][w]=(h+1)*100+(w+1) #각 배열에 거리와 호수 할당
    #선호하는 곳: 101-201-301--- 102-202-302---
#N-1까지의 손님들을 모두 배정 후 N번째 손님 배정? or
#거리 계산만 하고 N번째 손님만 배정?
'''   
'''
#알파벳 순서찾기
Alpa=[-1]*26 #배열을 -1로 초기화한다
somunja=input()
for i in range(len(somunja)):
    if(ord(somunja[i])>=97 and ord(somunja[i])<123):
        num=ord(somunja[i])-ord('a')
        if(Alpa[num]==-1): #-1즉,초기화 되어있는 값이면 저장, 하지만 이미 저장된 값이라면 바꾸지 않는다.
            Alpa[num]=i  
for k in range(26):
    print(Alpa[k],end=" ") #띄어쓰기 없으면("") 붙여서 나옴 그러므로 -175가 아닌 -1 7 5가 나와야하므로 " "필요
    
'''
while True:
    A,B,C=map(int,input().split())

    if(A==0 and B==0 and C==0):
        break
    else:
        #여기부터
        if(max(A,B,C)==A):
            A,C=C,A
        elif(max(A,B,C)==B):
            B,C=C,B
            #여기까지 몰랐음!!! max를 먼저 따지고 A,B=B,A는 swap없이도 바꿀 수 있다.
        pita=A*A+B*B
        if(pita==C*C):
            print("right")
        else:
            print("wrong")
