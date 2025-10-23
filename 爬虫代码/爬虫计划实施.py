import base64
import os
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
from lxml import etree
from bs4 import BeautifulSoup
import cv2
import numpy as np
from PIL import Image
import base64
import io
from DrissionPage import ChromiumPage
from DrissionPage.common import Keys 
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# day01 爬取百度搜索标题与链接  Selector和Xpath
# url = 'https://www.baidu.com/'
# headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# response = requests.get(url = url,headers=headers)
# html = response.text
# selector = parsel.Selector(html)
# title = selector.css('head > title::text').get()
# print(title)
# hrefs = selector.css('#hotsearch-content-wrapper > * > a::attr(href)').getall()
# for href in hrefs:
#     print(href)
# tree = etree.HTML(html)
# titles = tree.xpath('/html/head/title')
# for title in titles:
#     print(title.text)
# hrefs = tree.xpath('/html/body/div[1]/div[2]/div[3]/div/div/div[5]/ul/li/a/@href')
# for href in hrefs:
#     print(href)


# day02 爬取豆瓣Top250（电影名、评分、短评） BeautifulSoup与正则表达式
# url = 'https://movie.douban.com/top250?start=0'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# response = requests.get(url=url,headers=headers)
# html = response.text
# soup = BeautifulSoup(html,'lxml')
# ol = soup.find('ol',class_ ='grid_view')
# hd_list = ol.find_all('div',class_='hd')
# bd_list = ol.find_all('div',class_='bd')
# for hd,bd in zip(hd_list,bd_list):
#     name = hd.find('span', class_='title').get_text()
#     span_list = bd.find('div').find_all('span')
#     rating = span_list[1].get_text()
#     number = span_list[3].getText()
#     print(name,rating,number)
# print('下面是re表达式......')
# obj = re.compile(r'<li>.*?<span class="title">(?P<Name>.*?)</span>.*?<span class="rating_num" property="v:average">(?P<Rating>.*?)</span>.*?<span>(?P<Number>.*?)人评价</span>',re.S)
# result = obj.finditer(html)
# for it in result:
#     print("电影名:{} 评分:{} 评价人数:{}".format(it.group("Name"),it.group("Rating"),it.group("Number")))


# edge_options = Options()
# edge_options.add_argument("--headless")  # 启用无头模式
# driver = webdriver.Edge(service=Service('爬虫\edgedriver_win64\msedgedriver.exe'), options=edge_options)
# driver.get("https://www.baidu.com")
# print(driver.title)
# driver.quit()


# day03 爬取网易新闻标题和链接 XPath + lxml精确定位
# url = 'https://news.163.com/'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# response = requests.get(url=url,headers=headers)
# html = response.text
# tree = etree.HTML(html)
# titles = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[5]/div/ul/li/div/div/a/text()')
# hrefs = tree.xpath('/html/body/div[1]/div[3]/div[2]/div[3]/div[2]/div[5]/div/ul/li/div/div/a/@href')
# for title,href in zip(titles,hrefs):
#     print(title,href)


