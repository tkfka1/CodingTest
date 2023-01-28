def solution(str1, str2):
    
    def makedict(s):
        temp = {}
        s_sum = 0
        for i in range(1,len(s)):
            if s[i].isalpha():
                if s[i-1].isalpha():
                    if temp.get((s[i-1].lower(),s[i].lower())):
                        temp[(s[i-1].lower(),s[i].lower())] += 1
                    else:
                        temp[(s[i-1].lower(),s[i].lower())] = 1
                    s_sum += 1
                        
        
        return temp,s_sum
        
    s1,s1_sum = makedict(str1)
    s2,s2_sum = makedict(str2)
    
#     print(s1)
#     print(s2)
#     print(s1_sum+s2_sum)
    
    inter = 0
    for i in list(set(s1)&set(s2)):
        inter += min(s1[i],s2[i])

    # print(inter)
    
    if not s1_sum+s2_sum:
        return 65536
    
    return int(inter/(s1_sum+s2_sum-inter)*65536)