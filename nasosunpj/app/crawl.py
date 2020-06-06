import requests
from bs4 import BeautifulSoup
import random

def GetProductInfo(age, gender, budget):
    #상품이름 문자열 가공
    age_group = str((age//10)*10)+"대"
    gender_check = gender
    budget = budget 
    max_price = budget
    min_price = budget - budget//2
    product_M = ["가방", "시계", "셔츠", "향수", "신발", "스포츠", "지갑", "화장품", "음악", "니트"]
    product_W = ["가방", "목걸이", "향수", "구두", "원피스", "지갑", "화장품", "귀걸이", "음악", "치마", "니트"]
    
    if gender_check == "남자":
        product_type_list = product_M
    else:
        product_type_list = product_W

    product_type = random.choice(product_type_list)

    name_input = age_group + gender_check + product_type
    name_input = name_input.replace(" ","%20")
    print(name_input)

    #결과 dict
    product_info = {}

    product_html = requests.get(f"https://search.shopping.naver.com/search/all?baseQuery={name_input}&frm=NVSHMDL&maxPrice={max_price}&minPrice={min_price}&pagingIndex=1&pagingSize=40&productSet=model&query={name_input}&sort=rel&timestamp=&viewType=list")
    product_soup = BeautifulSoup(product_html.text, "html.parser")

    #get detail url
    product_box = product_soup.find("div", {"class" : "basicList_inner__eY_mq"})
    if product_box == None:
        name_input = name_input[3:]
        print("수정:",name_input)
        product_html = requests.get(f"https://search.shopping.naver.com/search/all?baseQuery={name_input}&frm=NVSHMDL&maxPrice={max_price}&minPrice={min_price}&pagingIndex=1&pagingSize=40&productSet=model&query={name_input}&sort=rel&timestamp=&viewType=list")
        product_soup = BeautifulSoup(product_html.text, "html.parser")
        product_box = product_soup.find("div", {"class" : "basicList_inner__eY_mq"})
    
    detail_url = product_box.find("div", {"class" : "basicList_img_area__a3NRA"}).find("a")['href']

    detail_html = requests.get(detail_url)
    detail_soup = BeautifulSoup(detail_html.text, "html.parser")
    #get name
    product_name = detail_soup.find("div", {"class" : "summary_inner"}).find("div", {"class": "naver-splugin"})['data-title'].strip()
    if len(product_name) > 10:
        product_name = product_name[:9] + ".."
    #get image
    product_img = detail_soup.find("div", {"class" : "photo_area"}).find("img", {"id" : "viewImage"})['src']

    price_area = detail_soup.find("div", {"class" : "summary_cet"}).find("div", {"class" : "price_area"})

    #get price
    product_price = price_area.find("span", {"class" : "low_price"}).find("em", {"class": "num"}).text.strip().replace(',','')

    #get url
    product_url = price_area.find("a")["href"]

    #결과에 삽입
    product_info["name"] = product_name
    product_info["img_url"] = product_img
    product_info["price"] = int(product_price)
    product_info["product_url"] = product_url

    print(product_info)
    return product_info  #dictionary 형식으로 반환

#GetProductInfo(age, gender, budget)
