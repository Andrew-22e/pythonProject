import requests
import execjs

# 读取JavaScript文件内容
with open(r'c:\lj666\VScode\python\爬虫\前端\JS\拼多多逆向webpack\env.js', 'r', encoding='utf-8') as f:
    env_js = f.read()

with open(r'c:\lj666\VScode\python\爬虫\前端\JS\拼多多逆向webpack\mod1.js', 'r', encoding='utf-8') as f:
    mod1_js = f.read()

with open(r'c:\lj666\VScode\python\爬虫\前端\JS\拼多多逆向webpack\mod2.js', 'r', encoding='utf-8') as f:
    mod2_js = f.read()

with open(r'c:\lj666\VScode\python\爬虫\前端\JS\拼多多逆向webpack\loader.js', 'r', encoding='utf-8') as f:
    loader_js = f.read()

with open(r'c:\lj666\VScode\python\爬虫\前端\JS\拼多多逆向webpack\main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()


# 创建JavaScript运行环境
ctx = execjs.compile(env_js + "\n" + loader_js + "\n" + mod1_js + "\n" + mod2_js + "\n" + main_js)
# 调用get_anti_content方法获取anti_content值
anti_content = ctx.call('getAntiContent')
print(anti_content)


headers = {
    "Accept": "application/json, text/javascript",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.pinduoduo.com",
    "Pragma": "no-cache",
    "Referer": "https://www.pinduoduo.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}

url = "https://apiv2.pinduoduo.com/api/gindex/tf/query_tf_goods_info"
params = {
    "tf_id": "TFRQ0v00000Y_13398",
    "page": "1",
    "size": "39",
    "anti_content": anti_content  # 使用动态生成的anti_content
}

response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)
response.close()


