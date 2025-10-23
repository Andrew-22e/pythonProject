'''单个歌曲的下载'''
# import requests

# # 使用爬虫工具库直接实现数据的获取
# headers = {
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
#     "content-type": "application/x-www-form-urlencoded",
#     "origin": "https://music.163.com",
#     "priority": "u=1, i",
#     "referer": "https://music.163.com/",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
# }
# cookies = {
#     "NMTID": "00OHaan-8giq5QXzUZ6tbn5iIrg78oAAAGWn3AKQQ",
#     "_iuqxldmzr_": "32",
#     "_ntes_nnid": "3671b2313f79dba114c9570e6e773eb5,1746431642999",
#     "_ntes_nuid": "3671b2313f79dba114c9570e6e773eb5",
#     "WEVNSM": "1.0.0",
#     "WNMCID": "zqgpkr.1746431643522.01.0",
#     "sDeviceId": "YD-ZJfwg7E74lRAA0ARVFfCLZfufkQXs8LZ",
#     "ntes_utid": "tid._.bJvJQj0NNZJEEgBQEVLWeJb%252BLwADtypB._.0",
#     "WM_TID": "0gGhUzyN4zVEFABRUUPWfdbvf0AHYlwc",
#     "__snaker__id": "siPu4DggfYCxGAPj",
#     "ntes_kaola_ad": "1",
#     "timing_user_id": "time_jmcpcArKIl",
#     "P_INFO": "15179869369|1753187123|1|music|00&99|null&null&null#jix&360700#10#0|&0||15179869369",
#     "__remember_me": "true",
#     "__csrf": "0fa5699291db129daa04ede23c7b87d9",
#     "MUSIC_U": "0066E505BF2DF17746E11E1486CAC9DBA70E9CFDF5A0D93A9CC96BF5F460301E32865C2EE2C8B2920BBBADBA2F71C6E8955E69819EAB28B0AB2591DD24C394E1B3095FA7645BDA7BAB853E55F65CEAFCEABE11C9AB160E758EEF7A170E5650FF8B14DC4D5F14741F60C8DA84BBE7EB1087085703D161FCAB46B6F5939DA6D1510C74A8F3EF3B60D3181A3A90168F92B691539739B745A463E39C5F15C3645EFAF1CE277B9B92E14C1935CA534CE5A871FEB297F752B44FCAEE2935ACF3989FC61820F5EFE374CA962290689D6B4C5B329266A2A773215B081E09EC888E5E277D41C65020EC18B27BF3436D08AF224BE843532E7D26F6EE19CA2780BD2BB7BC0E573F2809DCDE6112FB6C5DA596F7E16441F3E9052467CB6F1339F43715CE4B41BEA5DFCEAE8FE90030EB5A432724BCDBA2C01F00D55408EBBF2E70C7EDC37FB668D96F0D1E9DFC814AEBBC75E3DF560A0FC44EC63DFB8903247AFF8FA88A0C9326CF66E2E74338C1FCE3C2FC065B84BFAA07E3867C4969DF8650F0B1C49FD47478291AEDA10D94E57BD8A3100CC0AA4CA3233FEA5CD01034E4B90606A1FE471790",
#     "gdxidpyhxdE": "ZNra3czmN2te6nR%2Fn6QYs1Djm36652h5Sf2RqclTR9o4ox2vlioVhLazDMyxPhBlJOE5intSZeBsXJKNGHx%5CD%5CEiD4iG3sb%2FqEhp%2FjmxEt3%2B%2FHdiROcU%5CIU9yzIWhp%5Ca4K2ZkDKpZeyrX7L%2F365Qz%2B%2B8IzfzXO3YiT%2Fybmd6xcVKeygS%3A1753199105175",
#     "JSESSIONID-WYYY": "pBN%2Bes8FKw0%2FtiXI2tEBHKQQU1IJABRV3%5CSBF1wWGbW%2F2sEpAvKDQDhdVXBe0X6xAAWnSI8HcAEOv8%2B8N47XabKFvMD%5CFpdJmDmZF4FSyw6YkNv6tviSDz0DHGUhph49hnoSjj9DHwr38CyxtATMsfjDTMwyylzfBI%2FFSOme66v7lIrY%3A1753274187583",
#     "WM_NI": "s8ufrrodGZVfhU1ngwz2fLxWM2ZTS%2FGWRw2pFASVa8zvdkiwCUp15k9ccaGHuvp4tP%2F9EeJNszPeTZaK5IfSPyoiOHda%2F1LMhf0cIpQouwkfK7e7xEis6dpHSzKcMn7rMmw%3D",
#     "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee8ef060b4958490cf42aeb88fa6d15a979f8aaccb3c96ebbeb5e55c97bdf7adec2af0fea7c3b92ab1e8bb87f17aadbc89bbd56eac8bff8fe67dbaeeaaadfb5d8fee96b5d22585899e98b17c869f9db7e434baaaac8cec7d818bc0d2b861fbbdad82c644b7aac0d5f75cede78b86c946b1a6a086d752a395fbaae55994a7a18ace44a8bfe1d2cf47acba0084cc7c93b1bb98ea6e89e9abd8fb4fabadfa85f34491a68584d066f5ae838ef637e2a3"
# }
# url = "https://music.163.com/weapi/song/enhance/player/url/v1"
# params = {
#     "csrf_token": "0fa5699291db129daa04ede23c7b87d9"
# }
# data = {
#     "params": "9kTIgHst7IWxHTm/MKYbZgM0Z7hf2ECthMGd3SG8tL+00Ib3oiDg3ggh9JVUhnfOpFLmsSDPXhSgsI1EPoZBHZVwCUu3C6MURC9gn0TspBOnryCnR8cm3mqnO3rJsedBQPo2EZ9ETx6VAtvj+PLl/3FAfFxnp81pSPjw7OvAJu/F3k/fixlWHgFFT28JSAhYBlNyndUdMCo+6XRhUC8tgA==",
#     "encSecKey": "090333defa110cec6be3c5181db7f9b3578fe11759e8962ec2d1580ddb48f7694108fc4f6f96c09d16af7aeca0997eb83b81f6642f3218c6e6fdbb06573e174b2ffb3d6c7b9e400d1eede977511f280b7c23e590756d85d30f008f08058cf5fd57c6be46decec42e7d633071824c1814d4e5dabf469b6e8c28763530be4473d2"
# }
# response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data)
# # print(response.text)

