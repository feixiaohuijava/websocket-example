# coding:utf-8
from django.http import HttpResponse
from channels.handler import AsgiHandler
import time
#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端

#一个管道大概会持续30s


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)

#当连接上时，发回去一个connect字符串
def ws_connect(message):
    message.reply_channel.send({"text":"it connected!"})
    # lol_list = ['ali','aixi','huangzi','timo']
    # for item in lol_list:
    #     message.reply_channel.send({"text":item})
    #     time.sleep(1)

#将发来的信息原样返回
def ws_message(message):
    print message["text"]
    lol_list = ['ali','aixi','huangzi','timo']
    for item in lol_list:
        message.reply_channel.send({"text":item})
        time.sleep(2)
    # message.reply_channel.send({
    #     "text": "webserver response",
    # })
#断开连接时发送一个disconnect字符串，当然，他已经收不到了
def ws_disconnect(message):
    message.reply_channel.send({"disconnect":"disconnect"})