from __future__ import unicode_literals
import os
from flask import Flask, request, abort, send_file
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

from linebot.models.send_messages import ImageSendMessage
import PhotoCombine
from random import randrange

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@app.route("/image")
def image():
    return send_file("out_put_photo/result.jpg")

@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    mtext = event.message.text

    if mtext == "@photo" :
        try:
            PhotoCombine.generatePhoto()
            path = "YourWebSite" +"/image?r=" + str(randrange(100000))
            #print(path)
            message = ImageSendMessage(original_content_url = path,preview_image_url = path)
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="文青文想不出來啊呀!!!!")) 

if __name__ == "__main__":
    app.run()

    
