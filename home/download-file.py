import urllib.request

# URL 저장 경로 지정하기
url = "https://xmlangel.github.io/images/xmlangel.jpg"

# 저장할 파일이름
savename = "download.jpg"

##다운로드
urllib.request.urlretrieve(url, savename)
print("저장완료")