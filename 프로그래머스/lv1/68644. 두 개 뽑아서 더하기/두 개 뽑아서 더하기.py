def solution(numbers): import itertools; return sorted(set([sum(i) for i in itertools.combinations(numbers, 2)]))
    
    
    