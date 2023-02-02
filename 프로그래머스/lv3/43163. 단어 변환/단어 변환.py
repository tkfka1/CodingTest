def solution(begin, target, words):
    answer = 0
    lenth = len(begin)
    
    if not target in words:
        return 0
    
    def find(b,w):
        templi = []
        for i in w:
            st = 0
            for k,v in enumerate(i):
                if b[k] == v:
                    st += 1
            if st == lenth-1:
                templi.append(i)
                
        return templi
    
    
    li = find(begin,words)
    if target in li:
        return 1
    if not li:
        return 0
    
    for answer in range(2,50):
        
        temp = []
        for i in li:
            temp += find(i,words)
        
        li = set(temp)
        if target in li:
            return answer
    
    return answer