# 该网站不允许调试

import requests
import json
import csv
import execjs

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://dewu.com",
    "Referer": "https://dewu.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "traceparent": "00-f5328e836887137b0278dffd6f75cc90-81f41dfdc03145b5-01"
}
cookies = {
    "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%221984a862daf1ad-03453ffb814c9fe-4c657b58-1327104-1984a862db014c5%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTk4NGE4NjJkYWYxYWQtMDM0NTNmZmI4MTRjOWZlLTRjNjU3YjU4LTEzMjcxMDQtMTk4NGE4NjJkYjAxNGM1In0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221984a862daf1ad-03453ffb814c9fe-4c657b58-1327104-1984a862db014c5%22%7D"
}
url = "https://app.dewu.com/api/v1/h5/commodity-pick-interfaces/pc/pick-rule-result/feeds/info"
# 编译JS代码
js_code =  execjs.compile(open('爬虫/前端/JS/得物(中等).js',encoding='utf-8').read())

data = {
    #"sign": "0e5d10fb111f2afef6ac0a1776187e23", # 签名
    "pickRuleId": 644440, # 修改商品id （修改地方）
    "pageNum": 1, # 修改页码 （修改地方）
    "pageSize": 24,
    "filterUnbid": True,
    "showCspu": True
}
# 获取sign加密参数
sign = js_code.call('c', data)
# 将获取的sign参数添加到data中
data['sign'] = sign
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

# print(response.text)
# print(response)

products = []
# 获取商品信息
json_data = response.json()
info_list = json_data['data']['list']
# for循环遍历
for info in info_list:
    title = info['title']
    price = info['price'] // 100
    imgUrl = info['logoUrl']
    products.append({
        'title': title,
        'price': price,
        'img': imgUrl
    })
    #print("标题：",title,"价格：",price,"图片：",img)
# 按价格排序（从低到高）
products.sort(key=lambda x: x['price'])
# 保存到CSV文件
with open(f'爬虫\文本\得物商品数据.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['title', 'price', 'img']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for product in products:
        writer.writerow(product)

print("\n商品信息已保存到csv文件中")