# 命令行对新手实在是不太友好，因此我决定效仿各种开源工具，使用web服务器，提供网页图形操作界面
# 使用http 进行前后端通讯
from flask import Flask ,render_template
app = Flask(__name__)

app.config['STATIC_FOLDER'] = 'static'
app.config['STATIC_URL_PATH'] = '/'

@app.route('/')
def sd():
    # 将html 文件发送过去
    return app.send_static_file('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World'
app.run()