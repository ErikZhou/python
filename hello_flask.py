from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Flask!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):   # 函数参数中接收传递的参数
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/loginto')
def login():
    print(url_for('login'))   # 会打印出网址中主机名后的部分
    return 'Hello world!'



if __name__ == '__main__':
    app.run(debug=True)      # 设置debug=True是为了让代码修改实时生效，而不用每次重启加载

