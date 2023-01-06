def solution(spell, dic):
    for i in dic:
        temp = spell[:]
        for ii in i:
            if temp:
                if ii in temp:
                    temp.remove(ii)
                else:
                    break
        else:
            if not temp:
                return 1
    return 2