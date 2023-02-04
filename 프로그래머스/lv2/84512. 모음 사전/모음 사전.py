import itertools
def solution(word):
    answer = 0
    mo = ["A","E","I","O","U"]
    li = ["A","E","I","O","U"]
    for i in range(2,6):
        for ii in itertools.product(mo, repeat=i):
            li.append(''.join(ii))
    
    li = sorted(li)
    
    return li.index(word)+1