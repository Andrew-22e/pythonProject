# 导入自动化模块
from DrissionPage import ChromiumPage
from DrissionPage.common import Keys
import csv
import re
import time

# 实例化浏览器对象
dp = ChromiumPage()
# 访问京东首页
dp.get("https://www.jd.com")
# ele提取单个元素，eles提取多个元素,    #对应ID   .对应class
# 获取搜索框元素并且输入关键字
str = input("请输入商品名称：")
dp.ele("css:#key").input(str)
# 模拟回车键
dp.ele("css:#key").input(Keys.ENTER)
# 延时,确保数据完全加载出来
time.sleep(2)
# 模拟页面下滑到底部，刷新剩余的30条商品信息
dp.scroll.to_bottom()
# 延时,确保数据完全加载出来
time.sleep(2)
# 元素定位获取商品信息
list = dp.eles("css:._info_2xp6d_44")

# 创建商品列表
products = []

# for循环遍历商品信息
for i in list:
    # 获取商品名称
    name = i.ele("css:._text_1x4i2_30").text
    # 获取商品价格
    price_text = i.ele("css:._price_1tn4o_13").text
    # 获取商品评价数量
    comment = i.ele("css:._goods_volume_1xkku_1").text
    # 获取商品店铺名称
    shop = i.ele("css:._name_d19t5_35").text
    
      # 清理价格数据，使用正则表达式提取数字和小数点
    price_match = re.search(r'[\d.]+', price_text)
    if price_match:
        try:
            price_num = float(price_match.group())
        except ValueError:
            price_num = 0.0
    else:
        price_num = 0.0
    
    # 将商品信息添加到列表
    products.append({
        'name': name,
        'price': price_num,
        'price_text': price_text,
        'comment': comment,
        'shop': shop
    })
    
    # 打印信息
    print("标题：", name, "价格：", price_text, "评价数量：", comment, "店铺名称：", shop)
exit()
# 按价格排序（从低到高）
products.sort(key=lambda x: x['price'])

# 将排序后的数据写入CSV文件
with open(f'爬虫\文本\京东商品数据.csv', 'w', newline='', encoding='utf-8-sig') as csvfile:
    fieldnames = ['name', 'price_text', 'comment', 'shop']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # 写入表头
    writer.writeheader()
    
    # 写入数据
    for product in products:
        writer.writerow({
            'name': product['name'],
            'price_text': product['price_text'],
            'comment': product['comment'],
            'shop': product['shop']
        })

print(f"\n已将{len(products)}个商品按价格排序并保存到文件中")
# 如果要获取下一页的商品数据，将上面的延时以后的代码放到for循环中，并且在最后面加一个自动点击下一页的代码dp.ele("css:.pn-next").click