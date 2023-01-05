def solution(new_id):
    answer = ''
    id1 = new_id.lower()


    characters = "~!@#$%^&*()=+[{]}:?,<>/"
    for x in range(len(characters)):
        id1 = id1.replace(characters[x], "")
    id2 = id1


    chars = []
    prev = None
    for c in id2:
        if c == '.':
            if prev != c:
                chars.append(c)
        else:
            chars.append(c)
        prev = c
    id3 = ''.join(chars)


    id4 = id3.strip('.')

    print(id4)

    if id4 == '':
        id4 = 'a'
    id5 = id4

    if len(id5) > 15:
        id6 = id5[:15].strip('.')
    else:
        id6 = id5

    if len(id6) == 1:
        id7 = id6[0]+id6[0]+id6[0]
    elif len(id6) == 2:
        id7 = id6[0]+id6[1]+id6[1]
    else:
        id7 = id6

    answer = id7

    return answer