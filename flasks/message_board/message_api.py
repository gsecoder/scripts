#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   message_api.py
@Time    :   2020/4/1321:05
@Author  :   jiangheng
@Description    :   None
"""
from message_models import app
from message_models import db
from message_models import Admin
from message_models import Tag
from message_models import User
from message_models import Message

from flask import jsonify
from flask import request
from flask import session

"""
    状态码 200 成功
    状态码 400 失败
"""

@app.route('/')
@app.route('/index')
def hello_flask():
    return "Hello Flask"

# 管理员初始化
@app.route('/init/admin')
def init_admin():
    """
    账号：admin
    密码：default
    :return:
    """
    admin = Admin(username="crisimple", password="123456")
    try:
        db.session.add(admin)
        db.session.commit()
        return jsonify(code=200, msg="初始化管理员成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="初始化管理员失败")

# 管理员登录
@app.route('/admin/login', methods=["POST"])
def login_admin():
    """
    账号
    :return:
    """
    req_data = request.get_json()
    username = req_data.get("username")
    password = req_data.get("password")
    if not all([username, password]):
        return jsonify(code=400, msg="参数不完整")

    # 查找数据库管理员
    admin = Admin.query.filter(Admin.username == username).first()
    if admin is None or password !=admin.password:
        return jsonify(code=400, msg="账号或密码错误")
    session["admin_name"] = username
    session["admin_id"] = admin.id
    return jsonify(code=200, msg="登录成功")

# 检查管理员登录状态
@app.route('/admin/session', methods=['GET'])
def check_admin_session():
    username = session.get("admin_name")
    admin_id = session.get("admin_id")

    if username is not None:
        return jsonify(username=username, admin_id=admin_id)
    else:
        return jsonify(msg="出错了，你还没登录")

# 管理员退出登录
@app.route('/admin/logout')
def logout_admin():
    session.clear()
    return jsonify(msg="退出登录")

# 管理员增标签
@app.route('/admin/tag', methods=["POST"])
def add_tag():
    """
    tag_name
    :return:
    """
    req_data = request.get_json()
    tag_name = req_data.get("tag_name")     # 获取标签名
    admin_id = session.get("admin_id")      # 获取管理员的id

    if not all([tag_name, admin_id]):
        return jsonify(code=400, msg="参数不完整或未登录")

    tag = Tag(name=tag_name, admin_id=admin_id)
    try:
        db.session.add(tag)
        db.session.commit()
        return jsonify(code=200, msg="添加标签成功")
    except Exception as e:
        print(e)
        return jsonify(code=400, msg="添加标签失败")

# 管理员删标签
@app.route('/admin/tag', methods=["DELETE"])
def delete_tag():
    req_data = request.get_json()
    tag_name = req_data.get("tag_name")     # 获取标签名
    admin_id = session.get("admin_id")      # 获取管理员的id

    if not all([tag_name, admin_id]):
        return jsonify(code=400, msg="参数不完整或未登录")

    try:
        tag = Tag.query.filter(Tag.name == tag_name).delete()
        db.session.commit()
        return jsonify(code=200, msg="删除标签成功")
    except Exception as e:
        print(e)
        return jsonify(code=400, msg="删除标签失败")

# 管理员删留言
@app.route('/admin/message', methods=["DELETE"])
def admin_delete_message():
    req_data = reuqest.get_json()
    message_id = req_data.get("message_id")
    admin_id = req_data.get("admin_id")
    if not all([message_id, admin_id]):
        return jsonify(code=400, msg="参数不完整")
    # 判断留言是否存在
    msg = Message.query.get(id)
    if msg is None:
        return jsonify(code=400, msg="留言不存在，无法进行删除")
    # 判断留言是否是作者
    if user_id != msg.admin.id:
        return jsonify(code=400, msg="你不是作者，无法删除操作")
    try:
        m = Message.query.filter(Message.id == message_id).delete()
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")


# 用户初注册
@app.route('/user/register', methods=["POST"])
def user_register():
    """
    账号：
    密码：
    :return:
    """
    req_data = request.get_json()
    username = req_data.get("username")
    password = req_data.get("password")

    user = User(username=username, password=password)
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg="注册用户成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="注册用户失败")

# 用户登录
@app.route('/user/login', methods=["POST"])
def user_login():
    """
    账号
    :return:
    """
    req_data = request.get_json()
    username = req_data.get("username")
    password = req_data.get("password")
    if not all([username, password]):
        return jsonify(code=400, msg="参数不完整")

    # 查找数据库管理员
    user = User.query.filter(User.username == username).first()
    if user is None or password !=user.password:
        return jsonify(code=400, msg="账号或密码错误")
    session["user_name"] = username
    session["user_id"] = user.id
    return jsonify(code=200, msg="登录成功")

# 检查用户登录状态
@app.route('/user/session', methods=['GET'])
def check_user_session():
    username = session.get("user_name")
    user_id = session.get("user_id")

    if username is not None:
        return jsonify(username=username, user_id=user_id)
    else:
        return jsonify(msg="出错了，你还没登录")

# 用户退出登录
@app.route('/user/logout')
def user_logout():
    session.clear()
    return jsonify(msg="用户退出成功")

# 用户发布留言
@app.route('/user/message', methods=["POST"])
def user_post_message():
    req_data = request.get_json()
    user_id = req_data.get("user_id")
    tags = req_data.get("tags")
    content = req_data.get("content")
    if not all([user_id, tags, content]):
        return jsonify(code=400, msg="参数不完整")
    try:
        tags = Tag.query.filter(Tag.name.in_(tas)).all()
        message = Message(content=content, user_id=user_id)
        message.tags = tags
        db.session.add(message)
        db.session.commit()
        return jsonify(code=200, msg="发布留言成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="发布留言失败")

# 用户删除留言
@app.route('/user/message', methods=["DELETE"])
def user_delete_message():
    """
    留言对应的id
    发布者的user_id
    :return:
    """
    req_data = reuqest.get_json()
    message_id = req_data.get("message_id")
    user_id = req_data.get("user_id")
    if not all([message_id, user_id]):
        return jsonify(code=400, msg="参数不完整")
    # 判断留言是否存在
    msg = Message.query.get(message_id)
    if msg is None:
        return jsonify(code=400, msg="留言不存在，无法进行删除")
    # 判断留言是否是作者
    if user_id != msg.user.id:
        return jsonify(code=400, msg="你不是作者，无法删除操作")
    try:
        m = Message.query.filter(Message.id == message_id).delete()
        db.session.commit()
        return jsonify(code=200, msg="删除成功")
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="删除失败")

# 用户查看留言记录
@app.route('/user/message/history', methods=["GET"])
def user_message_history():
    user_id = session.get("user_id")
    if user_id is None:
        return jsonify(code=400, msg="请登录")

    user = User.query.get(user_id)
    if user is None:
        return jsonify(code=400, msg="用户不存在")

    # 获取留言
    payload = []
    messages = user.tags
    for message in messages:
        content = message.content
        tags = message.messages
        tags_name = []
        for tag in tags:
            for t in tag:
                tags_name.append(t.name)
        create_time = message.create_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = message.user_id
        data = {
            "content": content,
            "message_id": message_id,
            "tags": tags_name,
            "create_time": create_time,
            "user_id": user_id
        }
        payload.append(data)
    return jsonify(code=200, msg="查询成功", data=payload)

# 获取留言区留言
@app.route('/user/message/board', methods=["GET"])
def user_messages_board():
    messages = Message.query.all()
    payload = []
    for message in messages:
        content = message.content
        tags = message.messages
    tags_name = []
    for tag in tags:
        for t in tag:
            tags_name.append(t.name)
        create_time = message.create_time.strftime("%Y-%m-%d %H:%M:%S")
        user_id = message.user_id
        data = {
            "content": content,
            "message_id": message_id,
            "tags": tags_name,
            "create_time": create_time,
            "user_id": user_id
        }
        payload.append(data)
    return jsonify(code=200, msg="查询成功", data=payload)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="500")