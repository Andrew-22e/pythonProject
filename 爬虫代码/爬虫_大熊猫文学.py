"""经过AI优化过的完整版，下载缺失章节目前还存在问题"""

import requests
import parsel
import re
import tqdm
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# 创建session对象，复用TCP连接
session = requests.Session()
session.headers.update({
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "referer": "https://www.dxmwx.org/chapter/43904.html",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
})

cookies = {
    "ASP.NET_SessionId": "jek0fl2lpe1o4t0quhtb1qse",
    "_ga": "GA1.1.367481829.1754482768",
    "TokenId": "41BF3B1F2ADFEDED39D3C8D08B22845F5C36C23DB96F9B7E8BC36D8EC7BD21222A71662BA3C466052596628DB35F5D99",
    "_ga_829J453C49": "GS2.1.s1754482767$o1$g1$t1754482854$j53$l0$h0"
}

def download_chapter(ID):
    """下载单个章节"""
    try:
        url = f"https://www.dxmwx.org/read/{ID}.html"
        response = session.get(url, cookies=cookies, timeout=15)
        response.raise_for_status()
        
        # 解析数据
        html = response.text
        selector = parsel.Selector(html)
        title = selector.css('#ChapterTitle::text').get()
        content_list = selector.css('#Lab_Contents p::text').getall()
        
        if not title or not content_list:
            return ID, None, None
            
        content = '\n\n'.join(content_list)
        return ID, title, content
    except Exception as e:
        print(f"下载章节 {ID} 时出错: {e}")
        return ID, None, None

def load_downloaded_chapters(info_file):
    """加载已下载章节信息"""
    if os.path.exists(info_file):
        with open(info_file, 'r', encoding='utf-8') as f:
            return set(json.load(f))
    return set()

def save_downloaded_chapters(info_file, downloaded_ids):
    """保存已下载章节信息"""
    with open(info_file, 'w', encoding='utf-8') as f:
        json.dump(list(downloaded_ids), f, ensure_ascii=False, indent=2)

def rebuild_novel_file(txt_file, IDList, chapters_data):
    """按顺序重新构建小说文件"""
    with open(txt_file, 'w', encoding='utf-8') as f:
        for ID in IDList:
            if ID in chapters_data and chapters_data[ID][0] and chapters_data[ID][1]:
                title, content = chapters_data[ID]
                f.write(title + '\n' + content + '\n\n')

# 小说ID
link = "https://www.dxmwx.org/chapter/43904.html"
resp = session.get(link, cookies=cookies)
IDList = re.findall('<a href="/read/(.*?).html"', resp.text)

# 文件路径
novel_name = "剑来"
txt_file = f'爬虫\\文本\\{novel_name}.txt'
info_file = f'爬虫\\文本\\{novel_name}_downloaded.json'

# 加载已下载的章节ID
downloaded_ids = load_downloaded_chapters(info_file)

print(f"总共找到 {len(IDList)} 个章节")
print(f"已下载 {len(downloaded_ids)} 个章节")

# 确定需要下载的章节
missing_ids = [ID for ID in IDList if ID not in downloaded_ids]
print(f"其中 {len(missing_ids)} 个未下载")

if not missing_ids:
    print("所有章节均已下载完成！")
else:
    print(f"开始下载 {len(missing_ids)} 个缺失章节...")
    
    # 下载缺失的章节
    new_chapters = {}
    failed_chapters = []
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_id = {executor.submit(download_chapter, ID): ID for ID in missing_ids}
        
        for future in tqdm.tqdm(as_completed(future_to_id), total=len(missing_ids), desc="下载进度"):
            ID, title, content = future.result()
            if title and content:
                new_chapters[ID] = (title, content)
                downloaded_ids.add(ID)
            else:
                failed_chapters.append(ID)
    
    # 重新下载所有成功章节以确保顺序正确
    print("重新加载所有成功章节以确保顺序...")
    all_chapters = {}
    
    success_ids = [ID for ID in IDList if ID in downloaded_ids]
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_id = {executor.submit(download_chapter, ID): ID for ID in success_ids}
        
        for future in tqdm.tqdm(as_completed(future_to_id), total=len(success_ids), desc="验证章节"):
            ID, title, content = future.result()
            if title and content:
                all_chapters[ID] = (title, content)
    
    # 按正确顺序重建文件
    rebuild_novel_file(txt_file, IDList, all_chapters)
    
    # 更新下载状态
    save_downloaded_chapters(info_file, downloaded_ids)
    
    print(f"成功下载 {len(new_chapters)} 个新章节")
    
    if failed_chapters:
        print(f"{len(failed_chapters)} 个章节下载失败: {failed_chapters}")

print('下载完成！')