# day04 模拟知乎登录并抓取关注问题标题 Headers伪装、代理IP、Session保持
# session = requests.Session()
# url = 'https://www.zhihu.com/people/13-59-56-15'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }
# cookies = {
#     "_xsrf": "SObfzrBc0nH8aq8EYYQPsHtj4eosl4am",
#     "_zap": "d5851893-dc53-491d-82df-51b21d6cf77e",
#     "d_c0": "AEASmownBxqPThLEfkbHEoiGjOBwz9O0snU=|1739936728",
#     "__snaker__id": "LCLZiBqScHGFfw40",
#     "__zse_ck": "004_ceP3HCHAdvZYgjBNbsd8HcgYhIhGYZZ4=/o6hplWjm1fEQLSMx1PvLiNk0EucW/7KmOwDNjEXyYFh2nZj2mpXAHtHu=HD9nIdkep1R=tVzZTqb6zdq6UALX90fZljYRk-cfS4Muqcr5RKgEBBN2SCMTC/xuyN1/UjV7JGwwvf6cMzXsSDWM6tH6lMEtIkdeLpvQKRy1mTNXGkjH8sBY7Hb3nDAidFbyBZzQGD5SIl5QE51QT2MRCaoQCtbiF5KQwE",
#     "Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49": "1760243355,1760529822,1760773610,1760876659",
#     "HMACCOUNT": "F3736FE6F8274D41",
#     "DATE": "1746454516992",
#     "crystal": "U2FsdGVkX1+sGHLGP9Us9sdfmGfCR378IaepxZLH23TZNENCdly8vOoWLi+uaa/bZtJVWwbmU4nu3VUVp3x5kwxzHadznqAjUO5Y7TgSaPNWVPlJc+SRlQAW1WOaZGIDA6GAMpHpNrcDB+LE0SBTQMf98TxNbYf7SX9G/YWLBAIBgYJnF8Btg3hpbRlXLElU0uX1FDnuEnAspccM2fIpnRp5Sj8G+W8Bw52dn/cX2F6OqPSFo8y5wj8mjlnsg1kA",
#     "SESSIONID": "xVnIjqCiwu6JeDrHaSyQwxn3timJPr8HEVFwWgKLpMd",
#     "JOID": "U1wQBUtfDQE1xBtvZsiulkmydSJ4Ilpseq9vLQwpfTZ8p14YL6mT8VrAH21jW-BynkIuhmacIpgGEurmNBTF-zA=",
#     "osd": "UFwUC0JcDQU7zRhvYsanlUm2eyt7Il5ic6xvKQIgfjZ4qVcbL62d-FnAG2NqWOB2kEsthmKSK5sGFuTvNxTB9Tk=",
#     "gdxidpyhxdE": "JVrybe5aaVHM80d%2BfVN8CRkHDf6fHtONa7ZOtgeMd%2BnSGdr7rbsW%2FmjIg9ny%2BVgRGqRiOX3YZHyWg5%2FaSiw2ZUoAU32QwWljW%5C4hexVlAjQXhTXGYPndxisqXeAhGHbTbEWyoiQh8u9ipdk5rJaSVq75JG%5Cocp5uKJrnB5%2BXqcPP7pjA%3A1760927862557",
#     "cmci9xde": "U2FsdGVkX19Hh//VTlEHv5Bvb4Wp7RZZTe8SmnEEmxSkkcNgWywZBYssM7FYsvXPyJrXVuM+PrSiGB1E9+O0vg==",
#     "pmck9xge": "U2FsdGVkX1+P5SKsZYYxHyZC44rwK7eH4MrGkZ/BL4Y=",
#     "assva6": "U2FsdGVkX1+jiavgzQJLU0Da1aNYg+hV2bXrqSaAZwo=",
#     "assva5": "U2FsdGVkX1/O7rc6nty7sXqgwyM9gnggevfaOedw5pp14e6ldzh2M6Esi3iN1JgkJm/p+SEurXhbFtAPRdvodA==",
#     "vmce9xdq": "U2FsdGVkX1+wASVqvEtVOy6ybBB+aFRlcckhStTdPDdeIay3ve8yR87TbQhg2PtHSWrAI3I74/ewEEfIRdUWx7+YH6iQ9WCi1jm8wf2f6EMdyStwqB9/7Gl11DeW86A4Yo9t+HxaPhLjMIMJdL6QnnUvQ8+5GKl2hC3JmATAp7I=",
#     "captcha_session_v2": "2|1:0|10:1760927311|18:captcha_session_v2|88:YXRjcWhBZXpxNWlLeUVrWXhFdWk1d0FhMGlsdzAyTmtRL2FLc2piS3dYMEg4TzQxWVpMZnJ2b25LK1NMeWExTQ==|f516d78da5d38882e4accff274cd0547cabb293752f092bc4d59c83d3a2dc243",
#     "captcha_ticket_v2": "2|1:0|10:1760927320|17:captcha_ticket_v2|728:eyJ2YWxpZGF0ZSI6IkNOMzFfZk1FeWhlVERyVUliVEVKU0h6aGJtOWRUSnZpNWYxU3lWSEFITEU1OHE1S192TE4qQ252OWxJMVBfbVcuZlZzUGZBOVpoZEZ0MXR0TlBIZ2VqZzUqS29JYkpNZ05EMUZYLlpNd0hKejMuUThaMHFhYkVhLi52LkR2ZUVjcTQxZXNaVm04eHBKcmprWjBBSTh4YWpVMm4wNEN1MSpLTHJFUWJ0eS5ZMmxaT0ZVOFZOSjhpUVFuNDlCc2pub3dMQjE2d1lkWk1ndG1uYip1c0tvM1B2ME9HQSpxWGhick1HR2hsKnpYWExsdkdyM0xvTGZCMDRGTVlOcWlMS2VvQnhWTGJEa2h2cGtlX1JuclhKMk1sZ1Z5VlY0Z2VQb28ya0dXdEhpME9VeDlfdzB0cVNKMDR0TS5yV1YyVnFMNXcwbCpReG5aQ0dIR2xSOFlTQUJ6Y2hxSUtQeUt6bFdSallxU19UbEFQb2RIdGc4YmRqQkJfOWFkNWZiQzZHQ19YYXYqalpnRiptNDZhMjZOdCozLjBwNGlyTlh5RmEwWVR1bGpZOXdXSXV0ZEZ1VzNWMWFjdW5NbWRsYS5VMVY4Z2diWFFNSkk2NE1RQUpBaWRlX3ZxWVdqWEc4dFl0MGx0M0YxOEJJLlIxdUJxT1h5NXFFZl9sdTJhckd1RXBlV1pDSVZzYWJxLmc3N192X2lfMSJ9|6fa47d0e187177bfa5b3045b13e51e33f251509941a650c728227cdd9b9ba9ba",
#     "z_c0": "2|1:0|10:1760927336|4:z_c0|92:Mi4xOFVMOFZnQUFBQUFBUUJLYWpDY0hHaVlBQUFCZ0FsVk5hT3ppYVFBS3dMYTB3ODdBdHVWTzZqeXBSZDlZdTF3NmxB|605da131daf9d9c591b82087a0072720580efede7f90a2acd5d8f72ead125b49",
#     "q_c1": "d07dc1c5a35b41ca92a6258296ce8c3c|1760927336000|1760927336000",
#     "BEC": "7e33fec1f95d805b0b89c2974da3470f",
#     "Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49": "1760930521"
# }
# session.headers.update(headers)
# session.cookies.update(cookies)
# response = session.get(url=url)
# print(response.text)


