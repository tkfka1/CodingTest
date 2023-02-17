def solution(cards1, cards2, goal):
    answer = ''
    
    st1 = 0
    st2 = 0
    
    l1 = len(cards1)
    l2 = len(cards2)
    
    for i in goal:
        if st1 == l1:
            if i == cards2[st2]:
                st2 += 1
            else:
                return "No"
            
        elif st2 == l2:
            if i == cards1[st1]:
                st1 += 1
            else:
                return "No"
        elif i == cards1[st1]:
            st1 += 1
        elif i == cards2[st2]:
            st2 += 1
        else:
            return "No"
    
    return "Yes"