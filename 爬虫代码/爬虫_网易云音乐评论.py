# 优化后代码
import requests
from Crypto.Cipher import AES
import base64
import json

# 接口地址（获取歌曲评论）
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

# 请求参数模板
data = {
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    #"rid": "R_SO_4_569214247",  # 歌曲 ID 示例(多平凡的一天) （修改地方）
    #"threadId": "R_SO_4_569214247", # 评论 ID(多平凡的一天) （修改地方）
    "rid": "R_SO_4_1417849873",  # 歌曲 ID 示例(一程山路) （修改地方）
    "threadId": "R_SO_4_1417849873", # 评论 ID(一程山路) （修改地方）
}

# 固定密钥和 RSA 参数（来自 JS 加密逻辑）
g = "0CoJUm6Qyw8W8jud"  # 第一次 AES 加密密钥
i = "szYgxzGzHHh0o96d"  # 第二次 AES 加密密钥（手动写死）
e = "010001"  # RSA 公钥指数
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"

# 模拟 encSecKey（实际应为 RSA 加密结果，此处为固定值）
def get_encSeckey():
    return "1b7591a8427bc82e182205d92a54d29c78941694f38fe13348bc969efc406a8fb9a7a217e50ff3163c5b75ff2b2264689ddbf7b3f48771697caff3d96c60a92f8eba61ef57d014157d64288b68cd1c75c04516fdb8fe6c6d50cff3ac79ffcb4a643b646b7e0fe3c2d6aabcb0a1f92b1ebc6b23ff442976a57e95a9a87d7f30de"

# PKCS#7 填充函数（使数据长度为 AES 块大小的整数倍）
def pad(text):
    pad_len = 16 - (len(text) % 16)
    return text + pad_len * chr(pad_len)

# AES 加密函数（CBC 模式）
def enc_params(data, key):
    iv = "0102030405060708"
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_data = pad(data)
    encrypted = cipher.encrypt(padded_data.encode('utf-8'))  # 加密
    return base64.b64encode(encrypted).decode('utf-8')  # 返回 Base64 编码字符串

# 多层加密流程：两次 AES 加密
def get_params(data):
    first = enc_params(data, g)
    second = enc_params(first, i)
    return second

# 发送 POST 请求获取评论
response = requests.post(
    url,
    data={
        "params": get_params(json.dumps(data)),  # 加密后的 params
        "encSecKey": get_encSeckey()  # 固定 encSecKey
    },
    headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://music.163.com/",
        "Content-Type": "application/x-www-form-urlencoded"
    }
)
# 响应内容
json_data = response.json()
# 打印评论
#print(json_data)
# 检查是否请求成功
with open("爬虫/文本/热评1.txt", "w", encoding="utf-8") as f:
    # 检查是否请求成功
    if json_data.get("code") == 200:
        comments = json_data["data"].get("hotComments", [])
        print(f"共找到 {len(comments)} 条热评")

        for idx, comment in enumerate(comments, start=1):
            user = comment["user"]["nickname"]
            content = comment["content"]
            liked_count = comment["likedCount"]

            # 写入文件
            f.write(f"【{idx}】用户：{user}\n")
            f.write(f"💬 评论内容：{content}\n")
            f.write(f"👍 点赞数：{liked_count}\n")
            f.write("-" * 50 + "\n")
        print("评论已保存到文本文件。")
    else:
        error_msg = f"请求失败，状态码：{json_data.get('code')}\n详细信息：{json_data}"
        print(error_msg)
        f.write(error_msg)
f.close()
# 关闭连接
response.close()


# 加密函数
"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""
