# 导入自动化模块
from DrissionPage import ChromiumPage
import requests
import time
# import pyecharts.options as opts
# from pyecharts.charts import Calendar

headers = {
    'referer': 'https://www.douyin.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
# 实例化浏览器对象
dp = ChromiumPage()
# 监听数据包
dp.listen.start('aweme/v1/web/aweme/post/')
# 访问网址 （修改地方，博主视频主页）
dp.get("https://www.douyin.com/user/MS4wLjABAAAA2q7d7IguhZR_2APXu67r93zZX7ZYBc3oThd-qgFy4VhRVrxJLiPLylPKJQSqTzAl?from_tab_name=main&vid=7533947483454475572")
# 构建循环翻页
for i in range(1,3):
    # 等待数据包加载
    resp = dp.listen.wait()
    # 获取数据
    json_data = resp.response.body
    #print(json_data)
    # 解析数据
    info_list = json_data['aweme_list']
    for info in info_list:
        aweme_id = info['aweme_id']
        title = info['desc']
        video_url = info['video']['play_addr']['url_list'][0]
        print(title, video_url)
        #  # 下载视频
        # video_content = requests.get(url=video_url,headers=headers).content
        # with open(f'爬虫\视频\抖音\{title}.mp4', 'wb') as f:
        #     f.write(video_content)
        # print(f'{title}下载完成')
        # break
    # 翻页
    down = dp.ele('css:.Rcc71LyU')
    dp.scroll.to_see(down)