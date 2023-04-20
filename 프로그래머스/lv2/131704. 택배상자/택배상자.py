def solution(order):
    answer = 0
    
    stack = []
    
    li = [i for i in range(1,len(order)+1)]

    im = 1
    
    
    while True:
        if answer == len(order):
            break
            
        if order[answer] == im:
            answer += 1
            im += 1
        else:
            if stack:
                if stack[-1] == order[answer]:
                    stack.pop()
                    answer += 1
                else:
                    if im == len(order):
                        break
                    else:
                        stack.append(im)
                        im += 1
            else:
                if im == len(order):
                    break
                else:
                    stack.append(im)
                    im += 1
    
    return answer