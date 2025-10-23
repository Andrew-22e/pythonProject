import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup
from webdriver_manager.firefox import GeckoDriverManager

def download_image(url, save_path):
    """
    url (str): 图片的URL地址。
    save_path (str): 图片保存的本地路径。
    """
    try:
        # 发起GET请求，流式获取数据
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # 打开文件，准备写入
        with open(save_path, 'wb') as file:
            # 迭代响应数据，分块写入文件
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
        # 打印成功消息
        print(f"图片 {url} 下载成功，保存至 {save_path}")
    except requests.RequestException as e:
        # 打印错误消息
        print(f"下载图片 {url} 时出错: {e}")

def get_images_from_page(driver):
    """
    从给定的页面中提取所有图片的URL。
    参数:
    - driver: 页面的webdriver对象，用于获取页面源代码。
    返回:
    - image_urls: 包含所有图片URL的列表。
    """
    # 获取页面源代码
    page_source = driver.page_source
    # 使用BeautifulSoup解析页面源代码
    soup = BeautifulSoup(page_source, 'html.parser')
    # 找到页面中所有的<img>标签
    img_tags = soup.find_all('img')
    # 初始化图片URL列表
    image_urls = []
    # 遍历所有<img>标签
    for img in img_tags:
        # 获取<img>标签的src属性
        src = img.get('src')
        # 检查src属性是否存在
        if src:
            # 如果src属性不是完整的URL，构建完整的URL
            if not src.startswith('http'):
                # 获取当前页面的基URL
                base_url = driver.current_url.rsplit('/', 1)[0]
                # 拼接成完整的图片URL
                src = f"{base_url}/{src}"
            # 将完整的图片URL添加到列表中
            image_urls.append(src)
    # 返回所有图片的URL列表
    return image_urls


def main():
    """
    主函数，用于控制网页爬取和图片下载的整个流程。
    """
    # 设置Firefox WebDriver服务
    service = Service(GeckoDriverManager().install())
    # 初始化Firefox WebDriver
    driver = webdriver.Firefox(service=service)

    try:
        # 目标网站URL
        url = 'https://unsplash.com/'  # 请替换为你要爬取的网站 URL
        # 访问目标网站
        driver.get(url)

        # 从网页中获取所有图片的URL
        image_urls = get_images_from_page(driver)

        # 定义图片保存的文件夹
        save_folder = 'downloaded_images'
        # 如果保存文件夹不存在，则创建
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        # 设置最多下载的图片数量
        max_images = 8
        # 遍历图片URL，下载并保存图片
        for i, image_url in enumerate(image_urls[:max_images]):
            # 拼接图片保存路径
            file_name = os.path.join(save_folder, f'image_{i}.jpg')
            # 下载图片并保存
            download_image(image_url, file_name)

    except Exception as e:
        # 捕获并打印错误信息
        print(f"发生错误: {e}")
    finally:
        # 无论是否发生错误，都关闭WebDriver
        driver.quit()


if __name__ == "__main__":
    main()