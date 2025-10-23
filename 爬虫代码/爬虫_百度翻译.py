import requests

url = "https://fanyi.baidu.com/sug"
data = {
    "kw": input("请输入要翻译的单词：")
}
response = requests.post(url, data=data)
json_data = response.json()
print(json_data["data"][0]["v"])
response.close()