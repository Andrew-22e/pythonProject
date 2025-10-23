import requests
import time
import execjs
import re
import tqdm

# 待修改成批量获取视频下载

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://v.douyu.com",
    "priority": "u=1, i",
    # 防盗链（修改地方）
    "referer": "https://v.douyu.com/show/mPyq7obBnKdv1gLY",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
cookies = {
    "_ga": "GA1.1.341371085.1754285539",
    "dy_did": "b8ca3afd34364891baafb02e00021701",
    "_ga_7RMFJRR7D2": "GS2.1.s1754285549$o1$g0$t1754285550$j59$l0$h1087163443",
    "_ga_7H57T4TYRW": "GS2.1.s1754285539$o1$g1$t1754285560$j39$l0$h54880187",
    "_ga_X8YS4358RH": "GS2.1.s1754285539$o1$g1$t1754285560$j39$l0$h0"
}
url = "https://v.douyu.com/wgapi/vodnc/front/stream/getStreamUrlWeb"
t = int(time.time())
# 编译JS代码
js_code =  execjs.compile(open('爬虫/前端/JS/斗鱼视频.js',encoding='utf-8').read())
a = 43814012 
o = "b8ca3afd34364891baafb02e00021701"
sign = js_code.call('ub98484234',a,o,t).split('=')
# print(sign)
data = {
    "v": "220320250804", # 固定值
    "did": o,
    "tt": t,
    "sign": sign[4],
    "vid": "mPyq7obBnKdv1gLY"
}
response = requests.post(url, headers=headers, cookies=cookies, data=data)

# print(response.text)
json_data = response.json()
# 提取m3u8链接
m3u8_url = json_data['data']['thumb_video']['high']['url']
# print(m3u8_url)
# 提取ts文件
m3u8_text = requests.get(m3u8_url,headers=headers).text
# print(ts_url)
ts_urls = re.findall(r',\n(.*?)\n#',m3u8_text)
# print(ts_urls)
# 拼接ts文件
for url in tqdm(ts_urls):
    ts_url = 'https://play-hw-ugcpub.douyucdn2.cn/live/high_127068120250726231500-upload-0345/' + url
    # print(ts_url)
    ts_content = requests.get(ts_url,headers=headers).content
    with open(f'爬虫\视频\斗鱼\视频.mp4','ab') as f:
        f.write(ts_content)
print('下载完成！')