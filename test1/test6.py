m,n = map(int,input().split())

def inp_li(x):
    temp = []
    for i in range(x):
        temp.append(list(map(int,input().split())))
    return temp

def su_li(l1,l2):
    if len(l1) >= len(l2):
        for i in range(len(l2)):
            l1[i] += l2[i]
        return l1
    else:
        for i in range(len(l1)):
            l2[i] += l1[i]
        return l2

def print_li(l):
    for i in l:
        print(" ".join(list(map(str,i))))

def sol(m,n):
    answer = []
    if m == 0:
        if n == 0:
            print("")
            return
        else:
            answer = inp_li(n)
            print_li(answer)
            return
    if n == 0:
        answer = inp_li(m)
        print_li(answer)
        return
    li1 = inp_li(m)
    li2 = inp_li(n)
    if m >= n:
        for i in range(len(li2)):
            answer.append(su_li(li1[i],li2[i]))
        if m > n:
            for i in range(len(li2),len(li1)):
                answer.append(li1[i])
    else:
        for i in range(len(li1)):
            answer.append(su_li(li1[i],li2[i]))
        for i in range(len(li1),len(li2)):
            answer.append(li2[i])
    print_li(answer)
    return

sol(m,n)
        