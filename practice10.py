'''
#stack 구현
import sys
N=int(sys.stdin.readline()) #input 보다 빠름
top=-1
stack=[]

for i in range(N):
    command=sys.stdin.readline().split() #이러면 command는 리스트가 됨 스트링말고!
    if command[0]=='push':
        # 이거 안된다고!!(참고9)
        # 리스트에 추가할 땐 대입하지 말고 더해야함. 왜냐하면 할당이 미리 안되어있음(0으로 할당됐을땐 상관 ㄴ)
        # stack[top+1]=int(command[1]) 안됨!
        stack.append(command[1]) #맨 뒤에 추가한다는 뜻
        top+=1
    elif command[0]=='pop':
        if top==-1:
            print(-1) #'-1'을 출력한다는 뜻
        else:
            print(stack.pop()) #그냥 pop함수가 존재함 ㅁㅊ
            #맨 마지막 원소 리턴, 해당 원소 삭제
            #pop(i)는 i 번째 리턴, 삭제
            top-=1
           
            #삭제를 어떻게.. 하지..? pop함수 사용
    elif command[0]=='size':
        print(len(stack)) #string:len문자열길이 list:len리스트 개수
    elif command[0]=='empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif command[0]=='top':
        if top ==-1:
            print(-1) #top이 -1일때를 빠뜨려서 틀렸다.
        else:
            print(stack[top])
'''

#큐 구현
import sys
N=int(sys.stdin.readline())
queue=[]
front=0
back=0
for i in range(N):
    command=sys.stdin.readline().split() #=input().split() 리스트가 되어버려
    if command[0]=='push':
        queue.append(command[1])
        back+=1
    elif command[0]=='pop':
        if front==back: #같아도됨
            print(-1)    
            #얘 입장에서는 front랑 back이 같으면 요소가 없다는 뜻
            #그래서 back 출력 시에는 back-1의 요소를 출력해준당!
            # stack[top+1]=int(command[1]) 안됨!
        else:#***********************************************************
            #print(queue.pop(0))????????
            #왜 front로 했을 때 pop이 두번이 안되지..?
            #왜 0으로 했을 때 잘나오는거지..?
            #pop(0)을 하게 되면, 삭제하고 왼쪽으로도 옮겨줌 존나 편리함
            
            #오류 나는 이유는 큐가 비어있는 경우 인덱스 오류가 발생한다!!!
            
            print(queue[front]) #삭제는 아니지만 굿
            front+=1
            #********************************************************
    elif command[0]=='size':
        print(back-front) #len 은 불가능일듯.. 삭제를 안해서
    elif command[0]=='empty':
        if front==back:
            print(1)
        else:
            print(0)
            
    elif command[0]=='front':
        if front==back:
            print(-1)
        else:
            print(queue[front])
            
    elif command[0]=='back':
        if front==back:
            print(-1)
        else:
            print(queue[back-1])
