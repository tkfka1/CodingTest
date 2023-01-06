def solution(numbers):
    global answer
    answer = ""
    def find(i):
        global answer
        le = 0
        if numbers[i] == "o":
            answer += "1"
            le = 3
        elif numbers[i] == "t":
            if numbers[i+1] == "w":
                answer += "2"
                le = 3
            else:
                answer += "3"
                le = 5
        elif numbers[i] == "f":
            if numbers[i+1] == "o":
                answer += "4"
            else:
                answer += "5"
            le = 4
        elif numbers[i] == "s":
            if numbers[i+1] == "i":
                answer += "6"
                le = 3
            else:
                answer += "7"
                le = 5
        elif numbers[i] == "e":
            answer += "8"
            le = 5
        elif numbers[i] == "n":
            answer += "9"
            le = 4
        elif numbers[i] == "z":
            answer += "0"
            le = 4
        return le

    stat = 0
    while True:
        stat += find(stat)
        if stat == len(numbers):
            break

    return int(answer)