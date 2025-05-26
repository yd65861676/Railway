from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 配置密钥（在生产环境中应使用环境变量）
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-dev-key')

@app.route('/')
def home():
    """首页路由"""
    return render_template('index.html', title='数字艺术市场')

@app.route('/about')
def about():
    """关于页面路由"""
    return render_template('about.html', title='关于我们')

@app.route('/gallery')
def gallery():
    """艺术品展示页面"""
    # 这里可以从数据库获取艺术品列表
    artworks = [
        {'id': 1, 'title': '星空', 'artist': '艺术家A', 'image': 'img/artwork1.jpg'},
        {'id': 2, 'title': '海洋', 'artist': '艺术家B', 'image': 'img/artwork2.jpg'},
        {'id': 3, 'title': '山脉', 'artist': '艺术家C', 'image': 'img/artwork3.jpg'}
    ]
    return render_template('gallery.html', title='艺术品展示', artworks=artworks)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """联系页面路由"""
    if request.method == 'POST':
        # 处理表单提交
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # 这里可以添加发送邮件或保存到数据库的逻辑
        
        return redirect(url_for('thank_you'))
    
    return render_template('contact.html', title='联系我们')

@app.route('/thank-you')
def thank_you():
    """表单提交后的感谢页面"""
    return render_template('thank_you.html', title='谢谢您的留言')

# 错误处理路由
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='页面未找到'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html', title='服务器错误'), 500

if __name__ == '__main__':
    # 本地开发时使用
    app.run(debug=True)
