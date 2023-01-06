def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    x = my_string[num2]
    my_string[num2] = my_string[num1]
    my_string[num1] = x
    return "".join(my_string)