import itertools
def solution(word):
    answer = 0
    li = ["A","E","I","O","U"]
    for i in range(2,6):
        for ii in itertools.product(["A","E","I","O","U"], repeat=i):
            li.append(''.join(ii))

    return sorted(li).index(word)+1