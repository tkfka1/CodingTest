def solution(n, words):
    answer = []
    def man(n,i):
        a = i//n
        b = i%n
        a = a+1
        if b == 0:
            a = a-1
            b = n
        return [b,a]

    dic = {}
    lenwords = len(words)
    for i in range(lenwords):


        if words[i][0] == words[i]:
            i = i + 1

            answer = man(n, i)
            break
        if words[i][0] in dic.keys():
            if words[i] in dic[words[i][0]]:
                i = i+1

                answer = man(n, i)
                break
            else:
                dic[words[i][0]] = dic[words[i][0]] + [words[i]]
        else:
            dic[words[i][0]] = [words[i]]

        if not i == lenwords-1:
            if not words[i+1][0] == words[i][-1]:
                i = i+2

                answer = man(n, i)
                break
    else:
        answer = [0,0]

    return answer