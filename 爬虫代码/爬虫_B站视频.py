# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入json模块
import json
# 导入视频处理模块
from moviepy import VideoFileClip, AudioFileClip
# 导入文件处理模块
import os

# 批量合并视频和音频函数
def merge_video_audio(video_path: str, audio_path: str, output_path: str):
    """
    将音频文件合并到视频文件中并保存为新文件

    参数:
    video_path (str): 视频文件路径
    audio_path (str): 音频文件路径
    output_path (str): 合并后输出文件路径
    """
    try:
        # 加载视频和音频文件
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)

        # 将音频合并到视频中
        video.audio = audio

        # 写入文件
        video.write_videofile( output_path, 
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',  # 使用临时音频文件
            remove_temp=True,                 # 合成后删除临时文件
            threads=8,                        # 使用多线程
            preset='ultrafast',               # 使用最快的编码预设
            ffmpeg_params=["-crf", "23"] )

        # 关闭资源
        video.close()
        audio.close()

        print(f"合并完成!")
    except Exception as e:
        print(f"合并失败：{e}")
def batch_merge_videos(base_path: str):
    """
    批量合并B站文件夹下相同名字的视频和音频文件
    
    参数:
    base_path (str): B站视频文件夹路径
    """
    # 获取文件夹中所有文件名（不含扩展名）
    files = os.listdir(base_path)
    file_names = set()
    
    # 提取所有不带扩展名的文件名
    for file in files:
        if file.endswith('.mp4') or file.endswith('.mp3'):
            file_names.add(os.path.splitext(file)[0])
    
    # 遍历每个文件名，合并对应的视频和音频
    for name in file_names:
        video_path = os.path.join(base_path, f"{name}.mp4")
        audio_path = os.path.join(base_path, f"{name}.mp3")
        output_path = os.path.join(base_path, f"[完整]{name}.mp4")
        
        # 检查视频和音频文件是否存在
        if os.path.exists(video_path) and os.path.exists(audio_path):
            print(f"正在合并......")
            merge_video_audio(video_path, audio_path, output_path)
             # 合并成功后删除原始文件
            try:
                os.remove(video_path)
                os.remove(audio_path)
                print(f"已删除原始文件!")
            except Exception as e:
                print(f"删除原始文件失败: {e}")
        else:
            print(f"缺少文件，跳过!")
# 清理文件名，移除非法字符
def clean_filename(filename: str) -> str:
    """
    清理文件名，移除非法字符
    
    参数:
    filename (str): 原始文件名
    
    返回:
    str: 清理后的文件名
    """
    # 定义非法字符并替换为下划线
    illegal_chars = r'[\\/:*?"<>|]'
    cleaned_name = re.sub(illegal_chars, '_', filename)
    
    # 移除首尾空格并限制长度
    cleaned_name = cleaned_name.strip()
    
    # 限制文件名长度（Windows路径限制）
    if len(cleaned_name) > 150:
        cleaned_name = cleaned_name[:150]
    
    return cleaned_name
