import requests
from lxml import etree
import re
import execjs

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://qikan.cqvip.com/Qikan/Journal/JournalGuid?from=index",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}

url = "https://qikan.cqvip.com/Qikan/Journal/JournalGuid"
params = {
    "from": "index"
}

# 第一次请求获取初始cookie和页面内容
response = requests.get(url, headers=headers, params=params)

# 获取初始cookie
initial_cookies = {}
for cookie in response.cookies:
    initial_cookies[cookie.name] = cookie.value

print("初始cookies:", initial_cookies)

# 解析页面内容
html = etree.HTML(response.text)
content = html.xpath('//meta/@content')[-1]
ts = html.xpath('//script/text()')[0]

# 读取并修改01-env.js文件
env_file_path = r'c:\lj666\VScode\python\爬虫\前端\JS\中国期刊服务平台(瑞数6)\01-env.js'
with open(env_file_path, 'r', encoding='utf-8') as f:
    env_content = f.read()

# 替换content值
env_content_new = re.sub(
    r'content = ".*?"[;]?',
    f'content = "{content}"', 
    env_content
)

# 写入修改后的内容到01-env.js
with open(env_file_path, 'w', encoding='utf-8') as f:
    f.write(env_content_new)

print("01-env.js 中的 content 已更新")

# 读取并修改02-ts.js文件 - 完全替换文件内容
ts_file_path = r'c:\lj666\VScode\python\爬虫\前端\JS\中国期刊服务平台(瑞数6)\02-ts.js'

# 直接用新内容完全替换原文件内容
with open(ts_file_path, 'w', encoding='utf-8') as f:
    f.write(ts)

print("02-ts.js 文件内容已完全替换")

# 读取所有JS文件内容
with open(r'C:\lj666\VScode\python\爬虫\前端\JS\中国期刊服务平台(瑞数6)\01-env.js', 'r', encoding='utf-8') as f:
    env_js = f.read()
    
with open(r'C:\lj666\VScode\python\爬虫\前端\JS\中国期刊服务平台(瑞数6)\02-ts.js', 'r', encoding='utf-8') as f:
    ts_js = f.read()

with open(r'C:\lj666\VScode\python\爬虫\前端\JS\中国期刊服务平台(瑞数6)\03-auto.js', 'r', encoding='utf-8') as f:
    auto_js = f.read()

# 合并所有JS代码并执行
js_code = env_js + ";\n" + ts_js + ";\n" + auto_js + ";\n" + "document.cookie;"

ctx = execjs.compile(js_code)
cookie_result = ctx.eval("document.cookie")
print("JS生成的cookie值:", cookie_result)

# 使用正则表达式动态提取 cookie 名称和值
cookie_match = re.search(r'([^=]+)=([^;]+)', cookie_result)
if cookie_match:
    cookie_name = cookie_match.group(1).strip()
    cookie_value = cookie_match.group(2).strip()
    cookie = {
        cookie_name: cookie_value
    }
    print(f"动态获取的 Cookie: {cookie_name}={cookie_value}")
else:
    print("未找到有效的 Cookie")
cookie_dict = {
    cookie_name: cookie_value
}

# 合并所有cookies
final_cookies = {}
final_cookies.update(initial_cookies)
final_cookies.update(cookie_dict)

print("最终cookies:", final_cookies)

# 使用完整cookie发送最终请求
response = requests.get(url, headers=headers, cookies=final_cookies, params=params)
print("最终响应状态码:", response.status_code)
print("最终响应内容长度:", len(response.text))
response.close()