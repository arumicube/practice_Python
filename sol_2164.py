from collections import deque
#deque를 쓸 시간이 왔도다..
import sys
N=int(sys.stdin.readline())
card=[]
card = deque(range(1, N + 1))
'''
for i in range(N):
    card.append(i+1) #1,2,3,4
'''
while len(card)>1:
    '''
    card.pop(0) #0번째 원소 삭제
    card=card[1:]+card[:1]
    '''
    #시간초과가 뜬다.
    card.popleft()
    card.append(card.popleft())

print(card[0])