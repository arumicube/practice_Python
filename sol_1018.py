import sys
N,M=map(int,sys.stdin.readline().split()) #split vs strip
cnt=[]
Ches=[]
for n in range(N):
    Ches.append(sys.stdin.readline().strip())
        
#모든 경우의 수 중 최솟값을 구해야한다.
for a in range(N-7):
    for b in range(M-7): #-7인 이유: 만약 10일 경우 최대 2일 때 2~9까지 8*8이 갸능
        Black=0 #검정으로 시작
        White=0 #흰색으로 시작
        for i in range(a,a+8): #a+0~a+7
            for j in range(b,b+8):
                #i+j가 짝수면 처음 칠한 색과 같아야함
                #홀수면 처음과 달라야함 즉, 칠할 색의 양이 늘어난다.
                if (i+j)%2==0:
                    if Ches[i][j]=='W': #처음이 하얀색이라면
                        Black+=1 #옆이 검정색
                    else: #검정색이라면
                        White+=1
                else: # 홀수라면
                    if Ches[i][j]=='W': #처음이 검정색일 때
                        White+=1 #옆이 하얀색
                    else: #처음이 하얀색이라면
                        Black+=1
                        
        # 걍.... 증가시키는 부분을 모르겠는데 나중에 꼭 다시 풀어보기
        cnt.append(White)#흰색시작
        cnt.append(Black) #검정시작
        #a가 끝날 때까지(0-2) 계속하여 경우의 수 추가
print(min(cnt))
                        