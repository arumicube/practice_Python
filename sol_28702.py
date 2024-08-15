n=0
#sys.stdin.readline을 쓸경우 공백 줄바꿈이 포함되어
# 있기 때문에 input을 사용해야한다.
for i in range(3, 0, -1): #3부터 1까지 -1의 간격으로
    x = input().strip()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        n = int(x) + i
        #마지막에 11 입력 시 다음 수가 12 이므로 1을 더하는게 맞다
        #두번째가 11일 떄 다다음 수가 13 이므로 2를 더해준다.
if n%15==0: #3과 5의 배수 둘다 만족=15
    print("FizzBuzz")
elif n%3==0: #n%5 !=0 사실상 필요없음
    print("Fizz")
elif n%3!=0:
    print("Buzz")
else:
    print(n)