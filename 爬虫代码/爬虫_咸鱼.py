import hashlib
import requests
import time


j = int(time.time() * 1000)
headers = {
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://www.goofish.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.goofish.com/",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}
cookies = {
    "cna": "1qwMITu9pwgCAXWqbTccVdyy",
    "cookie2": "1fb042957bb9a2c053abbed385a6aae2",
    "mtop_partitioned_detect": "1",
    "_m_h5_tk": "b9e587edd17a229da79872bf8d9c85c0_1759674431271",
    "_m_h5_tk_enc": "fd79ae350ab1ad2ee36b0fe26efdf964",
    "xlly_s": "1",
    "tfstk": "gSBoIOZ4g_R5t2kSZkv7wl-7IEPvVL9BawHpJpLUgE8jy4HRY2bhuNI-e9Ie-wbvlwAQVeLe-wIFwoeTBgsWdp83WRet7HSPbacyLHre33tTD38zx5DydpzTkjHeNRvCzl6ppQS4mHKKa37ELil2lH0yYw8ygq-Mfp8F8wkq33tpYX8rLoj2lHJe4p7e3oxpueJeLwSqIdPyP9WV3yzcjVPvkfC6qQYN4USR2tkkgbsWoN_dh3X9kgoILvWDqQXqmWO9OQCFfC6RvJDXeGf23HXQbXYHs6WJ3Tz4QIOFT1dhM4rR7wjVRLB4Yb8NwapVU1mELivkoBKkN44D7TsVCKRYQljVhaI5nMnULnQ9ug6yKRr6EL8ynn6LlY8hg6WJNpgz-e6c0T5h4alq_qV-dnrd3XGBantDWOKz0wGHsXnYmocaAQ-XVFE0mXGBantDWoqm_JOyc3TO."
}
url = "https://h5api.m.goofish.com/h5/mtop.taobao.idlehome.home.webpc.feed/1.0/"

params = {
    "jsv": "2.7.2",
    "appKey": "34839810",
    "t": j,
    "sign": "8523d42c2c4dbf5d91d4bdee33d7147e",  # md5哈希算法、摘要算法
    #"sign": sign,
    "v": "1.0",
    "type": "originaljson",
    "accountSite": "xianyu",
    "dataType": "json",
    "timeout": "20000",
    "api": "mtop.taobao.idlehome.home.webpc.feed",
    "sessionOption": "AutoLoginOnly",
    "spm_cnt": "a21ybx.home.0.0"
}
data = {
    "data": "{\"itemId\":\"\",\"pageSize\":30,\"pageNumber\":1,\"machId\":\"164111_1\"}"
}

token = 'b9e587edd17a229da79872bf8d9c85c0'

# h = '34839810'
# data = '{"itemId":"","pageSize":30,"pageNumber":1,"machId":"165362_1"}'
k = token + "&" + str(j) + "&" + params["appKey"] + "&" + data["data"]
sign = hashlib.md5(k.encode("utf-8")).hexdigest()
params["sign"] = sign
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)