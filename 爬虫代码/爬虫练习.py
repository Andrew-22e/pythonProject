import base64
import re
import requests
import csv
import time
import json
import parsel
from lxml import etree
from Crypto.Cipher import AES
from retrying import retry
from tqdm import tqdm
from urllib.parse import unquote
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

"""
#如果使用requests模块发送请求获得的页面源代码与实际源代码不一致，
#则使用selenium模块模拟浏览器访问，获取真实页面源代码

# 使用selenium模块模拟浏览器，自动打开浏览器访问页面
service = Service(GeckoDriverManager().install())
# 创建一个Selenium WebDriver对象，用于模拟浏览器访问
driver = webdriver.Firefox(service=service)
#要访问的页面
driver.get("https://www.bilibili.com/")
# 获取页面源代码
page = driver.page_source
#  创建BeautifulSoup对象，将HTML内容解析成树状结构
soup1 = BeautifulSoup(page, 'lxml')
# 打印HTML内容
content1 = soup1.prettify()
#print(content1)
for i in soup1.find_all('div',id = 'i_cecream'):
   for j in i.find_all('a',class_ = 'channel-link'):
       print(j.string)
"""

"""
# 设置请求头，模拟浏览器访问，避免被网站识别为爬虫
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'cookie': 'APP_ANON=A=EA6F216F978C9B1C099EDADBFFFFFFFF; els=%7b%22account_type%22%3a%22MSA%22%7d; MUID=3CF49D042282636D31A18E3123FE6200; currentaccount=%7B%22login_hint%22%3A%22M%24EjB4nON4svPU-sOXdu9VFhI0MjA1NTU3MjA2dSgs1EvOz5VYvvrKmR__gYARAGagEwI%22%2C%22account_type%22%3A%22MSA%22%7D; USRLOC=; OptanonAlertBoxClosed=2024-11-22T07:26:46.357Z; msnup=%7B%22cnex%22%3A%22no%22%7D; aace=%7b%22child%22%3a0%2c%22expiredOn%22%3a%222025-09-11T06%3a09%3a36%22%7d; eupubconsent-v2=CQIgXhzQIgXhzAcABBENB-CsAP_AAEPAACiQIhNX_G__bXlj8X53aftkeY1f99h7rsQxBhaJk-4FzJvW_JwX32E7NAz6pqIKmRIAu3DBAQFlHIDURUCgaIgVqSDMaEyUoTNKJ6BEiFMRY2dYCFxvm4lDeQCY5vr991d52B-t7Nr83dTyy4hHv3a5_0S0WAAAAYANDLv9bROb29AOd_x8v4v4_F7pBD-AmADgAZQA6ACKAGfAZYAzMBuYDtoIJggoBBgCDYEIQIVwQuBC8CGYEOYIeAh6BD8A4JA3AAQAAuACgAKgAcAA8ACAAGUANAA1AB4AEQAJgAVQA3gB6AD8AISAQwBEgCOAEsAJoAYYAywBsgDvgHsAfEA-wD9AIBARcBGACNAFBAKuAXMAxQBogDaAG4AOIAh0BIgCdgFDgKRAWwAuQBd4C8wGGgMkAZOAy4BnMDWANZAbeA8cB7QQBVAA4ADwASABGAC2AH8AagA5wCDgE_AKGAdUBF4CPQEigJWATaAp8BYQC6AF1ALyAYEAxABi0DIQMjAZMA0IBowDUwG0ANuAboA4IB2ADugHlAPkAfYA_cCAgEDAIIhgCAARgAqABbADeAKQAagBLQClgHUAReAkUBYgDAgGRgNCAboIAHgAkABqAEYALYAbwBSADUAJaAUsA3gCLwEigMCAaEA3QUAKAFIANQAloB1QEegJFAWIA0IBrwD7BgAkAGoApABqAEtAOqAj0BYgDQgH2DgH4ACIAHAAeABcAEgAOQAfgBGAC2AGgAP4AhABSADNAGoAOcAdwBAICDgIQARGAnwCfgFLAKgAXoA3gB0gDqgHyAQgAj0BIoCVgExAJlATaApABSYCqgFdgLUgXQBdQC9gF9AMCAYgAxYBkIDJgGXgNCAaMA00BqYDXgG0ANsAbcA7AB5QD4gH2QP2A_cCB4EER0EQABcAFAAVAA4ACAAFwAMoAaABqADwAIgATAAqwBcAF0AMQAbwA9AB-gEMARIAlgBNACjAGGAMoAaIA2QB3gD2gH2AfsBFgEYAKCAVcAsQBcwC8gGKANoAbgA4gB1AEOgIvASIAmQBOwChwFNAKsAWKAtgBcAC5AF2gLvAXmAw0BjwDJAGTgMqAZYAy4BnIDVQGsANvAeOA9oB9YEASACEABAAaAA_gCkAGoAOcAnwBSwCxAGEAN4AdUBHoCYgE2gKTAXkAvYBgQDQgGpgNsAbcA6MB2ADygHxAPsAfsBA8CDAEGwIVkIDQACwAKAAuACqAFwAMQAbwA9ACOAHeASkAoIBVwC5gGKANoAdQBTQCxQFogLgAXIAycBnIDVQHjkoEAACAAFgAUAA4ADwAIgATAAqgBcADFAIYAiQBHACjAGyAO8AfgBVwDFAHUAQ6Ai8BIgCxQFsALzAZOAywBnIDWAG3gPaAgeSAOgAOAAuADkAKgAZAA3gCEAFIAL4AagA7gCAAEtAKgAbwA6oCPQEigJWATaApMBewDFgG5AOwAeUA-wB-4EESkDAABcAFAAVAA4ACAAGQANAAeABEACYAFUAMQAfoBDAESAKMAZQA0QBsgDvgH2AfoBFgCMAFBAKuAXMAvIBigDaAG4AQ6Ai8BIgCdgFDgLFAWwAuABcgC7QF5gMNAZIAycBlwDOYGsAayA28B44D2igDUAC4AJAAcgBGACoAGQANoAbwBCACOAEyAKQAagA5wB3AEAAJEAScAloBOwClgFiALqAYAA14BvADqgHbAP-Aj0BIoCYgEygJtAUgAp8BXYC6AF5AL6AYEAxYBk0DUgNTAa8A4IB2ADygHxAPsgfsB-4EDAIHgAA.f_gAD_gAAAAA; _EDGE_S=SID=0EB1DC6E5EEB6C453A0FC9B55FAC6D6B; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+27+2025+14%3A12%3A43+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202501.2.0&isIABGlobal=false&hosts=&consentId=11211ffb-158d-4526-9dca-d4d3177a12ff&interactionCount=3&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0008%3A1%2CV2STACK42%3A0&AwaitingReconsent=false&geolocation=%3B&browserGpcFlag=0&isAnonUser=1; _C_ETH=1'
    }
# 向指定的网站发送GET请求
r = requests.get("https://www.bilibili.com/",headers=headers,timeout=5)
# 检查响应状态码，如果状态码不是 200，会抛出异常
r.raise_for_status()
# 根据响应内容的实际编码设置响应的编码
r.encoding = r.apparent_encoding
# 获取请求的文本内容
#print(r.text)
# 解析HTML内容，会将HTML内容解析成BeautifulSoup对象（解析成树状图）
soup2 = BeautifulSoup(r.text, 'lxml')
# 打印HTML内容
content2 = soup2.prettify()
r.close()
#print(content2)
# 查找所有div标签，并遍历
# for m in soup2.find_all('div',id = 'i_cecream'):
#     #  查找所有a标签
#     for n in m.find_all('a',class_ = 'channel-link'):
#         # 打印a标签中的文本内容
#         print(n.string)
"""