# 自动刷视频
# edge_options = Options()
# edge_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 关键两行：排除 enable-logging 并设置日志级别
# edge_options.add_argument("--log-level=3")  # 0=INFO, 1=WARNING, 2=LOG_ERROR, 3=LOG_FATAL
# driver = webdriver.Edge(service=Service('爬虫\edgedriver_win64\msedgedriver.exe'), options=edge_options)
# driver.get('https://www.douyin.com/?recommend=1')
# time.sleep(2)
# actions = ActionChains(driver)
# for i in range(20):
#     actions.send_keys(Keys.DOWN).perform()
#     time.sleep(5)


# day05 爬取京东评论（多页采集） Cookies机制、验证码识别思路
# edge_options = Options()
# edge_options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 关键两行：排除 enable-logging 并设置日志级别
# edge_options.add_argument("--log-level=3")  # 0=INFO, 1=WARNING, 2=LOG_ERROR, 3=LOG_FATAL
# driver = webdriver.Edge(service=Service('爬虫\edgedriver_win64\msedgedriver.exe'), options=edge_options)

# dp = ChromiumPage()
# dp.get("https://item.jd.com/10127955410850.html")
# time.sleep(1)
# dp.ele('css:.login-btn').click()
# time.sleep(1)
# dp.ele('css:#loginname').input('12345678910')
# dp.ele('css:#nloginpwd').input('1234')
# time.sleep(1)
# dp.ele('css:#loginsubmit').click()
# time.sleep(2)
# # TODO 滑块验证
# # slider_selectors = ['css:.move-img'] 
# # bg_img_element = page.ele('css:#main_img', timeout=3)
# # slide_img_element = page.ele('css:#slot_img', timeout=3)

