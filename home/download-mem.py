import urllib.request

# URL 저장 경로 지정하기
url = "https://xmlangel.github.io/images/xmlangel.jpg"

# 저장할 파일이름
savename = "download2.jpg"

##다운로드
memory = urllib.request.urlopen(url).read()
print("memory 에 저장")

#파일로 저장
with open(savename, mode ="wb") as f:
	f.write(memory)
	print("저장완료")