# 爬取豆瓣电影top250
# verify = False ：去掉安全验证
# count = 1
# for start in range(0, 250, 25):
#     url = f"https://movie.douban.com/top250?start={start}"
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }
#     resp = requests.get(url,headers = headers)
#     obj = re.compile(r'<li>.*?<span class="title">(?P<Name>.*?)</span>.*?<br>(?P<Year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<Score>.*?)</span>.*?<span>(?P<Number>.*?)人评价</span>',re.S)
#     result = obj.finditer(resp.text)
#     for it in result:
#         print("序号:{} 电影名:{} 评分:{} 年份:{} 评价人数:{}".format(count,it.group("Name"),it.group("Score"),it.group("Year").strip(),it.group("Number")))
#         count += 1
# resp.close()

# 爬取电影天堂 获取电影中的下载地址
# url = "https://www.dytt8899.com/"
# child_list = []
# f = open("爬虫\文本\下载地址.csv","w",encoding="utf-8")
# csvWriter = csv.writer(f)
# response = requests.get(url)
# response.encoding = "gbk"
# obj = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
# obj1 = re.compile(r"<a href='(?P<href>.*?)'",re.S)
# ob2 = re.compile(r'◎片　　名(?P<Name>.*?)<br />.*?<a href="(?P<downLoad>.*?)">',re.S)
# result = obj.finditer(response.text)
# for it in result:
#     li = it.group("ul")
#     result1 = obj1.finditer(li)
#     for it1 in result1:
#         child_url = url + it1.group("href").strip('/')
#         child_list.append(child_url)
# for href in child_list:
#     child_rep = requests.get(href)
#     child_rep.encoding = "gbk"
#     result3 = ob2.finditer(child_rep.text)
#     for it3 in result3:
#         #print(it3.group("Name")+"下载地址: "+it3.group("downLoad"))
#         dict = it3.groupdict()
#         csvWriter.writerow(dict.values())
# f.close()
# print("Over!")
# response.close()
# child_rep.close()

