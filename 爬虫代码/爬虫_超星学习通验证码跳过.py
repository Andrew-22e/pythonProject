import requests
import time
import execjs
import re
# 验证码识别模块
import ddddocr

# 实现了超星学习通模拟登录的效果

headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://v8.chaoxing.com/",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.6.2081 SLBChan/105 SLBVPV/64-bit",
    "sec-ch-ua": "\"Chromium\";v=\"9\", \"Not?A_Brand\";v=\"8\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "route": "c873910f23fdbb50ba156beee2b1b2db"
}
url = "https://captcha.chaoxing.com/captcha/get/verification/image"
t = int(time.time() * 1000)
# 编译JS代码
js_code = execjs.compile(open('爬虫/前端/JS/超星学习通.js',encoding='utf-8').read())
r = js_code.call('GetSign',t)
params = {
    "callback": "cx_captcha_function",
    "captchaId": "qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv",
    "type": "slide",
    "version": "1.1.20",
    "captchaKey": r['captchaKey'],
    "token": r['token'],
    "referer": "https://v8.chaoxing.com/",
    "iv": r['iv'],
    "_": t
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)
# print(response.text)

# 解析数据
shadeImage, cutoutImage= re.findall('"shadeImage":"(.*?)","cutoutImage":"(.*?)"',response.text)[0]
token = re.findall('"token":"(.*?)"',response.text)[0]
# print(token)
# print(shadeImage, cutoutImage)

# 验证识别
shadeImage_content = requests.get(shadeImage, headers=headers, cookies=cookies).content
cutoutImage_content = requests.get(cutoutImage, headers=headers, cookies=cookies).content

det = ddddocr.DdddOcr(det=False,ocr=False)
res = det.slide_match(shadeImage_content, cutoutImage_content,simple_target=True)
# print(res)

# 获取x轴偏移量
x = res['target'][0]
# print(x)

# 验证链接
t1 = int(time.time() * 1000)
url1 = "https://captcha.chaoxing.com/captcha/check/verification/result"
params1 = {
    "callback": "cx_captcha_function",
    "captchaId": "qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv",
    "type": "slide",
    "token": token,
    "textClickArr": "[{\"x\":%d}]" % x,
    "coordinate": "[]",
    "runEnv": "10",
    "version": "1.1.20",
    "t": "a",
    "iv": js_code.call('GetIV',t1),
    "_": t1
}
response1 = requests.get(url1, headers=headers, cookies=cookies, params=params1)
# print(response1.text)

# 匹配转义的双引号
validata = re.findall(r'\\\"validate\\\":\\\"(.*?)\\\"', response1.text)[0]
# print(validata)

# 实现自动登录 # （修改地方）只要修改url3
cookies3 = {
    "route": "0ef7d2670c4bb223b05c7ace18fa04dc",
    "fid": "176854",
    "V8_front": "87795B89E109AF8A611ED6DA8728E3D74F849FAE5587CBB141096583A3A5636C005D0469B34B99BAE73DC1D152F48F5BE064178DBDEDD206106622DC11DB3E86DE694DFAE4062754111066E5BDD55D1A4D90A272A4EC7D9F2FF2338EC26EAACC3529884475C8A60018DC0EAE65C7DE8065533F706BCB0BB9A54E5E24F4B846B30138833F50C152E54A09469624BC258D133600584823F19734D20F62C41E07CA12491EE842F9B73A",
    "SESSIONID": "35D6DA29954ED99EC976F8767F8EE86C"
}
url3 = "https://v8.chaoxing.com/users/dologinV2/701D565054B61B64613A153CF73C614A"
data = {
    "uname":15179869369,
    "pwd":'@Li456456',
    "source": "num8",
    "validata": validata
}
response = requests.post(url3, headers=headers, cookies=cookies3, data=data)
print(response.text)