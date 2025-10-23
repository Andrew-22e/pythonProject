import requests


headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://mail.qq.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521",
    "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Microsoft Edge\";v=\"140\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}
cookies = {
    "ptcz": "6e0239ad7a443aa3a89ee53e6a80192ae115929f2c1fa02a054430228d38fe3d",
    "webp": "1",
    "pgv_pvid": "0715799444",
    "_qimei_q36": "",
    "_qimei_h38": "2db8c6d1109be7d705fe1f2c02000000218318",
    "RK": "d2mcpvx/U2",
    "qq_domain_video_guid_verify": "e18dd57881ce1da7",
    "_qimei_fingerprint": "28e27f13e024b4e72ed41740c05847af",
    "_qimei_uuid42": "19505173002100856ecf7cb760a7e15aa071765ccc",
    "_qimei_i_3": "25e04fd6920e0489c6c3fd3959d120e0f2eea5a0435b0487e2887a0975932665353064943c89e2a3bf82",
    "_qimei_i_1": "47c46f80c1085888c7c3ff315b8d21b5f0baa3f1170d5683e28d7b582493206c616337973981e1ddde9cdafc",
    "_qpsvr_localtk": "0.8514934466154596",
    "xm_envid": "456_6ZWY1hKYKdWuDhXOBfHWVVf/EUQrRJtvQg9aDQ6h45OJGUtMBryAKQcoTLNePDrkpeVg0QDC606nClc8XL5P5YJCE/6IzZcdC8h8R3JyTfcsCCEnLiJLuCHaqzH1I1x16KYa0vXZGNRfZ1QpF164luI0GVZz8oc=",
    "qm_device_id": "882XrWwlMyXUVcyfu4YUqW2i+aHC975mkOLTIwB1un2WhqrGhJMqGsscH/+s1YXR",
    "xm_pcache": "13102663080446531&V2@aNaXcXMuQ1CZjS1mmdhC9gAA@0",
    "qm_username": "2055572035",
    "uin": "o2055572035",
    "qm_domain": "https://mail.qq.com",
    "ssl_edition": "sail.qq.com",
    "edition": "mail.qq.com",
    "username": "2055572035&2055572035",
    "sid": "2055572035&5fdb7ee6322ec707231e095dd8a8f943",
    "qm_muti_sid": "13102663080446531&w4A9-3UZSs8NSjBY",
    "xm_uin": "13102663080446531",
    "xm_sid": "zUNTUYyKbnouhTl5AHpDeQAA",
    "xm_muti_sid": "13102663080446531&zUNTUYyKbnouhTl5AHpDeQAA",
    "xm_skey": "13102663080446531&5b945d87a6203e8b6e426dac805f52ca",
    "xm_ws": "13102663080446531&28948a7efd12285cedf74b3d9ffaa3d4",
    "xm_data_ticket": "13102663080446531&CAESIGjCbL0ALozNeoWKQ0sF9Hy6fVe-foRwkBceqDL3IauK",
    "qm_logintype": "qq",
    "CCSHOW": "000001"
}
url = "https://mail.qq.com/cgi-bin/compose_send"
params = {
    "sid": "w4A9-3UZSs8NSjBY" # 
}
data = {
    "a2822836acaaaf17a3d19df5ecb1ad7a": "5fdb7ee6322ec707231e095dd8a8f943", 
    "sid": "w4A9-3UZSs8NSjBY",
    "from_s": "cnew",
    "signtype": "0",
    "to": "\"画船听雨眠～.\"<2055572035@qq.com>",
    "subject": "主题",
    "content__html": "<div>这是发送内容</div>",
    "sendmailname": "2055572035@qq.com",
    "savesendbox": "1",
    "actiontype": "send",
    "sendname": "画船听雨眠～.",
    "acctid": "0 ",
    "separatedcopy": "false",
    "s": "comm",
    "hitaddrbook": "0",
    "selfdefinestation": "-1",
    "domaincheck": "0",
    "cgitm": "1757572286390", #
    "clitm": "1757572286503", # 
    "comtm": "1757572523141", #
    "logattcnt": "0",
    "logattsize": "0",
    "timezone": "28800",
    "timezone_dst": "0",
    "cginame": "compose_send",
    "ef": "js",
    "t": "compose_send.json",
    "resp_charset": "UTF8"
}
response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)

print(response.text)
print(response)