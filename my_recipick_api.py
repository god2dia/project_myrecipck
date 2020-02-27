from random import random
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
import random
app = Flask(__name__)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('s_official_card.html')



##################################### 레시피 API 생성 ######################################

@app.route('/s_official_recipes', methods=['GET'])
def official_recipes_view():
    soomis_official = list(db.soomi_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_official': soomis_official})

@app.route('/s_follow_recipes', methods=['GET'])
def follow_recipes_view():
    soomis_follow = list(db.soomi_all_recipes.find({'category':'따라하기 레시피'}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_follow': soomis_follow})
# @app.route('/follow_recipes', methods=['GET'])
# def follow_recipes_view():
#     # 서버 내부에서 수행 할 기능 / DB에 저장돼있는 모든 정보 중 '따라하기레시피' 가져오기
#     paik_follow = list(db.paik_all_recipes.find({'category': '따라하기레시피'}, {'_id': 0}))
#     return jsonify({'result': 'success', 'paik_follow': paik_follow})
##################################### 레시피검색 API ######################################
# 세미님 git_hub code 참고
# soomi_all_recipes db에서 s_official_recipe의 정보와 일치하는 data를 넘겨준다
@app.route('/search_soomi_official', methods=['GET'])
def search_soomi_official_view():
    recipe_title_receive = request.args.get('recipe_title_give')
    soomis_official_info = list(db.soomi_all_recipes.find({'category':'공식레시피','title':{'$regex':recipe_title_receive}}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_official_info': soomis_official_info})

# soomi_all_recipes s_follow_recipe db에서 정보와 일치하는 data를 넘겨준다
@app.route('/search_soomi_follow', methods=['GET'])
def search_soomi_follow_view():
    recipe_title_receive = request.args.get('recipe_title_give')
    soomis_follow_info = list(db.soomi_all_recipes.find({'category':'따라하기 레시피','title':{'$regex':recipe_title_receive}}, {'_id': 0}))
    return jsonify({'result': 'success', 'soomis_follow_info': soomis_follow_info})
    ##################################### 유저레시피 저 API ######################################
# 원하는 url을 주고 나의레시피에 저장한다
@app.route('/save_my_recipe', methods=['POST'])
def save_my_recipe():
    # 클라이언트로부터 데이터를 받는 부분
    email_receive = request.form['email_give']
    url_receive = request.form['url_give']

    taeget_url = db.soomi_all_recipes.find_one({'url': url_receive})
    # print(taeget_url)  # test
    title = taeget_url['title']
    image = taeget_url['image']
    categoey = taeget_url['category']
    author = taeget_url['author']
    posting_day = taeget_url['posting_day']
    description = taeget_url['description']

    save_my_recipe = {
        'email': email_receive,
        'url': url_receive,
        'image' : image,
        'title' : title,
        'categoey' : categoey,
        'description' : description,
        'author' : author,
        'posting_day' : posting_day
    }

    if categoey == '공식레시피':
        db.save_official_recipes.insert_one(save_my_recipe)
    else :
        db.save_follow_recipes.insert_one(save_my_recipe)
    return jsonify({'result': 'success'})

    # 사용자가 저장할 url과 my_recipedp 저장되어있는 url과 중복되는지 비교 (미구현)
    # f_sh_url = db.save_follow_recipes.find_one({'url': url_receive})['url']
    # o_sh_url = db.save_official_recipes({'url': url_receive})['url']
    # if taeget_url ==  f_sh_url or o_sh_url:
    #     print(taeget_url)

# 저장된 나의 레시피를 보여준다
@app.route('/search_my_recipe', methods=['POST'])
def search_my_recipe():

    # search_my_recipe에서는 왜 안되는거지
    email_receive = 'follow'
    taeget_email = db.save_official_recipes.find_one({'email': email_receive}) or db.save_follow_recipes.find_one(
        {'email': email_receive})
    key_url = taeget_email['url']
    show_my_recipe = db.soomi_all_recipes.find_one({'url': key_url})
    print(show_my_recipe)

##################################### 레시피 정렬해서 뿌리기 API #####################################
# @app.route('/s_show_recipes', methods=['GET'])
# def show_listing():
#     soomis_show = list(db.soomi_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
#     print(soomis_show)
#     return jsonify({'result': 'success', 'soomis_show': soomis_show})

##################################### 레시피 랜덤 뿌리기 API #####################################

# 추천 레시피 랜덤으로 뽑아서 보여주기 기본 틀
# for g in range(100):
#     soomi_follow_recipe = list(db.soomis_follow_recipes.find({'author':'수미네반찬 블로그'}, {'_id': 0}))
#     good = (random.sample(soomi_follow_recipe, 10))
#     for i in range(10):
#         numData = i
#     good = good[numData]['title']

@app.route('/s_rand_follow_recipes', methods=['GET'])
def random_recipes():
    for repeat in range(10):
        random_recipe = list(db.soomi_all_recipes.find({'category':'공식레시피'}, {'_id': 0}))
        soomi_random_recipe = (random.sample(random_recipe, 10))
        # print(soomi_random_recipe)
    return jsonify({'result': 'success', 'recommend_recipes': soomi_random_recipe})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
