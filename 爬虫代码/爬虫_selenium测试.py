from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import urllib3
import logging

# 文件配置地址
path = "D:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"
# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 添加这行代码来减少selenium的日志输出
logging.getLogger('selenium').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

# 设置 Edge 无头模式
edge_options = Options()
edge_options.add_argument("--headless")  # 启用无头模式

# 创建 WebDriver 实例
driver = webdriver.Edge(service=Service(path), options=edge_options)

# 打开网页
driver.get("https://www.baidu.com")

# 打印网页标题
print(driver.title)

# 关闭浏览器
driver.quit()