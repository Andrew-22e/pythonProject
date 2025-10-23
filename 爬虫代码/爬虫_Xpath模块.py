from lxml import etree

# Extra content at the end of the document表明在XML文档的末尾存在额外的、不符合 XML 格式规范的内容
# 多个根元素：XML 文档只能有一个根元素，若文档里存在多个顶级元素，就会产生此错误。
# 多余的字符：在 XML 文档结束标签之后不能有多余的字符，像空格、换行符、非 XML 文本等。
# 未闭合的标签：XML 标签必须正确闭合，若有未闭合的标签，解析器会认为文档结构不完整，进而报错。

# text()方法返回节点的文本内容
# // 表示后代节点
# / 表示当前节点的子节点
# * 表示任意节点
# s = """
# <books>
#     <book>
#         <title>Python Crash Course</title>
#             <author>Matthes</author>
#         <author>Eric Matthes</author>
#         <year>2015</year>
#     </book>
#     <book>
#         <title>Clean Code</title>
#         <author>Robert C. Martin</author>
#         <year>2008</year>
#     </book>
# </books>
# """
# tree = etree.XML(s)
# result = tree.xpath("/books/book/title/text()")
# for i in result:
#     print(i)

#######################################################
# 1. 返回元素节点列表
# 当 XPath 表达式匹配到一个或多个元素节点时，xpath方法会返回一个包含这些元素节点的列表。每个元素节点是一个lxml.etree._Element对象，你可以对这些对象继续使用xpath方法进行进一步的节点查找，也能获取其属性或文本内容。
# 示例代码：
html = """
<html>
    <body>
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
    </body>
</html>
"""
tree = etree.HTML(html)
divs = tree.xpath('//div[@class="item"]')
for div in divs:
    print(type(div))
    print(div.text)
#在这个例子中，xpath('//div[@class="item"]')匹配到了所有class属性为item的div元素，返回一个包含这些div元素节点的列表。通过遍历列表，我们可以访问每个元素的文本内容。

# 2. 返回文本节点列表
# 若 XPath 表达式使用了text()函数，xpath方法会返回一个包含匹配到的文本节点内容的列表。
# 示例代码：
html = """
<html>
    <body>
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
    </body>
</html>
"""
tree = etree.HTML(html)
texts = tree.xpath('//div[@class="item"]/text()')
for text in texts:
    print(text)
#这里，xpath('//div[@class="item"]/text()')直接获取了所有class属性为item的div元素的文本内容，返回一个包含这些文本的列表。

# 3. 返回属性值列表
# 当 XPath 表达式用于获取元素的属性值时，xpath方法会返回一个包含这些属性值的列表。
# 示例代码：
html = """
<html>
    <body>
        <div class="item" id="item1">Item 1</div>
        <div class="item" id="item2">Item 2</div>
    </body>
</html>
"""
tree = etree.HTML(html)
ids = tree.xpath('//div[@class="item"]/@id')
for id in ids:
    print(id)
#在这个例子中，xpath('//div[@class="item"]/@id')获取了所有class属性为item的div元素的id属性值，返回一个包含这些属性值的列表。

# 4. 返回空列表
# 如果 XPath 表达式没有匹配到任何节点，xpath方法会返回一个空列表。
# 示例代码：
html = """
<html>
    <body>
        <div class="item">Item 1</div>
        <div class="item">Item 2</div>
    </body>
</html>
"""
tree = etree.HTML(html)
result = tree.xpath('//span')
print(result)
#由于 HTML 文档中没有span元素，xpath('//span')返回一个空列表。

# 5. 返回单个节点或值
# 在某些情况下，XPath 表达式可能只匹配到一个节点或一个值，此时xpath方法仍然会返回一个包含该节点或值的列表。若要获取单个元素，可以通过索引访问列表中的第一个元素。
# 示例代码：
html = """
<html>
    <body>
        <div class="unique">Unique Item</div>
    </body>
</html>
"""
tree = etree.HTML(html)
unique_div = tree.xpath('//div[@class="unique"]')
if unique_div:
    print(unique_div[0].text)
#这里，xpath('//div[@class="unique"]')匹配到一个div元素，返回一个包含该元素的列表，通过unique_div[0]可以访问该元素。