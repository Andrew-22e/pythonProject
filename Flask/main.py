from flask import Flask, render_template_string, request

# 创建Flask应用实例
app = Flask(__name__)

# 简单的HTML模板
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .nav { margin-bottom: 20px; padding-bottom: 10px; border-bottom: 1px solid #ddd; }
        .nav a { margin-right: 15px; text-decoration: none; color: #333; }
        .nav a:hover { color: #007bff; }
        .content { margin: 20px 0; }
        form { margin: 20px 0; }
        input { padding: 8px; margin: 5px 0; width: 100%; max-width: 300px; }
        button { padding: 8px 15px; background-color: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <div class="nav">
        <a href="/">首页</a>
        <a href="/about">关于</a>
        <a href="/greet">问候</a>
    </div>
    <h1>{{ heading }}</h1>
    <div class="content">
        {{ content }}
    </div>
    {% if show_form %}
    <form method="post">
        <input type="text" name="name" placeholder="请输入你的名字" required>
        <button type="submit">提交</button>
    </form>
    {% endif %}
</body>
</html>
'''

# 首页路由
@app.route('/')
def home():
    return render_template_string(
        HTML_TEMPLATE,
        title="首页",
        heading="欢迎来到我的网站",
        content="这是一个使用Flask框架创建的简单网站示例。",
        show_form=False
    )

# 关于页面路由
@app.route('/about')
def about():
    return render_template_string(
        HTML_TEMPLATE,
        title="关于",
        heading="关于我们",
        content="这个网站展示了Flask的基本用法，包括路由、模板和表单处理。",
        show_form=False
    )

# 问候页面路由，支持GET和POST方法
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        # 获取表单提交的名字
        name = request.form.get('name', '访客')
        return render_template_string(
            HTML_TEMPLATE,
            title="问候",
            heading=f"你好，{name}！",
            content="很高兴见到你！",
            show_form=True
        )
    else:
        # GET请求，显示表单
        return render_template_string(
            HTML_TEMPLATE,
            title="问候",
            heading="请告诉我:你的名字",
            content="输入你的名字，我会向你问好。",
            show_form=True
        )

# 动态路由示例
@app.route('/user/<username>')
def user_profile(username):
    return render_template_string(
        HTML_TEMPLATE,
        title=f"{username}的个人资料",
        heading=f"{username}的个人资料",
        content=f"这是用户 {username} 的个人资料页面。",
        show_form=False
    )

# 启动应用
if __name__ == '__main__':
    app.run(debug=True)
