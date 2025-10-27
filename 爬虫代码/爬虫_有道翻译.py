import requests
import time
from hashlib import md5
from base64 import b64decode
from Crypto.Cipher import AES
import re

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://fanyi.youdao.com",
    "Referer": "https://fanyi.youdao.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "OUTFOX_SEARCH_USER_ID_NCOO": "1289876238.1521573",
    "_ga": "GA1.2.1381100309.1752678801",
    "OUTFOX_SEARCH_USER_ID": "744595817@117.170.109.62",
    "DICT_DOCTRANS_SESSION_ID": "MTIyMTQ3ZWEtMDQxMi00OTc0LTllYjgtYzc3OTI5MjdkNzU3",
    "_uetsid": "8e37fdb0649a11f0bb11df9e27c33aa5",
    "_uetvid": "8e3830f0649a11f0a28fff4d1a3accf9",
    "_uetmsclkid": "_uetf49f9a28a5351d7a6922f2532807e8cd"
}
url = "https://dict.youdao.com/webtranslate"
# 动态填充参数
#input_text = input("请输入要翻译的文本：")
input_text = '轮播'
time = int(time.time()*1000)  # 时间戳，如果是13位的时间戳，则乘以1000
# 创建md5对象
md5_obj = md5()
# 计算sign
md5_obj.update(f'client=fanyideskweb&mysticTime={time}&product=webfanyi&key=SRz6r3IGA6lj9i5zW0OYqgVZOtLDQe3e'.encode())
# 获取sign并且转换为16进制
sign =  md5_obj.hexdigest()

data = {
    "i": input_text,
    "from": "auto",
    "to": "",
    "useTerm": "false",
    "dictResult": "true",
    "keyid": "webfanyi",
    "sign": sign,
    "client": "fanyideskweb",
    "product": "webfanyi",
    "appVersion": "1.0.0",
    "vendor": "web",
    "pointParam": "client,mysticTime,product",
    "mysticTime": time,
    "keyfrom": "fanyi.web",
    "mid": "1",
    "screen": "1",
    "model": "1",
    "network": "wifi",
    "abtest": "0",
    "yduuid": "abcdefg"
}
# 发送请求
response = requests.post(url, headers=headers, cookies=cookies, data=data)
# print(response.text)

# 将结果进行base64解密处理
res = b64decode(((response.text).replace('-','+').replace('_','/')).encode())
# print(list(res))

# 使用的是AES128-CBC加密算法，需要使用密文、密钥和偏移量
key = bytes([8, 20, 157, 167, 60, 89, 206, 98, 85, 91, 1, 233, 47, 52, 232, 56])
IV = bytes([210, 187, 27, 253, 232, 59, 56, 195, 68, 54, 99, 87, 183, 156, 174, 28])

obj = AES.new(key, AES.MODE_CBC, IV)
res = obj.decrypt(res)
print((re.search(r'"#tran":"(.*?)"',res.decode())).group(1))