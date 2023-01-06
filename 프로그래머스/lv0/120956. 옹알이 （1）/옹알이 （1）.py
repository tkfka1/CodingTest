def solution(babbling):
    answer = 0
    list = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        count = 0
        while count < len(i):
            if i[count] == "a":
                if i[count+1:count+3] =="ya":
                    count += 3
                else:
                    break
            elif i[count] == "y":
                if i[count+1] =="e":
                    count += 2
                else:
                    break
            elif i[count] == "w":
                if i[count+1:count+3] =="oo":
                    count += 3
                else:
                    break
            elif i[count] == "m":
                if i[count+1] =="a":
                    count += 2
                else:
                    break
            else:
                break
                
            if count == len(i):
                answer += 1
                break
                    
            
                
    return answer