# # 改进的水平移动版滑块验证码处理函数
# def solve_slider_captcha_horizontal(slider_css,bg_img_css,slider_img_css,page):
#     try:
#         print("开始查找滑块验证码元素...")
        
#         # 查找滑块元素
#         slider = page.ele(slider_css, timeout=5)
#         if not slider:
#             print("未找到滑块元素")
#             return False
        
#         print("找到滑块验证码，开始处理...")
        
#         # 查找背景图和滑块图
#         bg_img_element = page.ele(bg_img_css, timeout=3)
#         slide_img_element = page.ele(slider_img_css, timeout=3)
        
#         if not bg_img_element or not slide_img_element:
#             print("未找到验证码图片元素")
#             return False
        
#         # 获取图片的src
#         bg_src = bg_img_element.attr('src')
#         slide_src = slide_img_element.attr('src')
        
#         # 下载图片数据
#         bg_data = None
#         slide_data = None
        
#         # 处理背景图
#         if bg_src and bg_src.startswith('data:image'):
#             # base64格式
#             bg_data = base64.b64decode(bg_src.split(',')[1])
#             print("背景图为base64格式")
        
#         # 处理滑块图
#         if slide_src and slide_src.startswith('data:image'):
#             # base64格式
#             slide_data = base64.b64decode(slide_src.split(',')[1])
#             print("滑块图为base64格式")
        
#         if not bg_data or not slide_data:
#             print("无法获取图片数据")
#             return False
            
#         # 将图片数据转换为OpenCV格式
#         try:
#             bg_array = np.frombuffer(bg_data, np.uint8)
#             slide_array = np.frombuffer(slide_data, np.uint8)
            
#             bg_img = cv2.imdecode(bg_array, cv2.IMREAD_COLOR)
#             slide_img = cv2.imdecode(slide_array, cv2.IMREAD_COLOR)
            
#             if bg_img is None or slide_img is None:
#                 print("图片解码失败")
#                 return False
                
#             print(f"图片解码成功，背景图尺寸: {bg_img.shape}, 滑块图尺寸: {slide_img.shape}")
#         except Exception as e:
#             print(f"图片解码时出错: {e}")
#             return False
        
#         # 使用模板匹配找到滑块位置（改进版）
#         try:
#             # 转换为灰度图
#             bg_gray = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
#             slide_gray = cv2.cvtColor(slide_img, cv2.COLOR_BGR2GRAY)
            
#             # 对滑块图片进行预处理，创建掩码
#             _, mask = cv2.threshold(slide_gray, 1, 255, cv2.THRESH_BINARY)
            
#             # 尝试多种匹配方法以提高准确性
#             methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED]
#             best_result = 0
#             best_loc = (0, 0)
            
#             for method in methods:
#                 try:
#                     result = cv2.matchTemplate(bg_gray, slide_gray, method, mask=mask)
#                     _, max_val, _, max_loc = cv2.minMaxLoc(result)
                    
#                     if max_val > best_result:
#                         best_result = max_val
#                         best_loc = max_loc
                        
#                 except Exception as e:
#                     print(f"匹配方法 {method} 出错: {e}")
#                     continue
            
