
N=int(input())
cnt=0
while N>=0:
    # 11이 입력될 경우 6+5
    #1. N=3i+5j여야한다.
    #걍.. 3이랑 5 둘다 빼고 구하면 될거같은디 일단 해보자
    '''
    if N>0:
        N-=3
        cnt+=1
    if N<0:
        N+=3
        cnt-=1
    if N>0:
        N-=5
        cnt+=1
    if N<0:
        N+=5
        cnt-=1
    if N==0:
        print(cnt)
        break
    ''' #뭐하냐?
    if(N%5==0): #15일 때 5로 나누는게 더 최솟값이므로
        cnt+=(N//5)
        print(cnt)
        break
    #5로 나누어지지 않을 때, 18일 때
    N-=3
    cnt+=1 #15 후 최솟값을 구하려면 5로 나누면되므로!
    
if(N<0):
    print(-1)
    
    
    
    
    