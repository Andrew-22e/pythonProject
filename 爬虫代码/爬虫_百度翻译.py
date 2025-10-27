import requests
import json


headers = {
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "Acs-Token": "1761501606444_1761568178057_t+QoNfaaIgnoBUC5qSlJOgmsK8sPkDIiSpdTqdt0zg/eZxNmRoNHDZBu4APBE/coV4VH1mgV+kO+56flcdr5k35ZchaD+kfpQThnm+voSA4YqjkmJW9rMifOdSEb13HPpRNUu6YOd4FQr0wtlUiqlypCDTlOA/lxl+IKxa1d4os06/SFg5FFzcGtxp3BOnLL0ZHUXB+Q/Nd2IsBJky9HFxoK805kQ+UFtlp9BwWwzdCY0IL7H7sNC0K60gqg8ExGoyv/TwZTXwioOdGKyUYCdtUIj4WpxQGguAtangfQ92EwocGY8xtZm06P0ssM37U+bqyZQxXY3fCl0i/lKDJ2ZCREI2UmcLplJoci/sl4Vp3R1SQcg8Wa3/LQw+1BJvWtNqO4tt9x5m5icS3r5ExvLbpaGz2GVNLWG30xMAHSPuzymqX8zvxyX66zAPIJPaEn2at0STLXUWfUVCGh+LzmIA==",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Origin": "https://fanyi.baidu.com",
    "Pragma": "no-cache",
    "Referer": "https://fanyi.baidu.com/mtpe-individual/transText?query=l&lang=en2zh",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0",
    "accept": "text/event-stream",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "BAIDUID_BFESS": "28AD3E498C7C985E220EF69110F6EA7C:FG=1",
    "PSTM": "1760860904",
    "BIDUPSID": "4B91195B13F4AF67C54811FE23ACD66C",
    "ZFY": "BwNRpVJuNJjBRgrrSL5y:BQpbR4:AGxiKWqTsXzag4fbU:C",
    "H_WISE_SIDS": "63144_64981_65250_65361_65455_65616_65602_65638_65659_65678_65666_65687_65700_65708_65738_65753_65759_65806_65865",
    "H_PS_PSSID": "63144_64981_65250_65361_65455_65616_65638_65659_65678_65666_65687_65700_65708_65738_65753_65759_65806_65865_65844",
    "AIT_PERSONAL_VERSION": "1",
    "AIT_ENTERPRISE_VERSION": "1",
    "ab_sr": "1.0.1_NjlmNzRjZWQwNjM4NDYyMjcxZTJmNTU1MGUwNTdhMTg5ZTFlNjRmNWM2NjkyMzJlMDQxMjg3ZGFmMzQ1ZTQ4MjU3OTc4OWE4Mjg0YTRhZDRkNzczZmZjNzI3ZDc5N2E5NTc0OTcxYzM4ZjQ2NGI5ZjUxNzBhNThmNmMxMGM4YWY5YTdjNzA0Y2M3MjRjYzBmYWNkZjM0ZjFlNTE2YWViOA==",
    "RT": "\"z=1&dm=baidu.com&si=cdbaa3b5-73dd-4fbf-8f57-bb7bceb616ce&ss=mh933245&sl=4&tt=478&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=14ggo\""
}
url = "https://fanyi.baidu.com/ait/text/translate"
data = {
    "isAi": False,
    "sseStartTime": 1761568178053,
    "query": "l",
    "from": "en",
    "to": "zh",
    "reference": "",
    "corpusIds": [],
    "needPhonetic": True,
    "domain": "common",
    "detectLang": "",
    "isIncognitoAI": False,
    "milliTimestamp": 1761568178125
}
data = json.dumps(data, separators=(',', ':'))
response = requests.post(url, headers=headers, cookies=cookies, data=data)
print(response.text)