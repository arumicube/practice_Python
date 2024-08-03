
import sys
N=int(sys.stdin.readline())
L=sys.stdin.readline().strip() #.strip()=공백제거
M = 1234567891
sum=0
for i in range(N):
    mod=((ord(L[i])-96)*(31**i)) % M #-'a'+1 한 다음 곱하기 31의 i제곱 나누기 mod의 최대
    sum+=mod
print(sum)
#이렇게 하면 50점이 나온다. 진짜 답은 밑에
#근데 r_power는 왜 있는지 아직도 모르겠다.
'''
import sys

# 입력 받기
N = int(sys.stdin.readline())
L = sys.stdin.readline().strip()

# 상수 정의
r = 31
M = 1234567891

# 해시 값 계산
hash_value = 0
r_power = 1  # r^i 값을 저장하기 위한 변수

for i in range(N):
    char_value = ord(L[i]) - ord('a') + 1  # 'a'를 1로 맞추기 위해
    hash_value = (hash_value + char_value * r_power) % M  # 매 단계마다 모듈러 연산 적용
    r_power = (r_power * r) % M  # r^i 값을 계산하고 매 단계마다 모듈러 연산 적용

print(hash_value)
'''