#             # 获取最佳匹配位置
#             x, y = best_loc
#             print(f"最佳匹配度: {best_result}, 位置: ({x}, {y})")
            
#             # 使用匹配结果计算拖拽距离
#             target_x = x
                
#         except Exception as e:
#             print(f"模板匹配时出错: {e}")
#             target_x = 200  # 使用默认值
        
#         # 计算需要拖拽的距离
#         drag_distance = target_x + 5  # 增加少量补偿确保完全覆盖缺口
        
#         if drag_distance <= 0 or drag_distance > 300:  # 设置合理范围
#             drag_distance = 200  # 使用默认值
            
#         print(f"需要拖拽的距离: {drag_distance}")
        
#         # 执行拖拽 - 只进行水平移动
#         try:
#             import random
            
#             # 构造偏移量列表 - 只在水平方向移动
#             offsets = []
#             remaining = drag_distance
            
#             while remaining > 0:
#                 if remaining > 50:
#                     step = min(random.randint(15, 25), remaining)
#                 elif remaining > 10:
#                     step = min(random.randint(8, 15), remaining)
#                 else:
#                     step = min(random.randint(3, 8), remaining)
                
#                 # 垂直方向移动设为0，只进行水平移动
#                 offsets.append((step, 0))
#                 remaining -= step
            
#             # 微调 - 仍然只进行水平移动
#             offsets.append((-2, 0))
#             offsets.append((3, 0))
            
#             print(f"拖拽偏移量: {offsets}")
#             slider.drag(drag_distance,0)
#             print("拖拽执行完成")
#         except Exception as e:
#             print(f"拖拽执行失败: {e}")
#             return False
        
#         # 等待验证结果
#         time.sleep(3)
        
#         # 检查验证是否成功
#         try:
#             slider_check = page.ele(slider_css, timeout=1)
#             if slider_check:
#                 print("验证失败，滑块仍在原位")
#                 return False
#             else:
#                 print("滑块验证成功")
#                 return True
#         except:
#             print("滑块验证成功")
#             return True
            
#     except Exception as e:
#         print(f"处理滑块验证码时出错: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# # 尝试使用改进的水平移动版方法处理滑块验证码
# print("尝试使用改进的水平移动版方法自动处理滑块验证码...")
# slider_css = 'css:.move-img'
# bg_img_css = 'css:#main_img'
# slider_img_css = 'css:#slot_img'
# captcha_solved = solve_slider_captcha_horizontal(slider_css,bg_img_css,slider_img_css,dp)

# # # TODO 点选验证
# # # 添加点选验证码处理函数
# def solve_click_captcha(page, color_based=False):
#     """
#     处理点选验证码（在大图中找到与小图最匹配的位置并点击）
#     :param page: DrissionPage页面对象
#     :param color_based: 是否使用基于颜色的匹配方法
#     :return: 是否处理成功
#     """
#     try:
#         print("开始处理点选验证码...")
        
#         # 等待验证码元素出现
#         question_image = page.ele('css:#cpc_img', timeout=10)  # 大图
#         target_image = page.ele('css:.pcp_showPicture.tip_pic', timeout=10)  # 小图
        
#         if not question_image:
#             print("未找到题目图片元素（大图）")
#             return False
            
#         if not target_image:
#             print("未找到目标图片元素（小图）")
#             return False
            
#         # 获取大图和小图的src
#         question_src = question_image.attr('src')
#         target_src = target_image.attr('src')
        
#         print(f"大图src长度: {len(question_src) if question_src else 0}")
#         print(f"小图src长度: {len(target_src) if target_src else 0}")
        
#         # 下载大图和小图数据
#         question_data = None
#         target_data = None
        
#         if question_src and question_src.startswith('data:image'):
#             question_data = base64.b64decode(question_src.split(',')[1])
#             print("大图为base64格式")
#         else:
#             print("大图不是base64格式或无法获取")
#             return False
            
