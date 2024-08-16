#2839번 시간제한:반복문 사용불가
import sys
import math
input=sys.stdin.readline
A,B,V=map(int,input().split())

#하루에 가는 거리 A-B, 남은거리 V-A+B 마지막날 +A 올라가면 안미끄러짐
#마지막날 남은거리가 0,1,2...인데 A가 더 크다.
#즉, 마지막날 제외하고 나중에 day에 1 더하면 됨
#2 1 5면 5-2=3//1+1, 5 1 6이면 6-5=1//1+1 하면 될듯..?
day=math.ceil((V-A)/(A-B)) +1 #ceil=올림
print(day)
