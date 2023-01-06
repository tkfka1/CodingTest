def solution(enroll, referral, seller, amount):
    lenth = len(enroll)
    answer = []
    
    moneydic = {}
    for i in enroll:
        moneydic[i] = 0
            
            
    refdic = {}
    for i in range(lenth):
        refdic[enroll[i]] = [referral[i]]
        
    def refdicing():
        for key,value in refdic.items():
            if not value[-1] == "-":
                refdic[key] += refdic[value[-1]]
                
    refdicing()
    # print(refdic)
    
    for i in range(len(seller)):
        ten = amount[i]*10
        nine = amount[i]*90
        moneydic[seller[i]] += nine
        find = seller[i]
        for ii in refdic[find]:
            if ii == "-":
                break
            else:
                if ten < 10:
                    moneydic[ii] += ten
                    break
                else:
                    ften = ten
                    ten = ften//10
                    nine = ften - ten
                    moneydic[ii] += nine

    for value in moneydic.values():
        answer.append(value)
    return answer