T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 0
    li = map(int, input().split())
    for i in li:
        if i % 2 == 1:
            answer += i
            
    print(f"#{test_case} {answer}")