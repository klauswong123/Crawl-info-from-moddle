import requests
from lxml import html
import http.cookiejar as cookielib
import xlwt
from bs4 import BeautifulSoup as bs
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Referer': 'https://buelearning.hkbu.edu.hk/login/index.php',
    'Origin': 'https://buelearning.hkbu.edu.hk'
}
account = '16202406'
password = 'Handsomeguy0!'
login_url = "https://buelearning.hkbu.edu.hk/login/index.php"
session_requests = requests.session()
print("开始模拟登录BU 系統")
post_Url = "https://buelearning.hkbu.edu.hk/login/index.php"
post_Data = {
    "username": account,
    "password": password,
    'anchor': ''
}
response_res = session_requests.post(post_Url, data=post_Data, headers=headers)
list_for_use = []
final_url_email = []
new_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    'Referer': 'https://buelearning.hkbu.edu.hk/course/view.php?id=57468'
}
for i in range(0, 98):
    num = str(i)
    url2= 'https://buelearning.hkbu.edu.hk/user/index.php?contextid=769959&id=57468&perpage=20&page='+num
    html = session_requests.get(url2, headers=new_headers)
    soup = bs(html.content, 'lxml')
    a_link = soup.find_all('a')
    for url in a_link:
        result_url = url.get('href')
        list_for_use.append(result_url)
    course_id = 'https://buelearning.hkbu.edu.hk/user/view.php?id='
    for use in list_for_use:
        if isinstance(use, str):
            if course_id in use:
                final_url_email.append(use)
    st_email = []
    for url in final_url_email:
        url_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
            'Host': 'buelearning.hkbu.edu.hk'
        }
        req = session_requests.get(url, headers=url_headers)
        # print(req.content)
        s = bs(req.content, 'lxml')
        a = s.find_all('a')

        for url1 in a:
            time.sleep(0.1)
            kk = url1.string
            if isinstance(kk, str):
                if 'life.hkbu.edu.hk' in kk:
                    st_email.append(kk)
                    print(kk)

    list_for_use = []
    final_url_email = []

#"I am Klaus"





