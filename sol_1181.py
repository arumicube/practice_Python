#단어 정렬
#길이 짧은 것부터
#길이 같으면 사전순대로
#1. 길이순대로 정리하고 계차함수 +1하고, 개수가 2개 이상이면 사전순으로 정렬 고
#2. 1번 해봤는데 개씹노가다임 그러므로 먼저 sort로 사전순 정렬 후 버블정렬 고
import sys

N=int(sys.stdin.readline())
arr=[]
for u in range(N):
    arr.append(sys.stdin.readline().strip())#strip=공백,줄바꿈제거
    #sys.stdin.readline().strip() = input()
    #sys.stdin.readline()는 \n이 포함되어있어 for에 연속으로 추가하게 되면 곤란해진다.
    
arr1=set(arr)
arr=list(arr1)
#중복제거

#사전순으로 먼저 고치고, 그걸 길이순으로 정렬하려면,
arr.sort() #사전순정렬
arr.sort(key=len) #길이를 기준으로 정렬

'''
for i in range(len(arr)):
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, len(arr) - i - 1): 
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if len(arr[j]) > len(arr[j + 1]): 
                arr[j],arr[j+1]=arr[j+1],arr[j]
#까지가 길이대로 정렬임
'''
#버블정렬은 시간초과된다.


for p in range(len(arr)):
    print(arr[p])
