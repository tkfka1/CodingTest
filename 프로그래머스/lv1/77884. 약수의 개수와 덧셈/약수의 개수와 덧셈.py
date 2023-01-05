def solution(left, right):
    return sum([ -i if len([a for a in range(1,i+1) if i%a==0])%2 else i for i in range(left,right+1)])