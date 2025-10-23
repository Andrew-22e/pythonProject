import execjs
import requests
import json

# 以UTF-8编码读取JavaScript文件，避免GBK编码问题
with open(r'c:\lj666\VScode\python\爬虫\前端\JS\国家医保平台逆向webpack\loader.js', 'r', encoding='utf-8') as f:
    loader_js = f.read()
    
with open(r'c:\lj666\VScode\python\爬虫\前端\JS\国家医保平台逆向webpack\main.js', 'r', encoding='utf-8') as f:
    main_js = f.read()

# 创建JavaScript运行环境
ctx = execjs.compile(loader_js + "\n" + main_js)

# 发送请求获取加密数据
headers = {
    "Accept": "application/json",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fuwu.nhsa.gov.cn",
    "Pragma": "no-cache",
    "Referer": "https://fuwu.nhsa.gov.cn/nationalHallSt/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "X-Tingyun": "c=B|4Nl_NnGbjwY;x=3f88cf6b84ec495d",
    "channel": "web",
    "contentType": "application/x-www-form-urlencoded",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-tif-nonce": "w2uyQe9D",
    "x-tif-paasid": "undefined",
    "x-tif-signature": "2bc573410230d8bb002abf9ff8ccd31ff2de7bff08f4b189f1b7db009b931999",
    "x-tif-timestamp": "1758069098"
}

cookies = {
    "amap_local": "360700",
    "acw_tc": "b65cfd3217580689988416443e228a3cf8da47710e457ca7b31dea32f9b092",
    "yb_header_show": "true",
    "yb_header_active": "-1"
}

url = "https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital"
data = {
    "data": {
        "data": {
            "encData": "3DFBCA4667B978F639BB23B95DCE4CC7D5AFF98F55C7DE7BEFADAEA0B65DF9DFCCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F33C56677481A67C67F739EE2C7D589054DC373615B5DDB33C24C5B31E61CB7643E00DDA865C3B75C85735F0744B0227B5CD0B4E7BB97C60BF8E5275CAFCAFD1E13E384C10195003FD638576645B5EF45EA"
        },
        "appCode": "T98HPCGN5ZVVQBS8LZQNOAEXVI9GYHKQ",
        "version": "1.0.0",
        "encType": "SM4",
        "signType": "SM2",
        "timestamp": 1758069098,
        "signData": "mQCwuPuSmu1apQTkiVcaEW36K2HDX8DVkFmQJCOQ1kzmYFxI5KUwD2qHt0JmAWjmYjxaqpI7kfVkCxxcrtuYIg=="
    }
}

data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)

# 获取响应数据
response_data = response.json()
# print("原始响应数据:")
# print(json.dumps(response_data, ensure_ascii=False, indent=2))

# 解密数据 - 注意：decrypt函数返回的已经是Python字典，不需要再解析
decrypted_data = ctx.call('decrypt', response_data)
# print("\n解密后的数据:")
# print(json.dumps(decrypted_data, ensure_ascii=False, indent=2))

# 直接从解密后的数据中提取信息
# 根据您提供的main.js中的decrypt函数，解密后的数据结构应该是:
info_list = decrypted_data['list']
print(f"\n共找到 {len(info_list)} 条医疗机构记录:")

# 提取并打印医疗机构信息
for i, hospital in enumerate(info_list, 1):
    medins_name = hospital.get('medinsName', '未知')
    medins_code = hospital.get('medinsCode', '未知')
    addr = hospital.get('addr', '未知')
    medins_type_name = hospital.get('medinsTypeName', '未知')
    
    print(f"{i}. 医疗机构名称: {medins_name}")
    print(f"   医疗机构代码: {medins_code}")
    print(f"   地址: {addr}")
    print(f"   类型: {medins_type_name}")
    print("-" * 50)

# # 如果需要将数据保存到文件
# def save_to_json(data, filename):
#     """将数据保存为JSON文件"""
#     with open(filename, 'w', encoding='utf-8') as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
#     print(f"数据已保存到 {filename}")

# # 保存解密后的完整数据
# save_to_json(decrypted_data, 'hospital_data.json')

# # 只保存医疗机构列表
# hospital_list = []
# for hospital in info_list:
#     hospital_info = {
#         '医疗机构名称': hospital.get('medinsName'),
#         '医疗机构代码': hospital.get('medinsCode'),
#         '地址': hospital.get('addr'),
#         '类型': hospital.get('medinsTypeName'),
#         '统一社会信用代码': hospital.get('uscc'),
#         '经度': hospital.get('lnt'),
#         '纬度': hospital.get('lat')
#     }
#     hospital_list.append(hospital_info)

# save_to_json(hospital_list, 'hospital_list.json')