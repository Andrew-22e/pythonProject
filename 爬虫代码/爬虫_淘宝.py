import requests
import time
import hashlib
import re
import json
import csv

# 无论是否登录，淘宝的token都会定期变化，这是网站的安全机制。建议在实际使用时增加token有效性的检查和自动更新机制。
# 每过一段时间，token值会发生变化，需要进行修改，token 的值通常与 cookies 中的 _m_h5_tk 相关，它是 _m_h5_tk 值的第一部分（第一个下划线前的部分
# 结果获取具有时效性，cookies的值会发生改变，data也需要根据cookie来进行修改
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "referer": "https://uland.taobao.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
#cookies（修改地方）
cookies = {
    "t": "ee35c4bd5fff03e8843256a47510a4c2",
    "thw": "cn",
    "cna": "AemUIGlAR0wCAXjOrk2tvHUJ",
    "cookie2": "1944544d603870ca50cf84604c8350cf",# 变化
    "_tb_token_": "e63d3655e7ed3",# 变化
    "xlly_s": "1",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "46569fb209d3d0dfbd1d0e818988096a_1753516219904",# 变化
    "_m_h5_tk_enc": "67254c6b216902d21b706592ae0ceaf8",# 变化
     "tfstk": "gABIKJ2-220BmK9-VBqZhkEtH795Fly4A0tRmgHE2ppKeu_P7TRJzWbWNa7Mw9JFYNTRuNTKU7YEFLs5ra75qkxJyaQWz6Pa3MjHELU2P-yVxgwR6TXBe4S9K3oUMFCu3MjnXDg801eqV3bUoLhJyap96nxkebdRyCp9S3x-J3HLflTMVbhpvXKTB3xr9LpRyGE6qFKpeQQRXb7Y5hVBJMZbhkiL-5LfvFM-eOekOEsKaYHRCHOCJML1bGW6ABTvwUK3y9QN29WHs5cwEG5fP_QY7X8dGn_6g6ajdZ_H2N9FHuVHsQB5FhfgPbTfwM5cwCZLpG9BRQBNWmlMd_QhFBfIqoj9pNfDoBFgSh6F3QTD1VUdbGTpG__USYLFGGQ6gOuZ3KCc5TOvHg-r3Et4rbi6iYt6ulZsZbjQRVWqULffbBKMbtr_f2Gk9hx6ulZsZbApjhR4flgIZ", # 变化
    "isg": "BGFhWSh0rbQGlQFJyOCBLrnzcC17DtUAnhSqdMM2UGjHKoH8C18t0EdsjF6sym04" # 变化
}
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
token = '46569fb209d3d0dfbd1d0e818988096a'  # 最主要的修改地方(如果结果返回非法请求)
u = int(time.time() * 1000)
s = '12574478'
#data（修改地方）
data = '{\"appId\":\"43356\",\"params\":\"{\\\"device\\\":\\\"HMA-AL00\\\",\\\"isBeta\\\":\\\"false\\\",\\\"grayHair\\\":\\\"false\\\",\\\"from\\\":\\\"nt_history\\\",\\\"brand\\\":\\\"HUAWEI\\\",\\\"info\\\":\\\"wifi\\\",\\\"index\\\":\\\"4\\\",\\\"rainbow\\\":\\\"\\\",\\\"schemaType\\\":\\\"auction\\\",\\\"elderHome\\\":\\\"false\\\",\\\"isEnterSrpSearch\\\":\\\"true\\\",\\\"newSearch\\\":\\\"false\\\",\\\"network\\\":\\\"wifi\\\",\\\"subtype\\\":\\\"\\\",\\\"hasPreposeFilter\\\":\\\"false\\\",\\\"prepositionVersion\\\":\\\"v2\\\",\\\"client_os\\\":\\\"Android\\\",\\\"gpsEnabled\\\":\\\"false\\\",\\\"searchDoorFrom\\\":\\\"srp\\\",\\\"debug_rerankNewOpenCard\\\":\\\"false\\\",\\\"homePageVersion\\\":\\\"v7\\\",\\\"searchElderHomeOpen\\\":\\\"false\\\",\\\"search_action\\\":\\\"initiative\\\",\\\"sugg\\\":\\\"_4_1\\\",\\\"sversion\\\":\\\"13.6\\\",\\\"style\\\":\\\"list\\\",\\\"ttid\\\":\\\"600000@taobao_pc_10.7.0\\\",\\\"needTabs\\\":\\\"true\\\",\\\"areaCode\\\":\\\"CN\\\",\\\"vm\\\":\\\"nw\\\",\\\"countryNum\\\":\\\"156\\\",\\\"m\\\":\\\"pc_sem\\\",\\\"page\\\":\\\"1\\\",\\\"n\\\":48,\\\"q\\\":\\\"%E9%94%AE%E7%9B%98\\\",\\\"qSource\\\":\\\"url\\\",\\\"pageSource\\\":\\\"tbpc.pc_sem_alimama/a.search_manual.0\\\",\\\"tab\\\":\\\"all\\\",\\\"pageSize\\\":48,\\\"totalPage\\\":100,\\\"totalResults\\\":4800,\\\"sourceS\\\":\\\"0\\\",\\\"sort\\\":\\\"_coefp\\\",\\\"bcoffset\\\":\\\"\\\",\\\"ntoffset\\\":\\\"\\\",\\\"filterTag\\\":\\\"\\\",\\\"service\\\":\\\"\\\",\\\"prop\\\":\\\"\\\",\\\"loc\\\":\\\"\\\",\\\"start_price\\\":null,\\\"end_price\\\":null,\\\"startPrice\\\":null,\\\"endPrice\\\":null,\\\"itemIds\\\":null,\\\"p4pIds\\\":null,\\\"categoryp\\\":\\\"\\\",\\\"myCNA\\\":\\\"AemUIGlAR0wCAXjOrk2tvHUJ\\\",\\\"clk1\\\":\\\"4cbf7880f6a5b703a56ef44c6b4854e6\\\",\\\"refpid\\\":\\\"mm_2898300158_3078300397_115665800437\\\"}\"}"}'
l = token + "&" + str(u) + "&" + s + "&" + data
string = hashlib.md5(l.encode("utf-8")).hexdigest()

params = {
    "jsv": "2.7.2",
    "appKey": "12574478",
    "t": u, # 时间戳
    "sign": string, # 签名
    "api": "mtop.relationrecommend.wirelessrecommend.recommend",
    "v": "2.0",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp4", # 回调函数
    "data": data
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
# print(response.text)
if "FAIL_SYS_TOKEN_EXOIRED" in response.text:
    print("Token已过期，请更新token值")
    # 可以在这里添加自动重试逻辑或提醒用户更新
    exit()

res_data = re.findall(r'mtopjsonp\d+\((.*)', response.text)[0][:-1]
json_data = json.loads(res_data)
# print(json_data)
items = []
for item in json_data['data']['itemsArray']:
    try:
        dit = {
            "标题": item['title'],
            "地区": item['procity'],
            "回头客": item['shopTag'],
            "价格": float(item['price']),
        }
        items.append(dit)
    except:
        pass
# 按价格排序（从低到高）
sorted_items = sorted(items, key=lambda x: x['价格'])

# 打印排序后的结果
for item in sorted_items:
    print(item)

# 将数据写入CSV文件
with open(f'爬虫\文本\淘宝商品数据.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['标题', '地区', '回头客', '价格']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # 写入表头
    writer.writeheader()
    
    # 写入数据
    for item in sorted_items:
        writer.writerow(item)

print("数据已成功写入到 淘宝商品数据.csv 文件中")