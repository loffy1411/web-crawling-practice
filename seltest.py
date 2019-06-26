from selenium import webdriver
from bs4 import BeautifulSoup

# chromedriver 연결
driver = webdriver.Chrome('C:/Users/Jisun/Downloads/chromedriver')

# 축구 사이트에 연렬
driver.get('https://sports.news.naver.com/wfootball/record/index.nhn')

# 소스 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# 팀 이름에 대한 정보
team = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td.align_l > div > span')
# 경기수에 대한 정보
info1 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(3) > div > span')
# 승점에 대한 정보
info2 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(4) > div > span')
# 승 수에 대한 정보
info3 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td.selected > div > span')
# 무 수에 대한 정보
info4 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(6) > div > span')
# 패 수에 대한 정보
info5 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(7) > div > span')
# 득점에 대한 정보
info6 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(8) > div > span')
# 실점에 대한 정보
info7 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(9) > div > span')
# 득실차에 대한 정보
info8 = soup.select('#wfootballTeamRecordBody > table > tbody > tr > td:nth-child(10) > div > span')

# 출력
print("%-30s%-5s%-5s%-5s%-5s%-5s%-5s%-5s%-5s"%("팀", "경기수", "승점", "승", "무", "패", "득점", "실점", "득실차"))
for i in range(len(team)) :
    print("%-30s%-5s%-5s%-5s"%(team[i].text.strip(), info1[i].text.strip(), info2[i].text.strip(), info3[i].text.strip()), end = '')
    print("%-5s%-5s%-5s%-5s%-5s"%(info4[i].text.strip(), info5[i].text.strip(), info6[i].text.strip(), info7[i].text.strip(), info8[i].text.strip()))