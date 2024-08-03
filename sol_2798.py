import sys

N,M=map(int,sys.stdin.readline().split()) #N개의 카드 중 3장

#arr의 숫자 중 3장을 더했을 때, (랜덤?)
#오류!!! 랜덤은 모든 경우의 수를 해주지 않음
#M과 같거나 작고 (x<=M) 
# 1. 그럼 이 때만 메모리에 저장할까?
#    그중에 Max여야함 그냥 arr2 에 새로 저장한 것들 중에 max면 됨

# 2. itertools 를 사용하여 애초에 카드중에 세장을 뽑는 코드 사용
import itertools
cards = list(map(int, sys.stdin.readline().split())) #카드에 숫자 저장

# 가능한 모든 3장의 카드 조합을 생성
combinations = itertools.combinations(cards, 3) 
#우리가 알고있는 콤비네이션이 아닌 "리스트 중 3개를 뽑는 것"의 모든 경우의 수

MaxSum=0 #으로 가정
for com in combinations: #combinations 라는 변수가 "모든 조합"을 뜻하므로 걍 처음부터 끝의 조합까지
    current_sum = sum(com)
    if current_sum <= M and current_sum >MaxSum: #M보다 작거나 같고, 현재의 max보다 크면
        MaxSum = current_sum
print(MaxSum)
