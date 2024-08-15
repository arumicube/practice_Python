import sys
N=int(sys.stdin.readline())
'''
for n in range(N):
    VPS=sys.stdin.readline()
    VPS1=VPS.count('(')
    VPS2=VPS.count(')')
    if VPS1==VPS2:
        print("YES")
    else:
        print("NO")
''' #이렇게 하면 ())(() 일 때 조차 yes가 나오므로 
#짝맞춰주는게 중요하다.
for n in range(N):
    VPS=sys.stdin.readline()
    stack=[] #pop을 사용할 것이다.
    for i in VPS: #range(len(VPS))는 귀찮아진다. vps걍 하면 vps[0]~으로 처리해줌
        if i=='(':
            stack.append(i)
        elif i ==')':
            if len(stack) !=0: #(가 들어있을 때
                stack.pop()
            else:
                print("NO") #)로 괄호를 열어야할때
                #ex) ()), )
                break
        else: #끝났으면
            if len(stack)==0: #모두 짝을 이룸
                print("YES")
            else: #'('만 추가된채로 끝났을 때
                print("NO")