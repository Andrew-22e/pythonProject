import requests
import time
import csv
import json
from urllib.parse import urljoin
from DrissionPage import ChromiumPage

# 创建会话对象，自动管理cookie
session = requests.Session()

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
    "priority": "u=1, i",
    "referer": "https://www.zhipin.com/web/geek/jobs?city=101210100&query=python%E5%AE%9E%E4%B9%A0",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Microsoft Edge\";v=\"138\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "x-requested-with": "XMLHttpRequest"
}

# 设置会话的headers
session.headers.update(headers)

def init_session_with_manual_cookies():
    """
    使用手动设置的cookies初始化会话
    你可以将从浏览器中获取的有效cookies放在这里
    """
    print("正在使用预设cookies初始化会话...")
    
    # 请在这里填入你从浏览器中获取的最新有效cookies
    # 获取方法：在浏览器中登录BOSS直聘后，按F12打开开发者工具，
    # 刷新页面，在Network标签中找到请求，查看Request Headers中的Cookie
    cookies = {
        # 示例格式（请替换为实际有效的cookies）：
        # "__zp_stoken__": "your_token_here",
        # "wt2": "your_wt2_value",
        # 添加其他必要的cookies...

    }
    
    if cookies:
        session.cookies.update(cookies)
        print("已设置预设cookies")
        return True
    else:
        print("未提供cookies，尝试自动获取...")
        return init_session_auto()

def init_session_auto():
    """
    自动初始化会话，访问主页获取初始cookies
    """
    print("正在自动初始化会话...")
    home_url = "https://www.zhipin.com/web/geek/jobs?city=101210100&query=python%E5%AE%9E%E4%B9%A0"
    
    try:
        # 访问主页以获取初始cookies
        home_response = session.get(home_url, timeout=10)
        print(f"主页响应状态码: {home_response.status_code}")
        print(f"主页Cookies: {dict(session.cookies)}")
        
        if home_response.status_code == 200:
            print("会话初始化完成")
            return True
        else:
            print(f"主页访问失败，状态码: {home_response.status_code}")
            return False
    except Exception as e:
        print(f"会话初始化失败: {e}")
        return False

def get_job_data_with_retry(page, max_retries=3):
    """
    获取指定页码的职位数据，带重试机制
    """
    url = "https://www.zhipin.com/wapi/zpgeek/search/joblist.json"
    try:
        t = int(time.time() * 1000)
        params = {
            "page": page,
            "pageSize": "15",
            "city": "101210100",
            "expectInfo": "",
            "query": "python实习",
            "multiSubway": "",
            "multiBusinessDistrict": "",
            "position": "",
            "jobType": "",
            "salary": "",
            "experience": "",
            "degree": "",
            "industry": "",
            "scale": "",
            "stage": "",
            "scene": "1",
            "_": t
        }
        
        # print(f"正在请求第{page}页数据... (尝试 {attempt + 1}/{max_retries})")
        response = session.get(url, params=params, timeout=10)
        # print(f"第{page}页响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            try:
                json_data = response.json()
                #print(f"第{page}页返回数据结构: {list(json_data.keys()) if isinstance(json_data, dict) else 'Not a dict'}")
                if isinstance(json_data, dict) and json_data.get('code') == 0:
                    return json_data
                else:
                    print(f"API返回错误码: {json_data.get('code', 'N/A')}, 消息: {json_data.get('message', 'N/A')}")
            except json.JSONDecodeError as je:
                print(f"第{page}页响应不是有效的JSON格式: {je}")
                print(f"响应内容前200字符: {response.text[:200]}")
        else:
            print(f"第{page}页请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:200]}")
            
    except Exception as e:
        print(f"获取第{page}页数据失败: {e}")

    return None

# 初始化会话
if not init_session_with_manual_cookies():
    print("无法初始化会话，程序退出")
    exit(1)

# 只在第一次写入时写入表头
header_written = False

