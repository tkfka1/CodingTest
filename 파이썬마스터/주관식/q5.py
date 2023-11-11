'''
【문제 5】 URL에서 쿼리 문자열 추출하기
1. 웹 사이트 주소는 “https://post.naver.com/viewer/postView.nhn?volumeNo=27174949&memberNo=37451778&navigationType=push” 로 한다.
2. 결과는 다음과 같이 한다.
volumeNo=27174949
memberNo=37451778
navigationType=push
'''

temp_url = "https://post.naver.com/viewer/postView.nhn?volumeNo=27174949&memberNo=37451778&navigationType=push"

temp_url1 = temp_url.split("?")
temp_url2 = temp_url1[1].split("&")

volumeNo=temp_url2[0].split("=")[1]
memberNo=temp_url2[1].split("=")[1]
navigationType=temp_url2[2].split("=")[1]

print(f"volumeNo={volumeNo}")
print(f"memberNo={memberNo}")
print(f"navigationType={navigationType}")