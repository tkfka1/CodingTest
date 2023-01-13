def solution(n, left, right):

#     print(n)
#     print(left)
#     print(right) 
        
    li = []
    
    def w(num):
        x = divmod(num,n)
        # print(x)
        if x[1] == 0:
            return n
        if x[1]-x[0] <= 0:
            return x[0]+1
        
        return x[1]
    
    for i in range(left+1,right+2):
        li.append(w(i))

    return li