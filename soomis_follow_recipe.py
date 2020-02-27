#크롤링시 copy_selector 한번으로는 가져올수 없어서 1st와 2nd로 나눔
import time

from selenium import webdriver
# from selenium import webdriver as wd
from bs4 import BeautifulSoup

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

driver = webdriver.Chrome('/Users/cho/Downloads/chromedriver')
# 크롬을 연다. (★chromedriver.exe 의 경로를 제대로 설정해주는 것이 중요함)


url = 'https://post.naver.com/search/post.nhn?keyword=%EC%88%98%EB%AF%B8%EB%84%A4%EB%B0%98%EC%B0%AC+%EB%A0%88%EC%8B%9C%ED%94%BC+'
driver.get(url)

SCROLL_PAUSE_TIME = 0.5
cnt_up = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
for cnt in range(0, 42):
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
		soomis_follow_recipes = soup.select('#_list_container > ul > li')

soomis_follow_recipe_doc = {
		'author': '',
		'description': '',
		'image': '',
		'category': '',
		'posting_day': '',
		'title': 'title',
		'url': url
	}

# 하나 더 만들어보자
for soomis_follow_recipe in soomis_follow_recipes:
    print(cnt_up)

    title = soomis_follow_recipe.select_one('div > div.feed_body > div.text_area > a.link_end > strong').text.strip()
    if title == "'수미네 반찬' 할배특집 오징어초무침-김치콩나물국밥 레시피는?":
        continue
    if title == "'수미네 반찬' 할배특집 오징어초무침-김치콩나물국밥 레시피는?.":
        continue
    if title == "[공유] 엄마가 해주는 그 맛 <수미네반찬 닭볶음탕 레시피>":
        continue
    if title == "예스24 주목신간 수미네반찬  예스맘의 선택":
        continue
    if title == "예스24 요리책 구매_수미네반찬 도마 굿즈까지:)":
        continue
    if title == "[공유] [이슈Q] '수미네 반찬' 묵은지등갈비찜, '만물상' 레시피와 차이점은?":
        continue
    if title == "수미네반찬 47회 48회 재방송 무료 다시보기 레시피 무료보기":
        continue
    if title == "오늘의 레시피 - 두부두루치기":
        continue
    if title == "예스24 요리책 구매_ 수미네반찬 도마 굿즈까지:)":
        continue
    if title == "+ 11월주목도서 _ 수미네 반찬 레시피북 & 퇴근길 인문학 수업":
        continue
    if title == "[공유] 김수미표 고구마순갈치조림 수미네 반찬 레시피":
        continue
    if title == "오늘의 레시피 - 묵은지쌈밥":
        continue
    if title == "[공유] [Recipe of the Day] #4. 수미네반찬'소라비빔국수' 레시피":
        continue
    if title == "오늘의 레시피 - 수미네반찬 오징어전":
        continue
    if title == "수미네반찬 책 사고 예스24굿즈 미피 윷놀이사은품 받아써효":
        continue
    if title == "[공유] 수미네반찬 레시피 호박볶음, 간단한 반찬 만들기":
        continue
    if title == "+ 예스24도서 _ 엄마요리책,레시피북,쿡북!! 수미네반찬 도마받기!":
        continue
    if title == "[공유] ​수미네 반찬 묵은지볶음, 묵은지찜 레시피 밥도둑 인정!":
        continue
    if title == "김수미 대파김치 수미네반찬 대파김치 초간단 레시피!.":
        continue
    if title == "[공유] 저녁메뉴 고민 왜해? 수미네반찬 오징어볶음 양념장부터 황금레시피":
        continue
    if title == "레시피북 YES24굿즈와 함께 요리책으로 집밥해먹기 도전!":
        continue
    if title == "수미네반찬 책사고 디즈니굿즈도 득템!":
        continue
    if title == "수미네반찬":
        continue
    if title == "[공유] [이슈Q] '수미네 반찬' VS 김가연 멸치볶음 레시피 차이점은? 백종원표 멸치볶음도 '눈길'":
        continue
    if title == "예스24 주목신간 수미네반찬 예스맘의 선택":
        continue
    if title == "수미네반찬 책 사고 2월예스24굿즈 페코 틴케이스 받고~!!":
        continue
    if title == "예스24 요리책 구입하고 10월 예스베리굿즈 수미네반찬 도마 득템":
        continue
    if title == "[공유] '수미네 반찬' 닭볶음탕·멸치볶음·육전 레시피 공개… 미카엘 표 '치킨 키예프'는?":
        continue
    if title == "예스24에서 수미네반찬 책사고 굿즈로 마블지갑까지 겟!":
        continue
    if title == "예스24 수미네 반찬 책 고르고 귀여운 미피램프 득템♩":
        continue
    if title == "오늘의 레시피 - 애호박찌개":
        continue
    if title == "예스24 디즈니굿즈, 수미네반찬 구입하니 딱!":
        continue
    if title == "오늘의 레시피 - 대피김치":
        continue
    if title == "예스24굿즈 마블지갑 사은품으로 받을 수 있어요":
        continue
    if title == "요리책 사고 예스24굿즈 도마 득템":
        continue
    if title == "예스24 레시피북 사고 수미네반찬 도마 받음♬":
        continue
    if title == "레시피북 사고 수미네반찬 도마 받아요":
        continue
    if title == "+ 예스맘이 선택한 요리책 _ 수미네반찬2, 에어프라이어 레시피100 맛있게 요리하자!!":
        continue
    if title == "오늘의 레시피 - 옛날돈가스":
        continue
    if title == "오늘의 레시피 - 간장감자조림":
        continue
    if title == "예스24굿즈 수미네반찬 도마 요리책과 같이 겟~!":
        continue
    if title == "오늘의 레시피 - 애호박찌개":
        continue
    if title == "예스24 디즈니굿즈 , 수미네반찬 구입하니 딱!":
        continue
    if title == "오늘의 레시피 - 대파김치":
        continue
    if title == "예스24굿즈 마블지갑 사은품으로 받을 수 있어요":
        continue
    if title == "요리책 사고 예스24굿즈 도마 득템":
        continue
    if title == "레시피북 사고 수미네반찬 도마 받아요":
        continue
    if title == "예스24 집밥 레시피북 구입하고 받은 수미네반찬 도마 좋네":
        continue
    if title == "여보~정숙네 이거야 이거!":
        continue







    print(title)
    #
    # feed_element_27165580 > div > div.feed_body.og_type > div.og.s_size > div > a
    image = str(soomis_follow_recipe.select_one('div > div.feed_body > div.image_area > a.link_end > img ').attrs['src'])
    print(image)

    category = '따라하기 레시피'
    print(category)
    #
    posting_day = str(soomis_follow_recipe.select_one('div.feed_head > div > div.info_post > time').text.split()[0])
    print(posting_day)

    #
    description = soomis_follow_recipe.select_one('div.feed_body > div.text_area > a.link_end > p').text
        # feed_element_27165580 > div > div.feed_body.og_type > div.text_area > a.link_end > p
    print(description)

    # tvN의 공식 레시피 제외 시키는 방법?
    # if 'tvN' in author:
    #   continue
    # feed_element_27450825 > div > div.feed_head > div > div.writer_area > p.writer > span.name > a > span
    author = soomis_follow_recipe.select_one('div.feed_head > div > div.writer_area > p.writer > span.name > a').text
    # if 'tvN' or '첫사랑 이야기' not in author:
    print(author)
    #
    pre_url = soomis_follow_recipe.select_one('div.feed_body > div.text_area > a.link_end').get('href')
    url = 'https://post.naver.com' + pre_url
    print(url)


    soomis_follow_recipe_doc = {
        'author': author,
        'description': description,
        'image': image,
        'category': category,
        'posting_day': posting_day,
        'title': title,
        'url': url
    }
    cnt_up += 1

    # db.soomi_all_recipes.insert_one(soomis_follow_recipe_doc)
    # db.soomis_follow_recipes.insert_one(soomis_follow_recipe_doc) #저장할때만 활성화 시키기
driver.close()

