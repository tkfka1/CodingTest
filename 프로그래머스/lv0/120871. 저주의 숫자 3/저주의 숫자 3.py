def solution(n):
    answer = 0
    
    def three(n):
        if n%3 == 0:
            return True
        elif 100 > n > 10:
            if str(n)[0] == "3" or str(n)[1] =="3":
                return True
        elif n > 100:
            if str(n)[1] == "3" or str(n)[2] =="3":
                return True
        return False
    
    temp = [0]
    for i in range(1,200):
        if not three(i):
            temp.append(i)

    return temp[n]