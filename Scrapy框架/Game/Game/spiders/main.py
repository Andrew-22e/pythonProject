import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["4399.com"]
    start_urls = ["https://4399.com/flash/"]

    def parse(self, response):
        print(response)
        # 获取所有游戏名字
        for name in response.xpath("//ul[@class='n-game cf']/li"):
            text = name.xpath("./a/b/text()").extract_first()
            print(text)
