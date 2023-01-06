def solution(msg):
    answer = []
    dic = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
           14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
           26: 'Z'}
    landic = 26

    while msg:
        do = False
        tempword = ""
        reskey = -1
        resnum = 0
        tlandic = landic

        for i in range(len(msg)):
            resnum = i
            tempword = tempword + msg[i]
            for key, value in dic.items():
                if tempword == value:
                    reskey = key
                    break
                elif key == landic:
                    landic = landic + 1
            if tlandic+1 == landic:
                do = True
                resnum = i
                dic[landic] = tempword
                break

        answer.append(reskey)
        if msg == tempword:
            if not do:
                break
        msg = msg[resnum:]



    return answer