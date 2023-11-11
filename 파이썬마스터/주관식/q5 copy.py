'''
【문제 5】 URL에서 쿼리 문자열 추출하기
웹 사이트 주소는 "https://example.com/product/item?itemId=12345&category=books&discount=yes"입니다.
URL에서 쿼리 문자열을 추출하여 다음과 같이 출력합니다.
itemId=12345
category=books
discount=yes
이 문제는 주어진 URL에서 쿼리 문자열을 파싱하여 각 파라미터와 값을 분리하는 방법을 학습하는 데 도움이 됩니다.
'''

temp_url = "https://example.com/product/item?itemId=12345&category=books&discount=yes"

temp_url1 = temp_url.split("?")
temp_url2 = temp_url1[1].split("&")

itemId=temp_url2[0].split("=")[1]
category=temp_url2[1].split("=")[1]
discount=temp_url2[2].split("=")[1]

print(f"itemId={itemId}")
print(f"category={category}")
print(f"discount={discount}")