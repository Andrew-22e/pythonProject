import re

# findall()方法: 返回一个列表，列表中的元素是所有匹配成功的字符串
lst = re.findall(r"\d+","我的电话是:10086，我number是:10010")
print(lst)

# finditer()方法: 返回一个迭代器，迭代器中的元素是所有匹配成功的字符串
lst = re.finditer(r"\d+","我的电话是:10086，我number是:10010")
for i in lst:
    print(i.group())

# search()方法: 全文匹配，返回一个匹配对象，如果匹配成功，则返回匹配对象，否则返回None
lst = re.search(r"\d+","我的电话是:10086，我number是:10010")
print(lst.group())

# match()方法: 从头匹配，返回一个匹配对象，如果匹配成功，则返回匹配对象，否则返回None
lst = re.match(r"\d+","10086，我number是:10010")
print(lst.group())

# 预加载正则表达式，提高效率，可重复使用
lst = re.compile(r"\d+",re.S)  # re.s：表示.能够匹配字符串中的换行符
res = lst.finditer("我的电话是:10086，我number是:10010")
for i in res:
    print(i.group())

# eg
s = """
<div class='jay'><span id='1'>王者荣耀</span></div>
<div class='jia'><span id='2'>英雄联盟</span></div>
<div class='jjf'><span id='3'>和平精英</span></div>
<div class='jff'><span id='4'>穿越火线</span></div>
<div class='jdf'><span id='5'>Counter-Strike</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id='(?P<ID>\d+)'>(?P<Game>.*?)</span></div>",re.S)
result = obj.finditer(s)
for i in result:
    print(i.group("ID"))
    print(i.group("Game"))