#         if target_src and target_src.startswith('data:image'):
#             target_data = base64.b64decode(target_src.split(',')[1])
#             print("小图为base64格式")
#         else:
#             print("小图不是base64格式或无法获取")
#             return False
        
#         if not question_data or not target_data:
#             print("无法获取验证码图片数据")
#             return False
        
#         # 使用OpenCV进行模板匹配
#         try:
#             # 将图片数据转换为OpenCV格式
#             question_array = np.frombuffer(question_data, np.uint8)
#             target_array = np.frombuffer(target_data, np.uint8)
            
#             question_img = cv2.imdecode(question_array, cv2.IMREAD_COLOR)
#             target_img = cv2.imdecode(target_array, cv2.IMREAD_COLOR)
            
#             if question_img is None or target_img is None:
#                 print("图片解码失败")
#                 return False
                
#             print(f"图片解码成功，大图尺寸: {question_img.shape}, 小图尺寸: {target_img.shape}")
            
#             if color_based:
#                 # 基于颜色的匹配方法
#                 print("使用基于颜色的匹配方法")
                
#                 # 直接在彩色图像上进行模板匹配
#                 result = cv2.matchTemplate(question_img, target_img, cv2.TM_CCOEFF_NORMED)
                
#                 # 设置匹配阈值
#                 threshold = 0.7  # 提高阈值，减少误匹配
                
#                 # 找到最佳匹配位置（只取一个）
#                 _, max_val, _, max_loc = cv2.minMaxLoc(result)
                
#                 if max_val < threshold:
#                     print("匹配度不足，无法识别目标")
#                     # 尝试另一种基于颜色的方法：在特定颜色空间中匹配
#                     print("尝试在HSV颜色空间中匹配...")
#                     hsv_question = cv2.cvtColor(question_img, cv2.COLOR_BGR2HSV)
#                     hsv_target = cv2.cvtColor(target_img, cv2.COLOR_BGR2HSV)
                    
#                     # 在HSV空间中进行匹配
#                     result_hsv = cv2.matchTemplate(hsv_question, hsv_target, cv2.TM_CCOEFF_NORMED)
#                     _, max_val, _, max_loc = cv2.minMaxLoc(result_hsv)
                    
#                     if max_val < threshold:
#                         print("HSV空间匹配也失败了")
#                         return False
#                     else:
#                         print(f"HSV空间匹配成功，匹配度: {max_val:.3f}")
#                 else:
#                     print(f"BGR空间匹配成功，匹配度: {max_val:.3f}")
#             else:
#                 # 转换为灰度图进行匹配（原有方法）
#                 print("使用基于灰度的匹配方法")
#                 question_gray = cv2.cvtColor(question_img, cv2.COLOR_BGR2GRAY)
#                 target_gray = cv2.cvtColor(target_img, cv2.COLOR_BGR2GRAY)
                
#                 # 模板匹配
#                 result = cv2.matchTemplate(question_gray, target_gray, cv2.TM_CCOEFF_NORMED)
                
#                 # 设置匹配阈值
#                 threshold = 0.7  # 提高阈值，减少误匹配
                
#                 # 找到最佳匹配位置（只取一个）
#                 _, max_val, _, max_loc = cv2.minMaxLoc(result)
                
#                 if max_val < threshold:
#                     print("匹配度不足，无法识别目标")
#                     return False
            
#             # 计算中心点
#             h, w = target_img.shape[:2]
#             center_x = max_loc[0] + w // 2
#             center_y = max_loc[1] + h // 2
            
#             print(f"找到最佳匹配位置: ({max_loc[0]}, {max_loc[1]}), 匹配度: {max_val:.3f}, 中心点: ({center_x}, {center_y})")
            
#         except Exception as e:
#             print(f"模板匹配时出错: {e}")
#             import traceback
#             traceback.print_exc()
#             return False
        
