# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:05:00 2020

@author: peishuo
"""

import json
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
import QA_Col
import random

app = Flask(__name__)


line_bot_api = LineBotApi('ABBASg7raTqZBOH+LoJhOqjHAtd3B1YWcKqzlMYH7PrXkjsJR1D8u9lhLqKK9OKACVSFijqC4+OoS979zuNF+22Xjl6UtfCbKFadjzP23fVhmTcTWd17LXA34s4po47YJd00wIHy1u+qKWEHff7ifAdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('ce973cb1bfcb8e8b27040457490e009c')

line_bot_api.push_message('U106d90b9cf035a5ab3b4a0ba62564ef3', TextSendMessage(text='系統測試中，若您覺得訊息干擾到您，您可以將聊天室設為靜音，謝謝喔！'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

######################處理LINE USER 傳來得訊息 ###############################
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # get user id when reply
    
    profile = line_bot_api.get_profile(event.source.user_id)
    nameid = profile.display_name     #使用者名稱
    uid = profile.user_id             #使用者ID  
    user_message=str(event.message.text) 
    

        #user_message='圖文訊息'
    if user_message.find('圖文訊息') != -1:    
        
        res_message = TemplateSendMessage(
            alt_text='圖文訊息',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='文字訊息',
                                text='文字訊息'
                            ),
                            MessageTemplateAction(
                                label='圖片訊息',
                                text='圖片訊息'
                            ),
                            MessageTemplateAction(
                                label='影片訊息',
                                text='影片訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='音訊訊息',
                                text='音訊訊息'
                            ),
                            MessageTemplateAction(
                                label='位置訊息',
                                text='位置訊息'
                            ),
                            MessageTemplateAction(
                                label='貼圖訊息',
                                text='貼圖訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='按鈕介面訊息',
                                text='按鈕介面訊息'
                            ),
                            MessageTemplateAction(
                                label='確認介面訊息',
                                text='確認介面訊息'
                            ),
                            MessageTemplateAction(
                                label='輪播模板訊息',
                                text='輪播模板訊息'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='圖文訊息選單',
                        text='請由下方選出您想測試的訊息格式！',
                        actions=[
                            MessageTemplateAction(
                                label='輪播圖模板訊息',
                                text='輪播圖模板訊息'
                            ),
                            URITemplateAction(
                                label='Line官方說明文件',
                                uri='https://developers.line.biz/zh-hant/docs/messaging-api/message-types/#common-features'
                            ),
                            MessageTemplateAction(
                                label='其他',
                                text='教材尚在開發中'
                            ),
                        ]
                    ),                                          
# =============================================================================        
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='文字訊息'
    elif user_message.find('聯絡商家') != -1:         #判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。   
        
        res_message = TextSendMessage(text='您可以透過以下方式聯絡我們： \n電話：456-789-012 \nEmail：info@deliciousbakery.com \n地址：台北市美味路456號 \n歡迎隨時與我們聯繫，我們期待為您提供最好的服務')        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0
###############################################################################
        # user_message='文字訊息'
    elif user_message.find('你們有什麼最新的優惠活動？') != -1:  # 判斷用戶使否傳來"文字訊息"關鍵字，若為是則觸發本區段。   

        res_message = TextSendMessage(
            text='我們最新推出了「滿額送禮」活動🎉！ \n當您在本店消費滿1000元，即可獲得一份精美的甜點禮盒🎁。 \n另外，前50名達到此消費標準的顧客還將獲得一張20%折扣卷，可用於下次購物🛍️~ \n預祝您消費愉快!')
        line_bot_api.reply_message(event.reply_token, res_message)
        return 0

###############################################################################
    elif user_message.find('圖片訊息') != -1 :         #判斷用戶使否傳來"圖片訊息"關鍵字，若為是則觸發本區段。  
        
        res_message = ImageSendMessage(
            original_content_url='https://cdn2.ettoday.net/images/3053/3053944.jpg',
            preview_image_url='https://cdn2.ettoday.net/images/3053/3053944.jpg'
        )
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0  
    
###############################################################################
        #user_message='影片訊息'
    elif user_message.find('影片訊息') != -1:         #判斷用戶使否傳來"影片訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = VideoSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=22&source=youtube&requiressl=yes&vprv=1&mime=video%2Fmp4&ns=6LcWIDtZWbxjYUXS1Dod_vIF&ratebypass=yes&dur=328.423&lmt=1572331630804319&fvip=5&c=WEB&txp=2216222&n=fRjt_f_oTJeD95i&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMXkWqUW9UIIMrcCJZ8dh_xZ7nWpUlNVWd4sdw2JHME4AiAKGxqLL5z6kL30RkfuW-mCUVIwWmqG1nPPOo0_PbecxA%3D%3D&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=3b1b213d3dba3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858827&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRAIgXT3f533nuXNJnQlehCh9ePDKFQtHpmkoWKAN1IzsJsgCIBtOmjBzv9DrdIWDtPjsHRSZXLCFcjAZN1zQSqWOHGEM',
            preview_image_url='https://lh3.googleusercontent.com/pw/ACtC-3fmvQXV2wh96fqQjSJ5KZXRUjprXHH9zG2EVFLuExV-Uxl1sN2AQ76RIN8Cy6A0COCT4FvQg9YRzqNujWkrxwA3kgGLcAOtsupqBi0JCqx4HUQuMqR8KMJ6CRQ7FBSJ3JLHfYv04V_BFmQAMFQIrWgvsg=w958-h539'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='音訊訊息'
    elif user_message.find('音訊訊息') != -1:         #判斷用戶使否傳來"音訊訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = message = AudioSendMessage(
            original_content_url='https://r5---sn-npoe7n7r.googlevideo.com/videoplayback?expire=1612879931&ei=20MiYIfkBIyWiwTEhrSQBQ&ip=144.202.56.145&id=o-ANCIwAp79OWJyLwTkkaRuKvMzGSf6gsljTB-wPAcLNh5&itag=140&source=youtube&requiressl=yes&vprv=1&mime=audio%2Fmp4&ns=vL6EbYMqRar6wkILnGFdM6sF&gir=yes&clen=5315836&otfp=1&dur=328.423&lmt=1572331593044296&fvip=5&keepalive=yes&c=WEB&txp=2211222&n=jinyYfcO0NUsfzO&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cotfp%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAL1zzZOOX4qwpMs5f8cTrPvw7OLcoFlrx7IoNt4qKE_jAiA7W2Xce4BnGqfOPsuzNGEVGudGIMhqHBb5d40qsKMjdQ%3D%3D&ratebypass=yes&redirect_counter=1&cm2rm=sn-vgqe7s76&req_id=a0e283de1a31a3ee&cms_redirect=yes&mh=ww&mip=182.234.79.223&mm=34&mn=sn-npoe7n7r&ms=ltu&mt=1612858105&mv=m&mvi=5&pl=18&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhANHX1USrlIJC8IXts4LcHkOClswgQoSKtfv-bBU76R7VAiB8SAfZxTgonssKfxUs6FL8O8Q5wn5cnL2r_OSUuKtjRQ%3D%3D',
            duration=328000
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='位置訊息'
    elif user_message.find('位置訊息') != -1:         #判斷用戶使否傳來"位置訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = LocationSendMessage(
            title='文藻外語大學',
            address='80793高雄市三民區民族一路900號',
            latitude=22.6704067,
            longitude=120.3191348
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='貼圖訊息'
    elif user_message.find('貼圖訊息') != -1:         #判斷用戶使否傳來"貼圖訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = StickerSendMessage(
            package_id='11539',
            sticker_id='52114116'
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0

###############################################################################
        #user_message='按鈕介面訊息'
    elif user_message.find('我想看一下你們的菜單') != -1:         #判斷用戶使否傳來"按鈕介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='美味家烘焙坊菜單',
            template=ButtonsTemplate(
                thumbnail_image_url='https://png.pngtree.com/element_pic/00/16/08/0457a237bf0c42d.jpg',
                title='美味家烘焙坊菜單',
                text='請點擊以下按鈕查看我們的菜單。',
                actions=[
                    MessageTemplateAction(
                        label='蛋糕類',
                       text='https://dfuhdfhosd.dsv cclov.sdfipo'
                    ),
                    MessageTemplateAction(
                        label='麵包類',
                        text='https://dfuhdfhosd.dsv cclov.sdfip'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='確認介面訊息'
    elif user_message.find('確認介面訊息') != -1:         #判斷用戶使否傳來"確認介面訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【確認介面訊息】',
            template=ConfirmTemplate(
                text='您是否確認要離開本次對話？',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='我要離開對話'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='圖文訊息'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='輪播模板訊息'
    elif user_message.find('我想訂購商品') != -1:         #判斷用戶使否傳來"輪播模板訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【我想訂購商品】',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/0/04/Pound_layer_cake.jpg',
                        title='用戶線上訂購: \n蛋糕類商品🎂',
                        text='歡迎使用對話方塊與我們訂購商品呦~',
                        actions=[
                            MessageTemplateAction(
                                label='訂購巧克力蛋糕🎂',
                                text='我要訂購一份巧克力蛋糕'
                            ),
                            MessageTemplateAction(
                                label='訂購草莓蛋糕🎂',
                                text='我要訂購一份草莓蛋糕'
                            ),
                            MessageTemplateAction(
                                label='訂購香草蛋糕🎂',
                                text='我要訂購一份香草蛋糕'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Whitney_Wright_2017-06-15_%28Unsplash%29.jpg/1280px-Whitney_Wright_2017-06-15_%28Unsplash%29.jpg',
                        title='用戶線上訂購: \n麵包類商品🎂',
                        text='歡迎使用對話方塊與我們訂購商品呦~。',
                        actions=[
                            MessageTemplateAction(
                                label='訂購牛角麵包🥐',
                                text='我要訂購一份牛角麵包'
                            ),
                            MessageTemplateAction(
                                label='訂購法國麵包🥖',
                                text='我要訂購一份法國麵包'
                            ),
                            MessageTemplateAction(
                                label='訂購吐司🍞',
                                text='我要訂購一份吐司'
                            )
                        ]
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='輪播圖模板訊息'
    elif user_message.find('輪播圖模板訊息') != -1:         #判斷用戶使否傳來"輪播圖模板訊息"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='本訊息為【輪播圖模板訊息】',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic04.jpg',
                        action=PostbackTemplateAction(
                            label='輪播圖一',
                            text='輪播圖一：您可以在此輸入您要描述的文字。',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://www.nups.ntnu.edu.tw/upfiles/univ-expo/%E5%8D%97%E9%83%A8/%E9%AB%98%E9%9B%84%E5%B8%82/%E6%8A%80%E5%B0%88%E6%A0%A1%E9%99%A2/%E6%96%87%E8%97%BB/%E6%96%87%E8%97%BB-pic02.jpg',
                        action=PostbackTemplateAction(
                            label='輪播圖二',
                            text='輪播圖二：您可以在此輸入您要描述的文字。',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)

        return 0
    
###############################################################################
        #user_message='相關網頁->學術單位'
    elif user_message.find('相關網頁->學術單位') != -1:         #判斷用戶使否傳來"相關網頁->學術單位"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->學術單位',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='英國語文系',
                                uri='http://c021.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='翻譯系',
                                uri='http://c033.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際事務系',
                                uri='http://c030.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='國際企業管理系',
                                uri='http://c031.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='英語教學中心',
                                uri='http://c043.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='法國語文系',
                                uri='http://c022.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='德國語文系',
                                uri='http://c023.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='西班牙語文系',
                                uri='http://c024.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='日本語文系',
                                uri='http://c025.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='外語教學系',
                                uri='http://c036.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='應用華語文系',
                                uri='http://c026.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='傳播藝術系',
                                uri='http://c032.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='學術單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='數位內容應用與管理系',
                                uri='http://c028.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='師資培育中心',
                                uri='http://c035.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='通識教育中心',
                                uri='http://c034.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================    
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁->行政單位'
    elif user_message.find('相關網頁->行政單位') != -1:         #判斷用戶使否傳來"相關網頁->行政單位"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->行政單位',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校長室',
                                uri='https://c001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='副校長室',
                                uri='https://c002.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='秘書室',
                                uri='https://c008.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='教務處',
                                uri='https://c003.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='學生事務處',
                                uri='https://c004.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='研究發展處',
                                uri='https://c016.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='總務處',
                                uri='https://c005.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='國際暨兩岸合作處',
                                uri='https://c015.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='進修部',
                                uri='https://c007.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='推廣部',
                                uri='https://c049.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='會計室',
                                uri='https://c010.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='人事室',
                                uri='https://c009.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='行政單位',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊與教學科技中心',
                                uri='https://c013.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='教師發展中心',
                                uri='https://c014.wzu.edu.tw/'
                            ),
                        ]
                    ),                                          
# =============================================================================  
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁->常用網頁'
    elif user_message.find('相關網頁->常用網頁') != -1:         #判斷用戶使否傳來"相關網頁->常用網頁"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁->常用網頁',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='校網首頁',
                                uri='https://a001.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='圖書館',
                                uri='https://lib.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='資訊服務入口網',
                                uri='https://sso.wzu.edu.tw/Portal/login.htm'
                            ),
                        ]
                    ),                                          
# =============================================================================
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='常用網頁',
                        text='請由下方選項中選出您需要的網頁！',
                        actions=[
                            URITemplateAction(
                                label='雲端學園',
                                uri='http://elearning2.wzu.edu.tw/'
                            ),
                            URITemplateAction(
                                label='網路選課系統',
                                uri='https://info.wzu.edu.tw/choice/'
                            ),
                            URITemplateAction(
                                label='活動管理系統',
                                uri='http://ma.wzu.edu.tw/bin/home.php'
                            ),
                        ]
                    ),                                          
# =============================================================================   
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
        #user_message='相關網頁'
    elif user_message.find('相關網頁') != -1:         #判斷用戶使否傳來"相關網頁"關鍵字，若為是則觸發本區段。 
        
        res_message = TemplateSendMessage(
            alt_text='相關網頁',
            template = CarouselTemplate(
                columns=[
#-----------------------------------------------------------------------------                    
                    CarouselColumn(
                        # thumbnail_image_url='',
                        title='請選擇您想查找的頁面',
                        text='請由下方選項中選出子分類！',
                        actions=[
                            MessageTemplateAction(
                                label='學術單位',
                                text='相關網頁->學術單位'
                            ),
                            MessageTemplateAction(
                                label='行政單位',
                                text='相關網頁->行政單位'
                            ),
                            MessageTemplateAction(
                                label='常用網頁',
                                text='相關網頁->常用網頁'
                            )
                        ]
                    ),                                          
# =============================================================================
                 ]            
            )
        )
        
        line_bot_api.reply_message(event.reply_token,res_message)
        return 0   
        
###############################################################################
    elif user_message.find('輪播圖') != -1:
        
        return 0
###############################################################################
    elif user_message.find('您剛剛點擊了') != -1:
        
        return 0
###############################################################################
    elif user_message.find('教材尚在開發中') != -1:
        
        return 0
###############################################################################
    elif user_message.find('我要離開對話') != -1:
        response='好的，期待您下次的呼喚，再見！'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        
        return 0
###############################################################################
    else:
        response='太棒了，已經記錄在小編的小本本上啦📒✨！ \n有任何其他問題或需求，隨時歡迎提出哦！🌟！'
        line_bot_api.reply_message(event.reply_token,TextSendMessage(response))
        return 0
        
    
    # user_id = event.source.user_id
    # print("user_id =", user_id)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))



###############################################################################
import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
if __name__ == "__main__":
    app.run()