#  爬取优美图库网的图片
# url = "https://www.umei.cc/gaoxiaotupian/baoxiaotupian/"
# response = requests.get(url)
# response.encoding = "utf-8"
# main_page = BeautifulSoup(response.text,"lxml")
# alist = main_page.find("div",class_="item_list infinite_scroll").find_all("img")
# #print(alist)
# for a in alist:
#     href = a.get('data-original')
#     #print(href)
#     img_resp = requests.get(href)
#     img_resp.content
#     img_name = href.split("/")[-1]
#     with open("爬虫/图片/优美图库网/"+img_name,"wb") as f:
#         f.write(img_resp.content)
# print("下载完成!")
# f.close()
# response.close()
# img_resp.close()

#爬取猪八戒网 并对价格进行排序
# url = "https://www.zbj.com/fw/?k=saas"
# response = requests.get(url)
# print(response.text)
# html = etree.HTML(response.text)
# divs = html.xpath("//div[@positioncode='30003']")
# for div in divs:
#     price = div.xpath("//div[@class='price']/span/text()")
# #print(price)
# price_numbers = [int(p.strip('¥')) for p in price]
# sorted_prices = sorted(price_numbers)
# for p in sorted_prices:
#     print(p)
# response.close()

# 爬取视频网站下载视频
# url = "https://v5-gz-a.douyinvod.com/bc01fe0c7d4e4f5d27f643d195669476/681c25f9/video/tos/cn/tos-cn-ve-15/oYEn3pMAeEhARNwf7DITVZBznhdiiAbqBgHQn3/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1654&bt=1654&cs=0&ds=4&ft=VWi6g76BRR0sLpC3BDj2Nc0iPMgzbLF~QVdU_4m9Cw2JNv7TGW&mime_type=video_mp4&qs=0&rc=NTdlNzZpaThlZWZmOzhpN0BpanE5b3U5cmdueDMzNGkzM0AxYGBfMGM1XzAxY2NhYWBhYSNiY19kMmRzZHJgLS1kLWFzcw%3D%3D&btag=c0000e000b8001&cquery=100y&dy_q=1746670437&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202505081013576FF690603DA5AE44268F"
# response = requests.get(url, stream=True)
# # 以二进制写入模式打开文件
# with open("爬虫/视频/video3.mp4", 'wb') as file:
#     # 逐块写入视频数据
#     for chunk in response.iter_content(chunk_size=8192):
#         if chunk:
#             file.write(chunk)
# print(f"视频下载成功！")

# AES加密/解密
# data = 'youngman is good'
# # key = '1234567890123456'.encode()
# # iv = '456165151222abcd'.encode()
# key = b'#cmZw\xaf-PVg\xed\xa1\xca1\xdc\x8f'
# iv = b'#cmZw\dPVg\xed\xa2\xca3\xdf\x8f'
# # print(key,iv)
# aes_obj = AES.new(key,AES.MODE_CBC,iv)
# # encrypt_data = aes_obj.encrypt(data.encode())
# # print(encrypt_data)
# # base64_encrypt_data = base64.b64encode(encrypt_data)
# # print(base64_encrypt_data)
# # base64_dencrypt_data = base64.b64decode(base64_encrypt_data)
# # print(base64_dencrypt_data)
# base64_dencrypt_data = b"'\xa9\x82\xe6v4\xceOu^lOG\xdc\xc1\xec"
# dencrypt_data = aes_obj.decrypt(base64_dencrypt_data)
# print(dencrypt_data.decode())

# 创建一个简单的 HTTP 服务器
# import socket

# sock = socket.socket()
# sock.bind(("127.0.0.1", 8000))
# sock.listen(3)

# print("服务器已经启动...")
# while 1:
#     conn, addr = sock.accept()
#     data = conn.recv(1024)
#     print("data:", data)
#     conn.send(b"HTTP/1.1 200 ok\r\n\r\n<h1>welcome to MyPage</h1><img src='https://ts2.tc.mm.bing.net/th/id/OIP-C.I2hMkvaohsXA0e8XhPxg_gHaQd?rs=1&pid=ImgDetMain&o=7&rm=3'>")
#     conn.close()

