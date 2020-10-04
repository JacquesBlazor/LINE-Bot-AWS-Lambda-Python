from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, SourceUser, SourceGroup, SourceRoom, TemplateSendMessage, ConfirmTemplate, MessageAction, ButtonsTemplate, 
    ImageCarouselTemplate, ImageCarouselColumn, URIAction, PostbackAction, DatetimePickerAction, CameraAction, CameraRollAction, LocationAction, CarouselTemplate, CarouselColumn, 
    PostbackEvent, StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, UnfollowEvent, FollowEvent, 
    JoinEvent, LeaveEvent, BeaconEvent, MemberJoinedEvent, MemberLeftEvent, FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent, TextComponent, SpacerComponent, 
    IconComponent, ButtonComponent, SeparatorComponent, QuickReply, QuickReplyButton, ImageSendMessage)
import requests, traceback, logging, boto3, json, sys, os
from botocore.exceptions import ClientError
from bs4 import BeautifulSoup

# === 將這個 Lambda 設定的環境變數 (environment variable) 輸出作為參考 ] ===
logger = logging.getLogger()
logger.setLevel(logging.INFO) 
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if not channel_secret or not channel_access_token:
    logger.error('需要在 Lambda 的環境變數 (Environment variables) 裡新增 LINE_CHANNEL_SECRET 和 LINE_CHANNEL_ACCESS_TOKEN 作為環境變數。')
    sys.exit(1)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)    
logger.info(os.environ)  

# ===[ 定義你的函式 ] ===
def get_userOperations(userId):
    return None

# === [ 定義回覆使用者輸入的文字訊息 - 依據使用者狀態，回傳組成 LINE 的 Template 元素 ] ===
def compose_textReplyMessage(userId, userOperations, messageText):
    return TextSendMessage(text='好的！已收到您的文字 %s！' % messageText)

# === [ 定義回覆使用者與程式使用者界面互動時回傳結果後的訊息 - 依據使用者狀態，回傳組成 LINE 的 Template 元素 ] ===
def compose_postbackReplyMessage(userId, userOperations, messageData):
    return TextSendMessage(text='好的！已收到您的動作 %s！' % messageData)

# === [ 主程式 - 這裡是主要的 lambda_handler 程式進入點區段，相當於 main() ]==================================================================================== 
def lambda_handler(event, context):
    
    # ==== [ 處理文字 TextMessage 訊息程式區段 ] ===
    @handler.add(MessageEvent, message=TextMessage)    
    def handle_text_message(event):
        userId = event.source.user_id
        messageText = event.message.text
        userOperations = get_userOperations(userId)
        logger.info('收到 MessageEvent 事件 | 使用者 %s 輸入了 [%s] 內容' % (userId, messageText))
        line_bot_api.reply_message(event.reply_token, compose_textReplyMessage(userId, userOperations, messageText))

    # ==== [ 處理使用者按下相關按鈕回應後的後續動作 PostbackEvent 程式區段 ] ===
    @handler.add(PostbackEvent)   
    def handle_postback(event):
        userId = event.source.user_id 
        messageData = json.loads(event.postback.data)
        userOperations = get_userOperations(userId)        
        logger.info('收到 PostbackEvent 事件 | 使用者 %s' % userId)        
        line_bot_api.reply_message(event.reply_token, compose_postbackReplyMessage(userId, userOperations, messageData))

    # ==== [ 處理追縱 FollowEvent 的程式區段 ] === 
    @handler.add(FollowEvent)  
    def handle_follow(event):
        userId = event.source.user_id
        logger.info('收到 FollowEvent 事件 | 使用者 %s' % userId)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='歡迎您的加入 !'))      

# === [ 這裡才是 lambda_handler 主程式 ]===================================================================================== 
    try:
        signature = event['headers']['x-line-signature']  # === 取得 event (事件) x-line-signature 標頭值 (header value)
        body = event['body']  # === 取得事件本文內容(body)
        # eventheadershost = event['headers']['host']        
        handler.handle(body, signature)  # === 處理 webhook 事件本文內容(body)
    
    # === [ 發生錯誤的簽章內容(InvalidSignatureError)的程式區段 ] ===
    except InvalidSignatureError:
        return {
            'statusCode': 400,
            'body': json.dumps('InvalidSignature') }        
    
    # === [ 發生錯誤的LineBotApi內容(LineBotApiError)的程式區段 ] ===
    except LineBotApiError as e:
        logger.error('呼叫 LINE Messaging API 時發生意外錯誤: %s' % e.message)
        for m in e.error.details:
            logger.error('-- %s: %s' % (m.property, m.message))
        return {
            'statusCode': 400,
            'body': json.dumps(traceback.format_exc()) }
    
    # === [ 沒有錯誤(回應200 OK)的程式區段 ] ===
    return {
        'statusCode': 200,
        'body': json.dumps('OK') }