# Maybe_Hipster_lineBot

## Itoduction
有時候感覺自己生活不夠文青，看著別人在不同社交平合貼了一些你看不懂的文章，相比之下自己甚麼文章都沒有，不然就是貼的文章不夠深奧。
每天不知道自己要貼甚麼好是，經常在深夜在床上煩惱哭泣為了貼文青圖而的你。

現在出現了這個偽文青廢圖產生器line-bot，有效解決為了貼文而煩惱的你。

## Build Process
### require Package Installation
'''
pip3 install -r requirements.txt
'''
or
'''
pip install -r requirements.txt
'''
### create your line bot

按這網站制作line bot:https://developers.line.biz/zh-hant/

![login](https://user-images.githubusercontent.com/72925954/122883848-28d86400-d370-11eb-8f1f-261f933f8108.PNG)
點下Log in登錄你的line

![messageAPI](https://user-images.githubusercontent.com/72925954/122884059-56251200-d370-11eb-9843-5fad7287e3cf.PNG)
之後先按下Line Develops 回到主頁後
之後按Message API

![startIT](https://user-images.githubusercontent.com/72925954/122884199-7bb21b80-d370-11eb-8a3d-c809b39ade4a.PNG)
下直住下滾動，直到找到開始使用Messaging API 

![startIT](https://user-images.githubusercontent.com/72925954/122885450-ad77b200-d371-11eb-9d4b-39cb59ddda5e.PNG)
按下開始體驗。
之後輸入基本資料
![name](https://user-images.githubusercontent.com/72925954/122885502-b9637400-d371-11eb-99fb-3c977650101e.PNG)
![messageInput](https://user-images.githubusercontent.com/72925954/122885510-bb2d3780-d371-11eb-9e44-c64ce506b464.PNG)
![cor](https://user-images.githubusercontent.com/72925954/122885577-c97b5380-d371-11eb-9de7-088a5caf1fe3.PNG)

最後接create
你的line bot建立成功了
### Input your Channel secret and Channel access token
你可以在Basic settings 找到你的Channel secret
在Messaging API 最下面
![line_channel_secret](https://user-images.githubusercontent.com/72925954/122888144-25df7280-d374-11eb-818f-09a470f7341d.PNG)

channel secret

![channel_long_access_token](https://user-images.githubusercontent.com/72925954/122888156-27a93600-d374-11eb-965e-7f3284db2982.PNG)

channel access token

之後用Notepad打開config.ini

![configFile](https://user-images.githubusercontent.com/72925954/122888607-97b7bc00-d374-11eb-8476-98506ae1d84d.PNG)

channel_access_token = 貼上你的line bot channel access token
channel_secret = 貼上你的line bot channel secret
### create your line bot Server
之後點撃ngrok.exe 行執它
不要關閉它，因為它是一個server
![ngerok](https://user-images.githubusercontent.com/72925954/122889799-b1a5ce80-d375-11eb-877f-ea24370c3f4f.PNG)
在界面輸入
```
ngrok http 5000
```

![webSite](https://user-images.githubusercontent.com/72925954/122890205-0d705780-d376-11eb-81bb-b48e15c3f317.PNG)

複製你所選取的網址
之後用Notepad打開你的app.py
在path貼上你的網址

![webSitePath](https://user-images.githubusercontent.com/72925954/122890757-8ec7ea00-d376-11eb-9dba-daa125bc2c04.PNG)
![pasteWebSitePath](https://user-images.githubusercontent.com/72925954/122890777-925b7100-d376-11eb-9441-11eb9daf2bcc.PNG)

之後打開新的cmd，去到你下載這檔案的路經底下打
```
pip app.py
```
or
```
pip3 app.py
```
最後在Message API 下的Webhook settings 按Edit
貼上你剛剛在ngrok界面的網址在後面要加上callback。
![pasteWebSiteOnLine](https://user-images.githubusercontent.com/72925954/122891942-8623e380-d377-11eb-8ffc-5864ca8db309.PNG)

按下Update之後按下Use webhook之後再按下Verify

![webhookAble](https://user-images.githubusercontent.com/72925954/122892652-27ab3500-d378-11eb-9169-fff479638931.PNG)
![sccuess](https://user-images.githubusercontent.com/72925954/122892760-40b3e600-d378-11eb-9e49-d235cc7bf741.PNG)



### reply message setting
在Messaging API 下Auto-reply messages的按Edit
![auto-reply](https://user-images.githubusercontent.com/72925954/122893337-d3ed1b80-d378-11eb-9d59-0360d83cca4b.PNG)

之後在Auto-reply messages的按Edit

![auto-replyEdit](https://user-images.githubusercontent.com/72925954/122893507-fa12bb80-d378-11eb-979f-e250ec281c2f.PNG)

調成以下設定就OK了

![replySetting](https://user-images.githubusercontent.com/72925954/122893707-26c6d300-d379-11eb-9586-344640f82b92.PNG)


### Add line bot Friend and start to use it
描QRcode加好友
![QRcode](https://user-images.githubusercontent.com/72925954/122892835-53c6b600-d378-11eb-8c93-c58cb1a70cd7.PNG)
傳送@photo
結果如下:
![30045](https://user-images.githubusercontent.com/72925954/122894204-9210a500-d379-11eb-9e95-c4b4044c671b.jpg)
![30050](https://user-images.githubusercontent.com/72925954/122894214-9341d200-d379-11eb-8391-dba2aeb4f6a6.jpg)