cookie = 'APP_ANON=A=EA6F216F978C9B1C099EDADBFFFFFFFF; els=%7b%22account_type%22%3a%22MSA%22%7d; MUID=3CF49D042282636D31A18E3123FE6200; currentaccount=%7B%22login_hint%22%3A%22M%24EjB4nON4svPU-sOXdu9VFhI0MjA1NTU3MjA2dSgs1EvOz5VYvvrKmR__gYARAGagEwI%22%2C%22account_type%22%3A%22MSA%22%7D; USRLOC=; OptanonAlertBoxClosed=2024-11-22T07:26:46.357Z; msnup=%7B%22cnex%22%3A%22no%22%7D; aace=%7b%22child%22%3a0%2c%22expiredOn%22%3a%222025-09-11T06%3a09%3a36%22%7d; eupubconsent-v2=CQIgXhzQIgXhzAcABBENB-CsAP_AAEPAACiQIhNX_G__bXlj8X53aftkeY1f99h7rsQxBhaJk-4FzJvW_JwX32E7NAz6pqIKmRIAu3DBAQFlHIDURUCgaIgVqSDMaEyUoTNKJ6BEiFMRY2dYCFxvm4lDeQCY5vr991d52B-t7Nr83dTyy4hHv3a5_0S0WAAAAYANDLv9bROb29AOd_x8v4v4_F7pBD-AmADgAZQA6ACKAGfAZYAzMBuYDtoIJggoBBgCDYEIQIVwQuBC8CGYEOYIeAh6BD8A4JA3AAQAAuACgAKgAcAA8ACAAGUANAA1AB4AEQAJgAVQA3gB6AD8AISAQwBEgCOAEsAJoAYYAywBsgDvgHsAfEA-wD9AIBARcBGACNAFBAKuAXMAxQBogDaAG4AOIAh0BIgCdgFDgKRAWwAuQBd4C8wGGgMkAZOAy4BnMDWANZAbeA8cB7QQBVAA4ADwASABGAC2AH8AagA5wCDgE_AKGAdUBF4CPQEigJWATaAp8BYQC6AF1ALyAYEAxABi0DIQMjAZMA0IBowDUwG0ANuAboA4IB2ADugHlAPkAfYA_cCAgEDAIIhgCAARgAqABbADeAKQAagBLQClgHUAReAkUBYgDAgGRgNCAboIAHgAkABqAEYALYAbwBSADUAJaAUsA3gCLwEigMCAaEA3QUAKAFIANQAloB1QEegJFAWIA0IBrwD7BgAkAGoApABqAEtAOqAj0BYgDQgH2DgH4ACIAHAAeABcAEgAOQAfgBGAC2AGgAP4AhABSADNAGoAOcAdwBAICDgIQARGAnwCfgFLAKgAXoA3gB0gDqgHyAQgAj0BIoCVgExAJlATaApABSYCqgFdgLUgXQBdQC9gF9AMCAYgAxYBkIDJgGXgNCAaMA00BqYDXgG0ANsAbcA7AB5QD4gH2QP2A_cCB4EER0EQABcAFAAVAA4ACAAFwAMoAaABqADwAIgATAAqwBcAF0AMQAbwA9AB-gEMARIAlgBNACjAGGAMoAaIA2QB3gD2gH2AfsBFgEYAKCAVcAsQBcwC8gGKANoAbgA4gB1AEOgIvASIAmQBOwChwFNAKsAWKAtgBcAC5AF2gLvAXmAw0BjwDJAGTgMqAZYAy4BnIDVQGsANvAeOA9oB9YEASACEABAAaAA_gCkAGoAOcAnwBSwCxAGEAN4AdUBHoCYgE2gKTAXkAvYBgQDQgGpgNsAbcA6MB2ADygHxAPsAfsBA8CDAEGwIVkIDQACwAKAAuACqAFwAMQAbwA9ACOAHeASkAoIBVwC5gGKANoAdQBTQCxQFogLgAXIAycBnIDVQHjkoEAACAAFgAUAA4ADwAIgATAAqgBcADFAIYAiQBHACjAGyAO8AfgBVwDFAHUAQ6Ai8BIgCxQFsALzAZOAywBnIDWAG3gPaAgeSAOgAOAAuADkAKgAZAA3gCEAFIAL4AagA7gCAAEtAKgAbwA6oCPQEigJWATaApMBewDFgG5AOwAeUA-wB-4EESkDAABcAFAAVAA4ACAAGQANAAeABEACYAFUAMQAfoBDAESAKMAZQA0QBsgDvgH2AfoBFgCMAFBAKuAXMAvIBigDaAG4AQ6Ai8BIgCdgFDgLFAWwAuABcgC7QF5gMNAZIAycBlwDOYGsAayA28B44D2igDUAC4AJAAcgBGACoAGQANoAbwBCACOAEyAKQAagA5wB3AEAAJEAScAloBOwClgFiALqAYAA14BvADqgHbAP-Aj0BIoCYgEygJtAUgAp8BXYC6AF5AL6AYEAxYBk0DUgNTAa8A4IB2ADygHxAPsgfsB-4EDAIHgAA.f_gAD_gAAAAA; _EDGE_S=SID=0EB1DC6E5EEB6C453A0FC9B55FAC6D6B; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Apr+27+2025+14%3A12%3A43+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202501.2.0&isIABGlobal=false&hosts=&consentId=11211ffb-158d-4526-9dca-d4d3177a12ff&interactionCount=3&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1%2CC0008%3A1%2CV2STACK42%3A0&AwaitingReconsent=false&geolocation=%3B&browserGpcFlag=0&isAnonUser=1; _C_ETH=1'
# 限制下载数量 （第二修改地方）
download_limit = 4
# up主mid （第二修改地方）
mid = 396395171
headers = {
        # Referer 防盗链 告诉服务器你请求链接是从哪里跳转过来的
        "Referer": f'https://space.bilibili.com/{mid}?spm_id_from=333.788.upinfo.head.click',
        # User-Agent 用户代理, 表示浏览器/设备基本身份信息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Cookie": cookie
}
# 请求网址 （第一修改地方）
link = f'https://api.bilibili.com/x/space/wbi/arc/search?mid=396395171&order=pubdate&ps=25&pn=1&index=1&order_avoided=true&platform=web&web_location=333.1387&dm_img_list=[]&dm_img_str=V2ViR0wgMS4wIChPcGVuR0wgRVMgMi4wIENocm9taXVtKQ&dm_cover_img_str=QU5HTEUgKEludGVsLCBJbnRlbChSKSBJcmlzKFIpIFhlIEdyYXBoaWNzICgweDAwMDA0NkE2KSBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKUdvb2dsZSBJbmMuIChJbnRlbC&dm_img_inter=%7B%22ds%22:[],%22wh%22:[3629,5833,3],%22of%22:[513,1026,513]%7D&w_webid=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzcG1faWQiOiIzMzMuMTM4NyIsImJ1dmlkIjoiRDdEMEVDQ0EtOTFCMS1GNjA4LUQ0RDktODk5QUI0QzE0NDc4NDIxOTRpbmZvYyIsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM4LjAuMC4wIFNhZmFyaS81MzcuMzYgRWRnLzEzOC4wLjAuMCIsImJ1dmlkX2ZwIjoiZTZmNmRlZDcwMTAzN2M2NjQwZmZiMWZiM2NlOTYzMzYiLCJiaWxpX3RpY2tldCI6ImV5SmhiR2NpT2lKSVV6STFOaUlzSW10cFpDSTZJbk13TXlJc0luUjVjQ0k2SWtwWFZDSjkuZXlKbGVIQWlPakUzTlRRd01qYzROakFzSW1saGRDSTZNVGMxTXpjMk9EWXdNQ3dpY0d4MElqb3RNWDAucWVEVFhSQVpESlRhV2NqVjNMNXpqVnN5SlVDNXF1RmFabnItSEphTzJzQSIsImNyZWF0ZWRfYXQiOjE3NTM4MDE0MjYsInR0bCI6ODY0MDAsInVybCI6Ii8zOTYzOTUxNzE_c3BtX2lkX2Zyb209MzMzLjc4OC51cGluZm8uaGVhZC5jbGljayIsInJlc3VsdCI6MCwiaXNzIjoiZ2FpYSIsImlhdCI6MTc1MzgwMTQyNn0.mF9YTYawt2gt5qd6C1azjxF8efs43S28W0F8tfX-1pSxSBczGYWhonCy6WMs0urUK35jLs3jPl-8hH5ZxSQ6qjtWcXWv8xbkXnt33-skcgVTolq1UcErHi21gpzRUIqWmjVn-eCB2zFeRa6RaWCAkH5dYU93KkKspY-96V9l5EwQxaZYkeRl-tk3r01jQ5J-qtUU9O0gbgKXedtMJknyk__vbn_yexeMXtczA2X3pBJAGPW7x6wkdeyXw_V9B3bT7ofN3LNJRrYtA3IPvOPfK7wjPEEWvFOCvhgXXdrjvhiEMycuhS2N-rUGX-uDP2Z5wAxdjRhmLr4hcHZW9l_HVA&w_rid=a0f9f54e021373448ad62b079dd218ea&wts=1753801427'
# 发送请求，获取响应的json数据
link_json = requests.get(url=link, headers=headers).json()
# 取值，对应的BV号码
bv_num = link_json['data']['list']['vlist']
download_count = 0
# 下载所有视频
for id in bv_num:
    # 检查是否达到下载限制
    if download_limit is not None and download_count >= download_limit:
        print(f"已达到下载限制数量 {download_limit}，停止下载")
        break
    video_id = id['bvid']
    url = f'https://www.bilibili.com/video/{video_id}'
    # 发送请求
    response = requests.get(url=url, headers=headers)
    html = response.text
    
    # 解析数据: 提取视频标题
    title = re.findall('title="(.*?)"', html)[0]
    print(title)
    
    # 清理文件名
    clean_title = clean_filename(title)
    print(f"清理后的文件名: {clean_title}")
    
    # 提取视频信息
    info = re.findall('window.__playinfo__=(.*?)</script>', html)[0]
    # info -> json字符串转成json字典
    json_data = json.loads(info)
    # 提取视频链接
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # 提取音频链接
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    
    video_content = requests.get(url=video_url, headers=headers).content
    # 获取音频内容
    audio_content = requests.get(url=audio_url, headers=headers).content
    # 保存数据
    with open(f'爬虫\\视频\\B站\\{clean_title}.mp4', mode='wb') as f:
        f.write(video_content)
    with open(f'爬虫\\视频\\B站\\{clean_title}.mp3', mode='wb') as f:
        f.write(audio_content)
    print("保存完成!")
     # 增加下载计数
    download_count += 1

# 所有视频下载完成后再进行批量合并
print("开始批量合并视频和音频...")
batch_merge_videos(base_path=f"爬虫\\视频\\B站")
print("所有任务完成!")

# import os
# import multiprocessing

# # 获取CPU核心数
# cpu_count = os.cpu_count()
# print(f"CPU核心数: {cpu_count}")

# # 线程数建议范围
# recommended_threads = cpu_count * 2  # 通常是CPU核心数的1-2倍
# print(f"建议线程数范围: 1-{recommended_threads}")