for i in range(1, 6):
    print(f"\n正在获取第{i}页数据...")
    
    # 获取数据
    json_data = get_job_data_with_retry(i)
    
    # 打印调试信息
    if json_data:
        # print(f"获取到的数据类型: {type(json_data)}")
        if isinstance(json_data, dict):
            # print(f"数据顶层键: {list(json_data.keys())}")
            if 'code' in json_data:
                print(f"响应码: {json_data['code']}")
            if 'message' in json_data:
                print(f"响应消息: {json_data['message']}")
    
    if not json_data:
        print(f"第{i}页未获取到数据")
        continue
        
    if not isinstance(json_data, dict):
        print(f"第{i}页数据格式不正确，不是字典类型")
        continue
        
    # 检查API是否返回成功
    if json_data.get('code') != 0:
        print(f"第{i}页API调用失败，错误码: {json_data.get('code')}, 消息: {json_data.get('message')}")
        continue
        
    if 'zpData' not in json_data:
        print(f"第{i}页数据缺少'zpData'字段")
        print(f"完整响应: {json_data}")
        continue
        
    if 'jobList' not in json_data['zpData']:
        print(f"第{i}页数据缺少'jobList'字段")
        print(f"zpData内容: {json_data['zpData']}")
        continue
    
    info_list = json_data['zpData']['jobList']
    
    # 如果没有数据，跳出循环
    if not info_list:
        print(f"第{i}页没有数据")
        break

    # 打开CSV文件进行写入
    with open(r'爬虫\文本\python实习职位.csv', 'a', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['职位名称', '实习时间', '每周工作天数', '学历要求', '薪资', '行业', '地区', '公司名称', '公司规模', '技能要求']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # 只在第一次写入表头
        if not header_written:
            writer.writeheader()
            header_written = True

        # 遍历并写入每条记录
        for info in info_list:
            title = info.get('jobName', '')
            ExercitationTime = info.get('leastMonthDesc', '')
            daysPerWeekDesc = info.get('daysPerWeekDesc', '')
            degree = info.get('jobDegree', '')
            salary = info.get('salaryDesc', '')
            brandIndustry = info.get('brandIndustry', '')
            areaDistrict = info.get('areaDistrict', '')
            brandName = info.get('brandName', '')
            brandScaleName = info.get('brandScaleName', '')
            skills = ', '.join(info.get('skills', [])) if info.get('skills') else ''
            
            writer.writerow({
                '职位名称': title,
                '实习时间': ExercitationTime,
                '每周工作天数': daysPerWeekDesc,
                '学历要求': degree,
                '薪资': salary,
                '行业': brandIndustry,
                '地区': areaDistrict,
                '公司名称': brandName,
                '公司规模': brandScaleName,
                '技能要求': skills
            })
    
    # 添加延迟，避免请求过于频繁
    time.sleep(1)

print("\n程序执行结束！")

# import requests
# import time
# import csv
# import json
# from urllib.parse import urljoin
# from DrissionPage import ChromiumPage

# dp = ChromiumPage()
# dp.listen.start('zpgeek/search/joblist.json')
# dp.get('https://www.zhipin.com/web/geek/jobs?city=101210100&position=120113&jobType=1901&degree=203')
# resp = dp.listen.wait()
# json_data = resp.response.body
# # print(json_data)
# # 向下滚动 200 像素
# for i in range(1, 5):
#     info_list = json_data['zpData']['jobList']
#     for info in info_list:
#         title = info.get('jobName', '')
#         ExercitationTime = info.get('leastMonthDesc', '')
#         daysPerWeekDesc = info.get('daysPerWeekDesc', '')
#         degree = info.get('jobDegree', '')
#         salary = info.get('salaryDesc', '')
#         brandIndustry = info.get('brandIndustry', '')
#         areaDistrict = info.get('areaDistrict', '')
#         brandName = info.get('brandName', '')
#         brandScaleName = info.get('brandScaleName', '')
#         skills = ', '.join(info.get('skills', [])) if info.get('skills') else ''
        
#         print({
#             '职位名称': title,
#             '实习时间': ExercitationTime,
#             '每周工作天数': daysPerWeekDesc,
#             '学历要求': degree,
#             '薪资': salary,
#             '行业': brandIndustry,
#             '地区': areaDistrict,
#             '公司名称': brandName,
#             '公司规模': brandScaleName,
#             '技能要求': skills
#         })
#     down = dp.ele('css:.inner home-inner')
#     dp.scroll.to_see(down)