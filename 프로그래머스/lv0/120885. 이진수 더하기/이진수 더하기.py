def solution(bin1, bin2):
    #무조건 bin1이 길이가 길던가 같게
    if len(bin1) < len(bin2):
        temp = bin1
        bin1 = bin2
        bin2 = temp
    
    #문자열 뒤집기
    bin1 = bin1[::-1]
    bin2 = bin2[::-1]
    
    newbin = ""
    stack = 0
    for i in range(len(bin2)):
        if bin2[i] == "1":
            if bin1[i] == "1":
                if stack:
                    newbin += "1"
                else:
                    stack = 1
                    newbin += "0"
            else:
                if stack:
                    newbin += "0"
                else:
                    stack = 0
                    newbin += "1"
        else:
            if bin1[i] == "1":
                if stack:
                    newbin += "0"
                else:
                    newbin += "1"
            else:
                if stack:
                    stack = 0
                    newbin += "1"
                else:
                    newbin += "0"
    print(bin1)
    for i in range(len(bin2),len(bin1)):
        if bin1[i] == "1":
            if stack:
                newbin += "0"
            else:
                newbin += "1"
        else:
            if stack:
                stack = 0
                newbin += "1"
            else:
                newbin += "0"
    
    if stack:
        newbin += "1"

    
    return newbin[::-1]