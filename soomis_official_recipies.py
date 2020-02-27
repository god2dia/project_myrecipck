# 수정금지
import time

from selenium import webdriver
# from selenium import webdriver as wd
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome('/Users/cho/Downloads/chromedriver')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


url = 'https://post.naver.com/my/series/detail.nhn?seriesNo=472832&memberNo=3669297'
driver.get(url)

SCROLL_PAUSE_TIME = 0.5
cnt_up = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for cnt in range(1, 4):
	driver.find_element_by_xpath('//*[@id="more_btn"]/button').click()
	# btn 클릭후 스크롤 하단으로 내리기 반복
	while True:

		# Scroll down to bottom
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
		soup = BeautifulSoup(driver.page_source, 'html.parser')
		soomis_official_recipes = soup.select('#el_list_container > ul > ul > li ')

for soomis_official_recipe in soomis_official_recipes:
	soomis_official_recipe_doc = {
		'author': '',
		'description': '',
		'image': '',
		'category': '',
		'posting_day': '',
		'title': 'title',
		'url': url
	}
	print(cnt_up)
	# &가 없는 title이 있어서 인데스를 설정하면 에러가 발생
	title = soomis_official_recipe.select_one('div.spot_post_name').text.strip()
	print(title)
	#

	image = str(soomis_official_recipe.select_one('img').attrs['src'])
	print(image)


	category = '공식레시피'
	print(category)
	#
	posting_day = str(soomis_official_recipe.select_one('a > p').text.split()[0])
	print(posting_day)

	#
	description = '수미네반찬 공식 레시피'
	print(description)

	author = '수미네반찬 블로그'
	print(author)
	#
	pre_url = soomis_official_recipe.select_one('a.spot_post_area').get('href')
	url = 'https://post.naver.com' + pre_url
	print(url)


	soomis_official_recipe_doc = {
		'author': author,
		'description': description,
		'image': image,
		'category': category,
		'posting_day': posting_day,
		'title': title,
		'url': url
	}

	# 	continue
	cnt_up += 1


        #db에 뽑은 data 저장
	# db.soomi_all_recipes.insert_one(soomis_official_recipe_doc) #저장할때만 활성화 시키기
	# db.soomis_official_recipes.insert_one(soomis_official_recipe_doc)
driver.close()

