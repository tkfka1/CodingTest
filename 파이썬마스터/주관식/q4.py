'''
【문제 4】 문자 코드 구하기
1. 문자를 커맨드 창에서 입력받는다.
2. 입력은 “문자 1개를 입력하세요 : ”로 한다.
3. 결과는 아래와 같이 화면에 프린트한다. 문자 : c 코드값: 99[0x63]
'''


temp = input("문자 1개를 입력하세요 : ")
c1 = str(ord(temp))
c2 = hex(ord(temp))
print(c2)
print(f"문자 : {temp} 코드값: {c1}[{c2}]")