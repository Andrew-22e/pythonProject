import requests
import parsel
import time

class WeatherCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        }
        self.base_url = 'https://www.tianqi.com/{}/'
        self.weekly_url = 'https://www.tianqi.com/{}/7/'
    
    def get_weather(self, city):
        """
        获取单个城市当前天气信息
        :param city: 城市名称(拼音)
        :return: 天气信息字典
        """
        url = self.base_url.format(city)
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            html = response.text
            
            # 解析数据
            selector = parsel.Selector(html)
            
            # 提取各个信息
            name = selector.css('.name h1::text').get()
            week = selector.css('.week::text').get()
            
            # 提取天气状况和温度
            weather_condition = selector.css('.weather span b::text').get()  # 天气状况，如"阴"
            weather_temperature = selector.css('.weather span::text').getall()  # 温度信息
            
            # 处理温度信息
            temperature = ""
            if weather_temperature:
                # 过滤掉空字符串并连接温度信息
                temp_texts = [text.strip() for text in weather_temperature if text.strip()]
                temperature = " ".join(temp_texts)
            
            # 组合天气信息
            if weather_condition and temperature:
                weather = f"{weather_condition} {temperature}"
            elif weather_condition:
                weather = weather_condition
            elif temperature:
                weather = temperature
            else:
                weather = None
                
            shidu_items = selector.css('.shidu b::text').getall()
            shidu = ' '.join(shidu_items) if shidu_items else None
            kongqi = selector.css('.kongqi h5::text').get()
            
            return {
                'city': name,
                'date': week,
                'weather_condition': weather_condition,  # 天气状况
                'temperature': temperature,  # 温度
                'weather': weather,  # 完整天气信息
                'humidity': shidu,
                'air_quality': kongqi
            }
        except Exception as e:
            print(f"获取{city}天气信息失败: {e}")
            return None
    
    def get_weekly_weather(self, city):
        """
        获取单个城市未来一周天气信息
        :param city: 城市名称(拼音)
        :return: 未来一周天气信息列表
        """
        url = self.weekly_url.format(city)
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            html = response.text
            # 解析数据
            selector = parsel.Selector(html)
            
            # 获取城市名称
            city_name = selector.css('.weaone_b a h1::text').get()
            
            # 提取一周天气列表
            weekly_forecast = []
            
            # 查找天气列表项 - 根据提供的HTML结构调整选择器
            weather_items = selector.css('.weaul li')
            
            for item in weather_items:
                # 日期信息（例如：08-09）
                date = item.css('.weaul_q .fl::text').get()
                
                # 星期信息（例如：今天、明天、后天、星期X）
                day_of_week = item.css('.weaul_q .fr::text').get()
                
                # 天气状况（例如：阴、小雨转中雨）
                weather_condition = item.css('.weaul_z::text').get()
                
                # 温度范围（例如：30~37℃）
                temp_elements = item.css('.weaul_z span::text').getall()
                if len(temp_elements) >= 2:
                    temperature = f"{temp_elements[0]}~{temp_elements[1]}℃"
                else:
                    temperature = item.css('.weaul_z:last-child::text').get()
                
                # 构建单日天气信息
                day_weather = {
                    'date': f"{date} ({day_of_week})" if date and day_of_week else (date or day_of_week),
                    'condition': weather_condition,
                    'temperature': temperature
                }
                
                # 只添加有效数据
                if any(day_weather.values()):
                    weekly_forecast.append(day_weather)
            
            return {
                'city': city_name,
                'weekly_forecast': weekly_forecast
            }
            
        except Exception as e:
            print(f"获取{city}未来一周天气信息失败: {e}")
            return None
    
    def get_multiple_weather(self, cities, delay=1):
        """
        批量获取多个城市天气信息
        :param cities: 城市名称列表
        :param delay: 请求间隔时间(秒)
        :return: 天气信息列表
        """
        results = []
        for city in cities:
            # print(f"正在获取 {city} 的天气信息...")
            weather_info = self.get_weather(city)
            if weather_info:
                results.append(weather_info)
                print(f"{city}: {weather_info['weather']}")
            else:
                print(f"未能获取 {city} 的天气信息")
            
            # 添加延时，避免请求过于频繁
            time.sleep(delay)
        
        return results

# 使用示例
if __name__ == "__main__":
    # 创建天气爬虫实例
    crawler = WeatherCrawler()
    
    # 可以批量查询城市列表(需要使用城市拼音)
    cities = [
            'ningdu', 
            # 'fuliang',
            # 'ganzhou',
            # 'nanchang'
              ]
    
    # 获取当前天气信息
    weather_data = crawler.get_multiple_weather(cities, delay=1)
    
    # 打印当前天气结果
    print("\n=== 当前天气信息汇总 ===")
    for data in weather_data:
        print(f"城市: {data['city']}")
        print(f"日期: {data['date']}")
        print(f"天气状况: {data['weather_condition']}")
        print(f"温度: {data['temperature']}")
        print(f"{data['humidity']}")
        print(f"{data['air_quality']}")
        print("-" * 50)
    
    # 获取未来一周天气信息
    print("\n=== 未来一周天气预报 ===")
    for city in cities:
        weekly_data = crawler.get_weekly_weather(city)
        if weekly_data:
            xx = weekly_data['city'].split()
            print(f"地区-{' '.join(xx)}:")
            for day_weather in weekly_data['weekly_forecast']:
                print(f"  日期: {day_weather['date']}")
                print(f"  天气: {day_weather['condition']}")
                print(f"  温度: {day_weather['temperature']}")
                print("  " + "-" * 20)
        else:
            print(f"未能获取 {city} 的未来一周天气信息")