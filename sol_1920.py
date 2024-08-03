#베껴냄 오답노트 다시하기!!!!!!!!!!!!!!
import sys
N=int(sys.stdin.readline())
arrN=list(map(int,sys.stdin.readline().split()))
arrN.sort() #엥 이게 필수라고????
M=int(sys.stdin.readline())
arrM=list(map(int,sys.stdin.readline().split()))

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start<= end :
        mid = (start + end) //2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid -1
    return 0

'''
for i in range(M):
    for j in range(N):
        if arrM[i]==arrN[j]:
            IsExist[i]=1
''' #시간초과 이슈
'''
for num in arrM: #arrM의 0~M
    if num in arrN: # if문에서 "in"은 안에 포함되는가?임
        IsExist.append(1)
    else:
        IsExist.append(0)
''' #이것도 시간초과 이슈
#걍 바로 print 해버려
'''
for num in arrM: #arrM의 0~M
    if num in arrN: # if문에서 "in"은 안에 포함되는가?임
        print(1)
    else:
        print(0)
''' #또 시간초과 미친
#마지막 최후의 수단: 이분 탐색(mid)
for m in arrM:
    isIn = binary_search(m,arrN)
    print(isIn)
    
