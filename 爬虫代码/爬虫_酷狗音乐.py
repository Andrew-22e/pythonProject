"""单个歌曲的下载"""
# import requests

# headers = {
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
#     "origin": "https://www.kugou.com",
#     "priority": "u=1, i",
#     "referer": "https://www.kugou.com/",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
# }
# url = "https://wwwapi.kugou.com/play/songinfo"
# params = {
#     "srcappid": "2919",
#     "clientver": "20000",
#     "clienttime": "1753420161307", # 时间戳
#     "mid": "828d02df2c8de8ad15200921aba8e181",
#     "uuid": "828d02df2c8de8ad15200921aba8e181",
#     "dfid": "1Jc5973BUuTi0psQtj26PVoy",
#     "appid": "1014",
#     "platid": "4",
#     "encode_album_audio_id": "14qlw960", # 音频id
#     "token": "bd1fd743f8c881d14702120702ad20773684b9d2a75dbe69d7c64e0a9b5dbc11",
#     "userid": "951920223",
#     "signature": "33ea9a1a576adcd55a58a812af7e3fe6" # 签名
# }
# response = requests.get(url, headers=headers, params=params)

# # print(response.text)

# # 解析数据
# # 提取音频链接地址
# audio_name = response.json()["data"]["audio_name"]
# music_url = response.json()["data"]["play_url"]
# print('歌曲名称：',audio_name,'歌曲链接：',music_url)
# # 获取音频数据
# music_content = requests.get(music_url,headers=headers).content
# # 保存音频数据
# with open(f"爬虫/音乐/酷狗/{audio_name}.mp3", "wb") as f:  # 创建一个文件对象
#     f.write(music_content)
# print("保存成功!")

"""批量歌曲的下载"""
import requests
import time
import hashlib
import re

def GetSign(time,encode_album_audio_id):
        # 加密参数列表
        s = [
            "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt",
            "appid=1014",
            f"clienttime={time}",
            "clientver=20000",
            "dfid=1Jc5973BUuTi0psQtj26PVoy",
            f"encode_album_audio_id={encode_album_audio_id}",
            "mid=828d02df2c8de8ad15200921aba8e181",
            "platid=4",
            "srcappid=2919",
            "token=bd1fd743f8c881d14702120702ad20773684b9d2a75dbe69d7c64e0a9b5dbc11",
            "userid=951920223",
            "uuid=828d02df2c8de8ad15200921aba8e181",
            "NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt"
        ]
        # 将列表合并成字符串
        string = "".join(s)
        # 进行md5加密
        signature = hashlib.md5(string.encode("utf-8")).hexdigest()
        return signature
headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "origin": "https://www.kugou.com",
    "priority": "u=1, i",
    "referer": "https://www.kugou.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
