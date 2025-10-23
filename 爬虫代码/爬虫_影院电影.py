import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import os
import time

# =================== 配置区域 ===================
headers = {
    "User-Agent": "Mozilla/5.0",
    # "Referer": "https://www.lzcdn.com"  # 如果不工作可先注释掉
}

TS_DIR = "爬虫/视频/ts_files/"
VIDEO_PATH = "爬虫/视频/1990.mp4"
TOTAL_SEGMENTS = 2034

os.makedirs(TS_DIR, exist_ok=True)
# =================================================

def download_ts(i):
    ts_path = f"{TS_DIR}{i}.ts"
    if os.path.exists(ts_path):  # 断点续传
        return True
    #（修改地方）
    url = f"https://v.lzcdn25.com/20250430/422_9c65e42c/2000k/hls/2e379ce697d0{i:05d}.ts"

    try:
        resp = requests.get(url, headers=headers, timeout=15)
        if resp.status_code == 200:
            with open(ts_path, 'wb') as f:
                f.write(resp.content)
            return True
        else:
            print(f"[{i}] 下载失败 | 状态码: {resp.status_code}")
            return False
    except Exception as e:
        print(f"[{i}] 异常 | 错误: {e}")
        return False

def main():
    print(f"🎬 开始下载电影，共 {TOTAL_SEGMENTS} 个分片...")

    # 检查已存在的 .ts 文件数量
    existing_files = [f for f in os.listdir(TS_DIR) if f.endswith('.ts')]
    downloaded_count = len(existing_files)
    print(f"📁 已存在 {downloaded_count} 个分片，将下载剩余 {TOTAL_SEGMENTS - downloaded_count} 个分片...")

    # 计算尚未下载的分片
    all_indices = list(range(1, TOTAL_SEGMENTS + 1))
    remaining_indices = [
        i for i in all_indices
        if not os.path.exists(f"{TS_DIR}{i}.ts")
    ]

    success_count = 0
    batch_size = 10

    with ThreadPoolExecutor(max_workers=5) as executor:
        for i in range(0, len(remaining_indices), batch_size):
            batch = remaining_indices[i:i + batch_size]
            futures = [executor.submit(download_ts, idx) for idx in batch]

            for future in tqdm(as_completed(futures), total=len(batch), desc=f"📥 下载批次 {i // batch_size + 1}"):
                if future.result():
                    success_count += 1

            if i + batch_size < len(remaining_indices):
                print("⏳ 暂停 2 秒...")
                time.sleep(2)

    print(f"✅ 共下载 {success_count} 个新分片，总计 {downloaded_count + success_count}/{TOTAL_SEGMENTS} 个分片")

if __name__ == '__main__':
    main()