import math

def solution(arrayA, arrayB):
    answer = 0

    # def 약수 나뉘냐
    def 나뉘냐(x,list):
        if sum(list)%x != 0:
            return False
        for i in list:
            if i%x != 0:
                return False
        return True
    
    def 나뉘는거없냐(x,list):
        for i in list:
            if i%x == 0:
                return False
        return True
    
    A_gcd = arrayA[0]
    for i in range(len(arrayA)):
        A_gcd = math.gcd(A_gcd, arrayA[i])
    
    B_gcd = arrayB[0]
    for i in range(len(arrayB)):
        B_gcd = math.gcd(B_gcd, arrayB[i])
    
    if A_gcd >= B_gcd:
        if 나뉘는거없냐(A_gcd,arrayB):
            return A_gcd
    
    if 나뉘는거없냐(B_gcd,arrayA):
        return B_gcd
    
    
    
    return answer