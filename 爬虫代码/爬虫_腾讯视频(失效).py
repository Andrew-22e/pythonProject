# # 爬虫实现的基本步骤
# # 一、数据来源分析：明确需求、抓包分析
# # 二、代码实现：发送请求、获取数据、解析数据、保存数据

# # 如果返回403错误，可以尝试添加防盗链
# # key加密参数需要逆向处理，响应数据中的密文需要逆向解密

# 引入相关库
import aiohttp # 异步请求库
import asyncio # 异步处理库
import requests # 同步请求库
import re # 正则库
import os # 操作系统库
from tqdm import tqdm # 进度条库
from urllib.parse import quote # url编码库
import time # 时间库
import execjs # JS执行库

# 模拟浏览器 headers（已提取自你的文件）
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cookie": "_ga=GA1.1.993021357.1746456437; language=cn; _ga_RDEPQPJKET=GS2.1.s1752497617$o14$g1$t1752497619$j58$l0$h0; i18n_redirected=cn",
    "kdsystem": "GreenVideo",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "referer": "https://jx.vcs6.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}

# 异步下载单个 ts 文件
async def download_ts(session, ts_url, filename, pbar):
    async with session.get(ts_url) as response:
        if response.status == 200:
            content = await response.read()
            with open(filename, 'wb') as f:
                f.write(content)
        pbar.update(1)
# 异步批量下载所有 ts 文件
def get_expected_ts_files(ts_list, output_dir):
    expected_files = set(range(len(ts_list)))
    existing_files = set()

    for file in os.listdir(output_dir):
        if file.endswith(".ts"):
            try:
                idx = int(file.split(".")[0])
                existing_files.add(idx)
            except ValueError:
                continue

    missing_files = sorted(expected_files - existing_files)
    return missing_files
# 异步批量下载所有 ts 文件
async def download_all_ts(ts_list, base_url, output_dir="爬虫/视频/ts_files"):
    os.makedirs(output_dir, exist_ok=True)

    # 获取缺失的分片索引
    missing_indices = get_expected_ts_files(ts_list, output_dir)
    
    if not missing_indices:
        print("✅ 所有分片已完整下载，无需补充")
        return

    print(f"⚠️ 发现 {len(missing_indices)} 个缺失分片，正在补充下载...")

    connector = aiohttp.TCPConnector(limit_per_host=10, ssl=False)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        tasks = []
        with tqdm(total=len(missing_indices), desc="补充下载缺失TS") as pbar:
            for idx in missing_indices:
                ts = ts_list[idx]
                ts_url = base_url + ts
                file_path = os.path.join(output_dir, f"{idx}.ts")
                task = download_ts(session, ts_url, file_path, pbar)
                tasks.append(task)
            await asyncio.gather(*tasks)

    print("✅ 补充下载完成")
# 主函数
async def main():
    # 视频链接地址
    # play_url = 'https://v.qq.com/x/cover/324olz7ilvo2j5f/t0035aw2v35.html'
    # # 获取m3u8密文
    # link = 'https://59.153.166.174:4433/xmflv.js'
    # # 获取时间戳
    # NowTime = int(time.time())
    # # 获取key密文,编译js加密代码
    # js_code = execjs.compile(open('爬虫/前端/JS/腾讯视频.js',encoding='utf-8').read())
    # key  = js_code.call('sign',NowTime,quote(play_url))
    # # 请求参数
    # data = {
    #     'wap':'0',
    #     'url':quote(play_url),
    #     'time':NowTime,
    #     'key':key,
    #     'area':'CMNET|JiangXi-117.170.109.62',
    # }
    # print(data)
    # try:
    #     # 发送请求获取json数据
    #     response = requests.post(url=link, data=data, headers=headers)
    #     response.raise_for_status()  # 检查请求是否成功
    #     json_data = response.json()
    #     print("成功获取json数据",json_data)
    # except requests.exceptions.RequestException as e:
    #     print(f"❌ 请求失败: {e}")
    #     return
    # except ValueError:
    #     print("❌ 响应内容不是有效的 JSON")
    #     print("响应内容:", response.text[:200])  # 只打印前200个字符
    #     return
    # try:
    #     json_data = requests.post(url=link, data=data, headers=headers).json()
    #     print(json_data)
    # except requests.exceptions.RequestException as e:
    #     print("❌ 请求失败:", e)
    # except ValueError:
    #     print("❌ 响应内容不是有效的 JSON")
    #     print("响应内容:", requests.post(url=link, data=data, headers=headers).text)
    # exit()

    url = "https://cache.hls.one/Cache/zyhls/e8dd33c8f344540d32112201fc4fd7c4.m3u8?vkey=393239664277565243465a544241674a4277565856774256446c4a5a425145424177565742464e51416730414177514444564d50"
    # 获取 m3u8 内容
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            m3u8_content = await resp.text()

    # 解析 ts 列表
    ts_list = re.findall(r',\n(.*?)\n#', m3u8_content)
    base_url = '/'.join(url.split('/')[:-1]) + '/'

    # 下载
    await download_all_ts(ts_list, base_url)
    print('下载完成!')
# 运行主程序
if __name__ == "__main__":
    asyncio.run(main())

# import requests


# headers = {
#     "accept": "*/*",
#     "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
#     "origin": "https://jx.xmflv.cc",
#     "priority": "u=1, i",
#     "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "cross-site",
#     "referer": "https://jx.vcs6.com/",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
# }
# url = "https://cache.hls.one/Cache/zyhls/1739ca2bf3edad59db8ca5a0c4ab2fa7.m3u8"
# params = {
#     "vkey": "653130394141525541674d46557745455651304843466f4e4251594f414155475631645255514d4555314547554149454146594c"
# }
# response = requests.get(url, headers=headers, params=params)

# print(response.text)
# print(response)