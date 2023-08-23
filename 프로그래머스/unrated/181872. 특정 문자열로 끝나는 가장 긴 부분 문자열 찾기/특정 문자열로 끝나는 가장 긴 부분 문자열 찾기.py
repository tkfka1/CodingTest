def solution(myString, pat):
    return myString[:len(myString)-myString[::-1].find(pat[::-1])]