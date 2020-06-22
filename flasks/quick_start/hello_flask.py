from flask import Flask
from flask import escape
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

# 路由
@app.route('/')
def index():
    return "Index Page."

@app.route("/hello/")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


# 变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    return "User is {}".format(escape(username))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

# 唯一的 URL / 重定向行为
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


# URL构建
with app.test_request_context():
    print(url_for('index'))
    print(url_for('hello'))
    print(url_for('hello', next='/'))
    print(url_for('show_user_profile', username="crisimple"))


if __name__ == "__main__":
    app.run(debug=True)