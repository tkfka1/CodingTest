def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        val = dic.get(s[i])
        if val or val == 0:
            answer.append(i - dic[s[i]])
            dic[s[i]] = i
            
        else:
            dic[s[i]] = i
            answer.append(-1)
    return answer