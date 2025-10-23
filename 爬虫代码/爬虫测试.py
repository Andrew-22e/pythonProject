import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from DrissionPage import ChromiumPage
from DrissionPage.common import Keys
from DrissionPage import Chromium, ChromiumOptions

# co = ChromiumOptions().headless()

# # 连接浏览器
# dp = ChromiumPage(co)  
# # 访问网页
# dp.get('https://www.baidu.com')

# print(dp.title)
# dp.quit()

import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://www.givemeoc.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.givemeoc.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}
cookies = {
    "online_count": "393",
    "online_count_time": "1760532361",
    "Hm_lvt_5c66a1115911457bff837bebe34f9d6e": "1760530008",
    "Hm_lpvt_5c66a1115911457bff837bebe34f9d6e": "1760532361",
    "shuaidi_OC": "2"
}
url = "https://www.givemeoc.com/wp-admin/admin-ajax.php"
data = {
    "action": "filter_companies",
    "nonce": "9d8d739859",
    "paged": "3",
    "company_name": "",
    "company_type": "",
    "location": "",
    "recruitment_type": "",
    "target_candidates": "",
    "position": "",
    "progress_status": "",
    "should_increment_counter": "1"
}
response = requests.post(url, headers=headers, data=data,cookies=cookies)

print(response.text)
print(response)