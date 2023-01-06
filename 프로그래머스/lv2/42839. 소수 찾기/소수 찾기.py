from itertools import permutations
import math

def solution(numbers):
    answer = 0
    n = int("9"*len(numbers)) # 2부터 9999999까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제와)

    # 에라토스테네스의 체 알고리즘
    for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    
    array[0] = False
    array[1] = False
    
    num = []
    for i in numbers:
        num.append(int(i))
    num = set(num)
    for i in num:
        if array[i]:
            answer += 1

    if len(numbers) > 1:
        for i in range(len(numbers),1,-1):
            num = []
            combi = list(permutations(numbers,i))
            for ii in combi:
                num.append(int("".join(map(str, ii))))
            
            num = set(num)
            for ii in num:
                if ii >= 10**(i-1):
                    if array[ii]:
                        answer += 1

    return answer