import os

# 配置路径
TS_DIR = "爬虫/视频/ts_files/"         # 存放所有 .ts 文件的目录
VIDEO_PATH = "爬虫/视频/tsxk.mp4"       # 输出的视频文件路径

# 动态获取 .ts 分片数量
ts_files = [f for f in os.listdir(TS_DIR) if f.endswith('.ts')]
TOTAL_SEGMENTS = len(ts_files)          # 自动统计分片数量

def merge_segments():
    """合并所有 .ts 分片为一个完整的视频文件"""
    print(f"🎬 开始合并视频分片，共 {TOTAL_SEGMENTS} 个分片...")

    with open(VIDEO_PATH, 'wb') as output_file:
        for i in range(1, TOTAL_SEGMENTS + 1):
            ts_path = f"{TS_DIR}{i}.ts"
            if os.path.exists(ts_path):
                with open(ts_path, 'rb') as ts_file:
                    output_file.write(ts_file.read())
                print(f"✅ 已合并分片 {i}/{TOTAL_SEGMENTS}")
            else:
                print(f"❌ 缺失分片: {i}.ts")
    
    print(f"🎉 合并完成！视频已保存至: {VIDEO_PATH}")

if __name__ == "__main__":
    merge_segments()