import asyncio
import aiohttp
import os

# ✅ 正确构建 urls 列表 （修改地方）
urls = [
    f"https://v.lzcdn25.com/20250430/422_9c65e42c/2000k/hls/2e379ce697d0{i:05d}.ts"
    for i in range(1900, 2035)
]

async def download_ts(url):
    last_part = url.rsplit('/', 1)[-1]  # 获取文件名部分
    number_part = last_part.rsplit('.', 1)[0]  # 去掉 .ts 后缀
    name = number_part.rsplit('d', 1)[-1]  # 提取 d 后面的数字字符串
    file_number = int(name)  # 转换为整数避免前导 0 问题
    filename = f"爬虫/视频/ts_files/{file_number}.ts"  # 构造带扩展名的路径

    # ✅ 检查文件是否已存在
    if os.path.exists(filename):
        print(f"{filename} 已存在，跳过下载")
        return

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                # 创建目录（如果不存在）
                os.makedirs(os.path.dirname(filename), exist_ok=True)
                with open(filename, 'wb') as f:
                    f.write(await resp.content.read())
                print(f"{filename} 下载完成")
            else:
                print(f"{url} 请求失败，状态码：{resp.status}")
async def main():
    tasks = [asyncio.create_task(download_ts(url)) for url in urls]
    await asyncio.gather(*tasks)  # 更推荐使用 asyncio.gather

if __name__ == "__main__":
    asyncio.run(main())