# # 解析数据
# # 提取音频链接地址
# music_url = response.json()["data"][0]["url"]
# # print(music_url)
# # 获取音频数据
# music_content = requests.get(music_url,headers=headers).content
# # 保存音频数据
# with open("爬虫/音乐/一荤一素.mp3", "wb") as f:  # 创建一个文件对象
#     f.write(music_content)
# print("保存成功!")

'''批量歌曲的下载'''
import requests
import re
import execjs

headers = {
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "content-type": "application/x-www-form-urlencoded",
    "origin": "https://music.163.com",
    "priority": "u=1, i",
    "referer": "https://music.163.com/",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
cookies = {
    "NMTID": "00OHaan-8giq5QXzUZ6tbn5iIrg78oAAAGWn3AKQQ",
    "_iuqxldmzr_": "32",
    "_ntes_nnid": "3671b2313f79dba114c9570e6e773eb5,1746431642999",
    "_ntes_nuid": "3671b2313f79dba114c9570e6e773eb5",
    "WEVNSM": "1.0.0",
    "WNMCID": "zqgpkr.1746431643522.01.0",
    "sDeviceId": "YD-ZJfwg7E74lRAA0ARVFfCLZfufkQXs8LZ",
    "ntes_utid": "tid._.bJvJQj0NNZJEEgBQEVLWeJb%252BLwADtypB._.0",
    "WM_TID": "0gGhUzyN4zVEFABRUUPWfdbvf0AHYlwc",
    "__snaker__id": "siPu4DggfYCxGAPj",
    "ntes_kaola_ad": "1",
    "timing_user_id": "time_jmcpcArKIl",
    "P_INFO": "15179869369|1753187123|1|music|00&99|null&null&null#jix&360700#10#0|&0||15179869369",
    "__remember_me": "true",
    "__csrf": "0fa5699291db129daa04ede23c7b87d9",
    "MUSIC_U": "0066E505BF2DF17746E11E1486CAC9DBA70E9CFDF5A0D93A9CC96BF5F460301E32865C2EE2C8B2920BBBADBA2F71C6E8955E69819EAB28B0AB2591DD24C394E1B3095FA7645BDA7BAB853E55F65CEAFCEABE11C9AB160E758EEF7A170E5650FF8B14DC4D5F14741F60C8DA84BBE7EB1087085703D161FCAB46B6F5939DA6D1510C74A8F3EF3B60D3181A3A90168F92B691539739B745A463E39C5F15C3645EFAF1CE277B9B92E14C1935CA534CE5A871FEB297F752B44FCAEE2935ACF3989FC61820F5EFE374CA962290689D6B4C5B329266A2A773215B081E09EC888E5E277D41C65020EC18B27BF3436D08AF224BE843532E7D26F6EE19CA2780BD2BB7BC0E573F2809DCDE6112FB6C5DA596F7E16441F3E9052467CB6F1339F43715CE4B41BEA5DFCEAE8FE90030EB5A432724BCDBA2C01F00D55408EBBF2E70C7EDC37FB668D96F0D1E9DFC814AEBBC75E3DF560A0FC44EC63DFB8903247AFF8FA88A0C9326CF66E2E74338C1FCE3C2FC065B84BFAA07E3867C4969DF8650F0B1C49FD47478291AEDA10D94E57BD8A3100CC0AA4CA3233FEA5CD01034E4B90606A1FE471790",
    "gdxidpyhxdE": "ZNra3czmN2te6nR%2Fn6QYs1Djm36652h5Sf2RqclTR9o4ox2vlioVhLazDMyxPhBlJOE5intSZeBsXJKNGHx%5CD%5CEiD4iG3sb%2FqEhp%2FjmxEt3%2B%2FHdiROcU%5CIU9yzIWhp%5Ca4K2ZkDKpZeyrX7L%2F365Qz%2B%2B8IzfzXO3YiT%2Fybmd6xcVKeygS%3A1753199105175",
    "JSESSIONID-WYYY": "pBN%2Bes8FKw0%2FtiXI2tEBHKQQU1IJABRV3%5CSBF1wWGbW%2F2sEpAvKDQDhdVXBe0X6xAAWnSI8HcAEOv8%2B8N47XabKFvMD%5CFpdJmDmZF4FSyw6YkNv6tviSDz0DHGUhph49hnoSjj9DHwr38CyxtATMsfjDTMwyylzfBI%2FFSOme66v7lIrY%3A1753274187583",
    "WM_NI": "s8ufrrodGZVfhU1ngwz2fLxWM2ZTS%2FGWRw2pFASVa8zvdkiwCUp15k9ccaGHuvp4tP%2F9EeJNszPeTZaK5IfSPyoiOHda%2F1LMhf0cIpQouwkfK7e7xEis6dpHSzKcMn7rMmw%3D",
    "WM_NIKE": "9ca17ae2e6ffcda170e2e6ee8ef060b4958490cf42aeb88fa6d15a979f8aaccb3c96ebbeb5e55c97bdf7adec2af0fea7c3b92ab1e8bb87f17aadbc89bbd56eac8bff8fe67dbaeeaaadfb5d8fee96b5d22585899e98b17c869f9db7e434baaaac8cec7d818bc0d2b861fbbdad82c644b7aac0d5f75cede78b86c946b1a6a086d752a395fbaae55994a7a18ace44a8bfe1d2cf47acba0084cc7c93b1bb98ea6e89e9abd8fb4fabadfa85f34491a68584d066f5ae838ef637e2a3"
}
# 指定要下载的歌曲数量
download_count = int(input("请输入要下载的歌曲数量: "))
# 榜单链接网址（修改地方）
top_url = "https://music.163.com/discover/toplist?id=3778678"
# 获取网页数据
html_data = requests.get(top_url, headers=headers,cookies=cookies).text
# 正则表达式获取歌曲名字和ID
song_list = re.findall(r'<a href="/song\?id=(\d+)">(.*?)</a>', html_data)
# 限制下载数量
if download_count > len(song_list):
    print(f"榜单只有 {len(song_list)} 首歌曲，将下载全部歌曲")
    download_count = len(song_list)
elif download_count <= 0:
    print("下载数量必须大于0")
    exit()
print(f"开始下载前 {download_count} 首歌曲...")
# for循环遍历获取数据
i = 0
for i in range(download_count):
    music_id, title = song_list[i]
    print('歌曲名字：', title, '歌曲ID：', music_id)
    # 编译JS代码
    js_code =  execjs.compile(open('爬虫/前端/JS/网易云音乐.js',encoding='utf-8').read())
    # 获取加密参数
    i5n = {
        "ids": f"[{music_id}]",
        "level": "exhigh",
        "encodeType": "aac",
        "csrf_token": "0fa5699291db129daa04ede23c7b87d9"
    }
    # 调用JS加密代码函数
    r = js_code.call('GetEncSeckey',i5n)
    # print(r)
    url = "https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=0fa5699291db129daa04ede23c7b87d9"
    data = {
        "params": r['encText'],
        "encSecKey": r['encSecKey']
    }
    response = requests.post(url = url, headers=headers, cookies=cookies, data=data)
    # 解析数据
    # 在获取 music_url 后添加检查
    response_data = response.json()
    # print("API响应数据:", response_data)  # 调试信息

    # 检查响应数据结构
    if "data" in response_data and len(response_data["data"]) > 0:
        music_url = response_data["data"][0].get("url")
        if music_url:
            # print("歌曲链接:", music_url)
            # 获取音频数据
            music_content = requests.get(music_url, headers=headers).content
            # 保存音频数据
            with open(f"爬虫/音乐/网易云/{title}.mp3", "wb") as f:
                f.write(music_content)
            print(f"《{title}》保存成功!")
        else:
            print(f"《{title}》无法获取播放链接，没有VIP权无法播放")
    else:
        print(f"《{title}》API响应中无有效数据")