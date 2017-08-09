import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

# 지역명을 입력받는다.(지역명이 없을경우 Error 를 보여준다.)
if len(sys.argv)<=1 :
	print("Error: 지역이름을 입력하세요")
	sys.exit()
regionNumber = sys.argv[1]

#RSS Site 주소
siteURL = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 지역명이름을 위한 변수
values = {
	'stnId': regionNumber
}
print(values)

# 매개변수를 URL 인코딩을 해준다.
params = urllib.parse.urlencode(values)

# RSS URL을 파라미터와 조합
RSSurl = siteURL + "?" + params

print("url=",RSSurl)

#RSS 정보를 메모리에 저장
sitedata = urllib.request.urlopen(RSSurl).read()

# utf-8 형식으로 decode
RSStext = sitedata.decode("utf-8")

# BeautifulSoup 으로 분석
soup= BeautifulSoup(RSStext,"html.parser")

#정보추출
title_list = soup.find_all("title")
wf = soup.find("wf")

for title in title_list:
	sitetitle=title.string
	print(sitetitle)

print(wf)

