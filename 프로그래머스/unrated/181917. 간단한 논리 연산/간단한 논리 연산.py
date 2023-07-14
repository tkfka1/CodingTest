def solution(x1, x2, x3, x4):
    answer = True
    
    
    def findv(a,b):
        if a == True or b == True:
            return True
        else:
            return False
    
    def findn(a,b):
        if a == False or b == False:
            return False
        else:
            return True

    answer = findn(findv(x1,x2),findv(x3,x4))
    
    
    return answer