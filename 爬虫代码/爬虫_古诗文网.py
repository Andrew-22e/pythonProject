import json
import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


# 请求网页
def page_request(url):
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.get(url)
        page = driver.page_source
    except Exception as e:
        print(f"出现异常: {e}")
        page = None
    finally:
        if 'driver' in locals():
            driver.quit()
    return page


# 解析网页
def page_parse(html):
    sentence_list = []
    href_list = []
    if html:
        soup = BeautifulSoup(html, 'lxml')
        sentences = soup.select('div.left>div.sons>div.cont>a:nth-of-type(1)')
        poets = soup.select('div.left>div.sons>div.cont>a:nth-of-type(2)')
        min_len = min(len(sentences), len(poets))
        for i in range(min_len):
            temp = sentences[i].get_text() + "————" + poets[i].get_text()
            sentence_list.append(temp)
            href = sentences[i].get('href')
            href_list.append("https://so.gushiwen.cn/" + href)
    return [href_list, sentence_list]


# 保存名句到txt中
def save_txt(info_list):
    with open(r'C:\\lj666\\VScode\\python\\爬虫\\文本\sentence.txt', 'a', encoding='utf-8') as txt_file:
        for element in info_list[1]:
            txt_file.write(json.dumps(element, ensure_ascii=False) + '\n\n')


# 请求子网页
def sub_page_request(info_list):
    subpage_urls = info_list[0]
    sub_html = []
    try:
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        for url in subpage_urls:
            driver.get(url)
            html = driver.page_source
            sub_html.append(html)
    except Exception as e:
        print(f"请求子网页时出现异常: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()
    return sub_html


# 解析子网页
def sub_page_parse(sub_html):
    poem_list = []
    for html in sub_html:
        if html:
            soup = BeautifulSoup(html, 'lxml')
            poems = soup.select('div.left>div.sons>div.cont>div.contson')
            if poems:
                poem = poems[0].get_text().strip()
                poem_list.append(poem)
    return poem_list


# 保存完整诗词到txt中
def sub_page_save(poem_list):
    with open(r'C:\\lj666\\VScode\\python\\爬虫\\文本\\poems.txt', 'a', encoding='utf-8') as txt_file:
        for element in poem_list:
            txt_file.write(json.dumps(element, ensure_ascii=False) + '\n\n')


# 主函数
if __name__ == '__main__':
    print('爬取古诗中...')
    for i in range(1, 4):
        url = 'https://www.gushiwen.cn/mingjus/default.aspx?page=%d&tstr=&astr=&cstr=&xstr='%i
        time.sleep(1)
        html = page_request(url)
        info_list = page_parse(html)
        save_txt(info_list)
        print('第%d页爬取完毕' % i)
        sub_html = sub_page_request(info_list)
        poem_list = sub_page_parse(sub_html)
        sub_page_save(poem_list)
        print('第%d页保存完毕' % i)
    print('所有数据爬取完毕!')