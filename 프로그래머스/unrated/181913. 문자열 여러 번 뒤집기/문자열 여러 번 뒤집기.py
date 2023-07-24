def solution(my_string, queries):
    answer = ''
    for i in queries:
        temp = my_string[i[0]:i[1]+1][::-1]
        answer = my_string[:i[0]] + temp + my_string[i[1]+1:]
        my_string = answer
    return answer