cookies = {
    "kg_mid": "828d02df2c8de8ad15200921aba8e181",
    "kg_dfid": "1Jc5973BUuTi0psQtj26PVoy",
    "kg_dfid_collect": "d41d8cd98f00b204e9800998ecf8427e",
    "Hm_lvt_aedee6983d4cfc62f509129360d6bb3d": "1753360209",
    "HMACCOUNT": "92DDEA22E155F965",
    "KuGoo": "KugooID=951920223&KugooPwd=64452AD4CB7FE3834AB08C49D9C1B2FC&NickName=%u0053%u0075%u006e%u0073%u0068%u0069%u006e%u0065&Pic=http://imge.kugou.com/kugouicon/165/20230505/20230505081050360989.jpg&RegState=1&RegFrom=&t=bd1fd743f8c881d14702120702ad20773684b9d2a75dbe69d7c64e0a9b5dbc11&t_ts=1753360261&t_key=&a_id=1014&ct=1753360260&UserName=%u0031%u0035%u0031%u0037%u0039%u0038%u0036%u0039%u0033%u0036%u0039",
    "KugooID": "951920223",
    "t": "bd1fd743f8c881d14702120702ad20773684b9d2a75dbe69d7c64e0a9b5dbc11",
    "a_id": "1014",
    "UserName": "%u0031%u0035%u0031%u0037%u0039%u0038%u0036%u0039%u0033%u0036%u0039",
    "mid": "828d02df2c8de8ad15200921aba8e181",
    "dfid": "1Jc5973BUuTi0psQtj26PVoy",
    "ACK_SERVER_10015": "%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D",
    "Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d": "1753422964",
    "ACK_SERVER_10028": "%7B%22list%22%3A%5B%5B%22p1.fx.kgimg.com%22%5D%2C%5B%22p3fx.service.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10029": "%7B%22list%22%3A%5B%5B%22p3.fx.kgimg.com%22%5D%2C%5B%22p3fx.service.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10035": "%7B%22list%22%3A%5B%5B%22fxsong.kugou.com%22%5D%2C%5B%22fxsong2.kugou.com%22%5D%2C%5B%22fxsong3.kugou.com%22%5D%2C%5B%22fxsong4.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10011": "%7B%22list%22%3A%5B%5B%22fanxing.kugou.com%22%5D%2C%5B%22sparefx2.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10034": "%7B%22list%22%3A%5B%5B%22image.fanxing.kugou.com%22%5D%2C%5B%22s3fx.kgimg.com%22%5D%5D%7D",
    "ACK_SERVER_10022": "%7B%22list%22%3A%5B%5B%22fx1.service.kugou.com%22%5D%2C%5B%22fxservice3.kugou.com%22%5D%2C%5B%22fx2.service.kugou.com%22%5D%2C%5B%22fxservice4.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10014": "%7B%22list%22%3A%5B%5B%22service.fanxing.kugou.com%22%5D%2C%5B%22servicefx2.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10023": "%7B%22list%22%3A%5B%5B%22service1.fanxing.kugou.com%22%5D%2C%5B%22service3.fanxing.kugou.com%22%5D%2C%5B%22service2.fanxing.kugou.com%22%5D%2C%5B%22service4.fanxing.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10033": "%7B%22list%22%3A%5B%5B%22s3.fx.kgimg.com%22%5D%2C%5B%22s3fx.kgimg.com%22%5D%5D%7D",
    "ACK_SERVER_10036": "%7B%22list%22%3A%5B%5B%22gateway.kugou.com%22%5D%2C%5B%22gatewayretry.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10030": "%7B%22list%22%3A%5B%5B%22p3fx.kgimg.com%22%5D%2C%5B%22p3fx.service.kugou.com%22%5D%5D%7D",
    "ACK_SERVER_10020": "%7B%22list%22%3A%5B%5B%22fx.service.kugou.com%22%5D%2C%5B%22fxservice1.kugou.com%22%5D%2C%5B%22fxservice2.kugou.com%22%5D%5D%7D"
}
url = "https://wwwapi.kugou.com/play/songinfo"
# 榜单链接地址 （修改地方）
link = "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
html_data = requests.get(url=link, headers=headers,cookies=cookies).text
# print(html_data)
song_list = re.findall(r'title="(.*?)"[^>]*?data-eid="(.*?)"',html_data)
# print(song_list)
for song in song_list:
    song_name = song[0]
    song_id = song[1]
    #print("歌曲名称：",song_name,"歌曲ID：",song_id)
    # 动态传入参数
    current_time  = int(time.time()*1000)
    sign = GetSign(current_time,song_id)
    params = {
        "srcappid": "2919",
        "clientver": "20000",
        "clienttime": current_time , # 时间戳
        "mid": "828d02df2c8de8ad15200921aba8e181",
        "uuid": "828d02df2c8de8ad15200921aba8e181",
        "dfid": "1Jc5973BUuTi0psQtj26PVoy",
        "appid": "1014",
        "platid": "4",
        "encode_album_audio_id": song_id, # 音频id
        "token": "bd1fd743f8c881d14702120702ad20773684b9d2a75dbe69d7c64e0a9b5dbc11",
        "userid": "951920223",
        "signature": sign, # 签名
    }
    response = requests.get(url, headers=headers, params=params)

    # print(response.text)

    # 解析数据
    # 提取音频链接地址
    audio_name = response.json()["data"]["audio_name"]
    music_url = response.json()["data"]["play_url"]
    print('歌曲名称：',audio_name,'歌曲链接：',music_url)
    # 获取音频数据
    music_content = requests.get(music_url,headers=headers).content
    # 保存音频数据
    with open(f"爬虫/音乐/酷狗/{audio_name}.mp3", "wb") as f:  # 创建一个文件对象
        f.write(music_content)
    print("保存成功!")
