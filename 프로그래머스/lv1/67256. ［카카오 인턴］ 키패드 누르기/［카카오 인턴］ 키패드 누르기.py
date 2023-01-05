def solution(numbers, hand):
    answer = ''
    prevL = 1, 4
    prevR = 1, 4

    for r in numbers:
        print(r)
        if r == 1 or r == 4 or r == 7:
            result = "L"
            prevL = 1, int((r+2)/3)
        elif r == 3 or r == 6 or r == 9:
            result = "R"
            prevR = 1, int(r/3)
        else:
            if r == 0: r = 4
            else: r = int((r+1)/3)

            diffL = abs(r - prevL[1]) + prevL[0]
            diffR = abs(r - prevR[1]) + prevR[0]

            if diffR == diffL:
                if hand == "right":
                    result = "R"
                elif hand == "left":
                    result = "L"
            elif diffR > diffL:
                result = "L"
            elif diffL > diffR:
                result = "R"

            if result == "L":
                prevL = 0, r
            elif result == "R":
                prevR = 0, r

        answer = answer + result

    return answer