def solution(begin, end):
    answer = []
    
    def find(x):
        t = [1]
        for i in range(2,int(x**0.5)+ 1):
            if x%i == 0:
                temp = x//i
                if temp > 10000000:
                    t.append(i)
                else:
                    return temp
        return max(t)
    
    if begin == 1:
        answer.append(0)
        begin += 1
        
    for i in range(begin,end+1):
        answer.append(find(i))
    
    return answer