#         # 获取大图在页面中的位置
#         try:
#             rect = question_image.rect
            
#             if hasattr(rect, 'location'):
#                 question_left, question_top = rect.location
#             else:
#                 print(f"无法识别的rect类型: {type(rect)}, 内容: {rect}")
#                 return False
                
#             print(f"大图位置: 左={question_left}, 上={question_top}")
            
#         except Exception as e:
#             print(f"获取元素位置失败: {e}")
#             return False
        
#         # 计算实际点击坐标
#         click_x = question_left + center_x
#         click_y = question_top + center_y
#         # Deleted: breakpoint()
#         print(f"最终点击坐标: 页面坐标({click_x}, {click_y})")
        
#         # 使用JavaScript精确点击（推荐）
#         try:
#             page.run_js(f'''
#                 var evt = new MouseEvent('click', {{
#                     bubbles: true,
#                     cancelable: true,
#                     clientX: {click_x},
#                     clientY: {click_y}
#                 }});
#                 document.elementFromPoint({click_x}, {click_y}).dispatchEvent(evt);
#             ''')
#             print("✓ 成功执行JavaScript点击")
            
#         except Exception as js_e:
#             print(f"✗ JavaScript点击失败: {js_e}")
#             return False
        
#         # 等待验证结果
#         time.sleep(2)
        
#         # 可选：检查是否跳转或关闭弹窗
#         try:
#             if page.ele('css:.captcha-container') is None:
#                 print("✓ 验证通过，弹窗已消失")
#                 return True
#             else:
#                 print("⚠️ 验证未通过，弹窗仍在")
#                 return False
#         except:
#             print("✓ 验证完成")
#             return True
            
#     except Exception as e:
#         print(f"处理点选验证码时出错: {e}")
#         import traceback
#         traceback.print_exc()
#         return False

# if captcha_solved:
#     # 尝试处理点选验证码
#     click_captcha_solved = solve_click_captcha(dp)
# else :
#     print('滑块验证失败，程序已退出...')
#     exit()

# if not click_captcha_solved:
#     print("点选验证码处理失败，等待手动处理...")
#     exit()
# # ... existing code ...
# dp.listen.start('client.action')
# time.sleep(2)
# down = dp.ele('css:.all-btn')
# dp.scroll.to_see(down)
# time.sleep(2)
# dp.ele("css:.all-btn .arrow").click()
# time.sleep(2)

# # 定位到评论容器元素
# comment_container = None
# for _ in range(10):  # 等待评论容器出现
#     try:
#         comment_container = dp.ele( 'css:._list_1ygkr_67', timeout=0.5)
#         if comment_container:
#             break
#     except:
#         time.sleep(0.5)
#         continue

# all_comments = []
# number = 0
# for i in range(5):
#     try:
#         res = dp.listen.wait(timeout=3)
#         data = res.response.body
#         comment_list = data['result']['floors'][2]['data']
#         for comments in comment_list:
#             try:
#                 comment = comments['commentInfo']['commentData']
#                 if comment not in all_comments:
#                      all_comments.append(comment)
#                      number += 1
#             except:
#                 pass
#     except:
#                 pass
    
#     # 在评论区域内部滚动
#     if comment_container:
#         comment_container.scroll.down(200)
#     else:
#         dp.scroll.down(300)
#     time.sleep(1)  # 等待加载

# # 打印所有收集到的评论
# for comment in all_comments:
#     print(comment)
# print(f"共抓取{number}条数据")


# day06 抓取哔哩哔哩排行榜接口数据并保存 AJAX与接口抓取
url = 'https://api.bilibili.com/pgc/season/rank/web/list?day=3&season_type=4&web_location=333.934&w_rid=7ffe4b731aeb63773f5e092069ce7c16&wts=1761124811'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response = requests.get(url=url,headers=headers)
print(response.text)
response.close()