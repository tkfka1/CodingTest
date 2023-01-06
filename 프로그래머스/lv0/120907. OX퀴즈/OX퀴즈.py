def solution(quiz):
    answer = []
    def plma(s):
        if s == "+":
            return True
        return False
    for i in quiz:
        temp = i.split(" ")
        if plma(temp[1]):
            if int(temp[0]) + int(temp[2]) == int(temp[4]):
                answer.append("O")
            else:
                answer.append("X")
        else:
            if int(temp[0]) - int(temp[2]) == int(temp[4]):
                answer.append("O")
            else:
                answer.append("X")
                        
    return answer