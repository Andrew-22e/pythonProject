import requests
import json
import execjs
import time

def create_js_environment():
    """创建JavaScript运行环境"""
    try:
        # 读取必要的JavaScript文件
        with open(r'c:\lj666\VScode\python\爬虫\前端\JS\五矿逆向补环境\env.js', 'r', encoding='utf-8') as f:
            env_js = f.read()
            
        with open(r'c:\lj666\VScode\python\爬虫\前端\JS\五矿逆向补环境\loader.js', 'r', encoding='utf-8') as f:
            loader_js = f.read()
            
        with open('爬虫/前端/JS/五矿.js', 'r', encoding='utf-8') as f:
            main_js = f.read()
        
        # 创建JavaScript运行环境
        ctx = execjs.compile(env_js + "\n" + loader_js + "\n" + main_js)
        return ctx
    except Exception as e:
        print(f"创建JavaScript环境时出错: {e}")
        return None

def fetch_public_data():
    """获取公共数据"""
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "Origin": "https://ec.minmetals.com.cn",
        "Pragma": "no-cache",
        "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"140\", \"Chromium\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    
    cookies = {
        "Hm_lvt_f32803886966beff8fa513f7a33dea1e": "1757212522",
        "__jsluid_s": "111aefa2d58433cc4db4b677678ea4de",
        "SUNWAY-ESCM-COOKIE": "9f25150b-8d00-4acf-b2eb-6d0c32b354aa",
        "JSESSIONID": "66D3CE73FD2120232CCA12C4DE0B4A5B"
    }
    
    url = "https://ec.minmetals.com.cn/open/homepage/public"
    
    try:
        response = requests.post(url, headers=headers, cookies=cookies, timeout=10)
        
        if response.status_code == 200:
            # 检查响应内容是否为JSON
            content_type = response.headers.get('content-type', '')
            if 'application/json' in content_type:
                return response.text
            else:
                print(f"公共数据接口返回的不是JSON格式，内容类型: {content_type}")
                print(f"响应内容前200字符: {response.text[:200]}")
                return None
        else:
            print(f"获取公共数据失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:500]}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"请求公共数据时发生网络错误: {e}")
        return None

def fetch_purchase_data(page_num=1):
    """获取采购信息数据"""
    # 先获取公共数据
    print("正在获取公共数据...")
    public_data = fetch_public_data()
    if not public_data:
        print("获取公共数据失败，无法继续")
        return None
    
    print(f"成功获取公共数据!")

    ctx = create_js_environment()

    # 使用JavaScript加密参数
    print("正在加密参数...")
    try:
        enc_param = ctx.call("getParam", page_num, public_data)
        print(f"加密成功!")
    except Exception as e:
        print(f"加密参数时出错: {e}")
        return None
    
    # 请求头
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ar;q=0.5",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Origin": "https://ec.minmetals.com.cn",
        "Pragma": "no-cache",
        "Referer": "https://ec.minmetals.com.cn/open/home/purchase-info",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"140\", \"Chromium\";v=\"140\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\""
    }
    
    # Cookies - 可能需要更新这些cookie
    cookies = {
        "Hm_lvt_f32803886966beff8fa513f7a33dea1e": str(int(time.time())),
        "__jsluid_s": "111aefa2d58433cc4db4b677678ea4de",
        "SUNWAY-ESCM-COOKIE": "9f25150b-8d00-4acf-b2eb-6d0c32b354aa",
        "JSESSIONID": "66D3CE73FD2120232CCA12C4DE0B4A5B"
    }
    
    # 请求URL和数据
    url = "https://ec.minmetals.com.cn/open/homepage/zbs/by-lx-page"
    data = {
        "param": enc_param
    }
    
    # 发送请求
    print("正在发送采购数据请求...")
    try:
        response = requests.post(url, headers=headers, cookies=cookies, json=data, timeout=15)
        
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        
        # 检查响应内容
        if response.status_code == 200:
            # 先检查是否是JSON
            content_type = response.headers.get('content-type', '')
            if 'application/json' in content_type:
                try:
                    response_data = response.json()
                    print("成功解析JSON响应")
                    return response_data
                except json.JSONDecodeError as e:
                    print(f"JSON解析错误: {e}")
                    print(f"响应内容前500字符: {response.text[:500]}")
                    return None
            else:
                print("响应不是JSON格式，可能是HTML页面")
                print(f"响应内容: {response.text}")
                
                # 检查是否是重定向或验证页面
                if "<html" in response.text.lower() or "<!doctype" in response.text.lower():
                    print("检测到HTML页面，可能是验证或重定向")
                    # 可以尝试保存HTML内容进行调试
                    with open('debug_response.html', 'w', encoding='utf-8') as f:
                        f.write(response.text)
                    print("已将响应内容保存到 debug_response.html 文件")
                
                return None
        else:
            print(f"请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text[:500]}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"请求采购数据时发生网络错误: {e}")
        return None

def main():
    """主函数"""
    print("开始获取五矿采购数据...")
    
    # 获取采购数据（默认第一页）
    purchase_data = fetch_purchase_data(page_num=1)
    
    if purchase_data:
        print("\n获取数据成功！")
        
        # 这里可以添加数据处理逻辑
        if purchase_data.get("success"):
            print("请求成功")
            # 提取需要的数据
            data_list = purchase_data.get("data", {}).get("list", [])
            print(f"共获取到 {len(data_list)} 条采购信息")
            
            # 简单展示几条数据
            for i, item in enumerate(data_list[:3]):  # 只显示前3条
                print(f"\n第 {i+1} 条采购信息:")
                print(f"标题: {item.get('title', '无')}")
                print(f"发布时间: {item.get('publishDate', '无')}")
                print(f"采购编号: {item.get('purchaseCode', '无')}")
        else:
            print(f"请求失败: {purchase_data.get('message', '未知错误')}")
            print(f"完整响应: {json.dumps(purchase_data, ensure_ascii=False, indent=2)}")
    else:
        print("获取数据失败！")
        
    print("\n程序执行完毕")

if __name__ == "__main__":
    main()