def solution(dots):
    
    x,y = dots[-1]
    
    for i in dots:
        if i[0] != x:
            if i[1] != y:
                return abs(x-i[0])*abs(y-i[1])
    
 