while True:
    STR1=input()
    
    STACK=[]

    
    if STR1 == "." :
        break
    for i in STR1:
        if i =='[' or i=='(':
            STACK.append(i)
        elif i ==']':
            if len(STACK)!=0 and STACK[-1]=='[':
                STACK.pop()
                #]로 시작하지 않고, 마지막 글자가 [일 때 (] X
            else:
                STACK.append(']')
                break
        elif i ==')':
            if len(STACK)!=0 and STACK[-1]=='(':
                STACK.pop()
            else:
                STACK.append(i)
                break
    
    
    if len(STACK)==0:
        print("yes")
    else:
        print("no")
'''
    for i in STR1: 
        if i=='(':
            STACK1.append(i)
        elif i ==')':
            if len(STACK1) !=0: #(가 들어있을 때
                STACK1.pop()            
                    
    for j in STR1: 
        if j=='[':
            STACK2.append(j)
        elif j ==']':
            if len(STACK2) !=0: #(가 들어있을 때
                STACK2.pop()
    if  len(STACK1)==0 and len(STACK2)==0: #모두 짝을 이룸
        print("YES")
    else: #'('만 추가된채로 끝났을 때
        print("NO")
'''
#괄호가 짝을 이루지 않는 경우에 대해 제대로 처리하지 않고 
#있습니다. 예를 들어, (와 ] 또는 [와 )가 혼합된 경우를 올바르게 처리하지 못합니다.
#ex)      ([ (([( [ ] ) ( ) (( ))] )) ]).
            
    
        