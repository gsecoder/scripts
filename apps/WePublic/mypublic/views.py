from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import hashlib
from . import receive
from . import reply


# Create your views here.
# django默认开启了csrf防护，@csrf_exempt是去掉防护
# 微信服务器进行参数交互，主要是和微信服务器进行身份的验证
@csrf_exempt
def check_signature(request):
    if request.method == "GET":
        print("request: ", request)
        # 接受微信服务器get请求发过来的参数
        # 将参数list中排序合成字符串，再用sha1加密得到新的字符串与微信发过来的signature对比，如果相同就返回echostr给服务器，校验通过
        # ISSUES: TypeError: '<' not supported between instances of 'NoneType' and 'str'
        # 解决方法：当获取的参数值为空是传空，而不是传None
        signature = request.GET.get('signature', '')
        timestamp = request.GET.get('timestamp', '')
        nonce = request.GET.get('nonce', '')
        echostr = request.GET.get('echostr', '')
        # 微信公众号处配置的token
        token = str("Txy159wx")

        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        print("[token, timestamp, nonce]: ", hashlist)

        hashstr = ''.join([s for s in hashlist]).encode('utf-8')
        print('hashstr before sha1: ', hashstr)

        hashstr = hashlib.sha1(hashstr).hexdigest()
        print('hashstr sha1: ', hashstr)

        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin index")
    elif request.method == "POST":
        otherContent = autoreply(request)
        return HttpResponse(otherContent)
    else:
        print("你的方法不正确....")


def autoreply(request):
    try:
        webData = request.body
        print("Handle POST webData is: ", webData)

        recMsg = receive.parse_xml(webData)
        if isinstance(recMsg, receive.Msg):
            toUser = recMsg.FromUserName
            fromUser = recMsg.ToUserName
            if recMsg.MsgType == 'text':
                content = recMsg.Content.decode('utf-8')
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            if recMsg.MsgType == 'image':
                # Issues1: 'ImageMsg' object has no attribute 'MeidaId'
                # Issues2: 发送图片返回了：qCs1WNDj5p9-FULnsVoNoAIeKQUfLsamrfuXn-Goo32RwoDT8wkhh3QGNjZT0D5a
                # Issues3: 'str' object has no attribute 'decode'
                # Issues4: '该公众号提供的服务出现故障，请稍后再试' --- xml格式写错了
                mediaId = recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            if recMsg.MsgType == 'voice':
                mediaId = recMsg.MediaId
                replyMsg = reply.VoiceMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            if recMsg.MsgType == 'video':
                mediaId = recMsg.MediaId
                # Issues5: 'VideoMsg' object has no attribute 'MediaId' ----- VideoMsg错写成了VoiceMsg
                # Issues51: 'VideoMsg' object has no attribute 'MediaId' -----
                replyMsg = reply.VideoMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            if recMsg.MsgType == 'shortvideo':
                mediaId = recMsg.MediaId
                replyMsg = reply.ShortVideoMsg(toUser, fromUser, mediaId)
                return replyMsg.send()
            else:
                return reply.Msg().send()
        else:
            print("暂不处理")
            return reply.Msg().send()
    except Exception as e:
        print(e)

