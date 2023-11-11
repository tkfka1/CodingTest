'''
【문제 1】 주어진 숫자를 천 단위로 구분하기.
1. 사용자로부터 숫자를 입력받아 천 단위 마다 콤마를 구분하여 숫자를 출력
2. 입력 받는 숫자를 변수 num에 저장한다.
3. 입력받은 정보가 숫자로만 되어 있는지 확인한다.
'''

test_num = "10000"

num = test_num

print(num)

if num.isdigit():
    #print("숫자 입니다.")
    stack = 0
    for i in reversed(num):

        print(i, end = ",")
