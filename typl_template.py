from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, SourceUser, SourceGroup, SourceRoom, TemplateSendMessage, ConfirmTemplate, MessageAction, ButtonsTemplate,
    ImageCarouselTemplate, ImageCarouselColumn, URIAction, PostbackAction, DatetimePickerAction, CameraAction, CameraRollAction, LocationAction, CarouselTemplate, CarouselColumn,
    PostbackEvent, StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage, ImageMessage, VideoMessage, AudioMessage, FileMessage, UnfollowEvent, FollowEvent,
    JoinEvent, LeaveEvent, BeaconEvent, MemberJoinedEvent, MemberLeftEvent, FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent, TextComponent, SpacerComponent,
    IconComponent, ButtonComponent, SeparatorComponent, QuickReply, QuickReplyButton, ImageSendMessage)
from botocore.exceptions import ClientError
from pymongo import MongoClient, ASCENDING, DESCENDING
from bs4.element import NavigableString
from bs4 import BeautifulSoup
from decimal import Decimal
from errno import EEXIST
import typl_elements as typl
import traceback
import datetime
import requests
import logging
import errno
import boto3
import json
import json
import sys
import os

# === 將這個 Lambda 設定的環境變數 (environment variable) 輸出作為參考 ] ===
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 設定記錄等級為 INFO DEBUG

# === 在環境變數取得 LineBot Message API 的 channel_secret 和 channel_access_token 設定 LineBot Message API 的變數 line_bot_api 和 handler ] ===
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# === 設定 AWS EC2(MongoDB)/DynamoDB/SQS 的變數和取得環境變數 ] ===
aws_access_key_id = os.getenv('ACCESS_KEY')
aws_secret_access_key = os.getenv('SECRET_KEY')
ec2instance_id = os.getenv('EC2INSTANCE_ID')
region_name = os.getenv('REGION_NAME')
sqsclient = boto3.client('sqs', region_name=region_name)
dynamodb = boto3.resource('dynamodb', region_name='ap-east-1')
dynamodbTb_userop = dynamodb.Table('typl-userop')
mongo_user = os.getenv('MONGO_USER')
mongo_password = os.getenv('MONGO_PASSWORD')
logger.debug(os.environ)

# ===[ 定義 my_messageLogger 函式 ] ===
def my_messageLogger(loggingMessage):
    pass

# === [ 從桃園市圖書館的網站抓取館藏細節回傳所有館藏的字典清單 ] ===
def get_bookDetailPage(name, bookid):
    return books

# === [ 從桃園市圖書館的網站抓取分館開放時間細節顯示在 LINE 裡 ] ===
def get_libOpeningPage(libraryCode):
    return books

# === [ 從桃園市圖書館的網站抓取分館最新資訊顯示在 LINE 裡 ] ===
def get_libNewsPage(library, thisYear):
    return allNews, newsPage

# === [ 從桃園市圖書館的網站抓取借閱清單回傳清單 ] ===
def get_bookBorrowingPage(user, password):
    return username, books

# === [ 從桃園市圖書館的網站抓取預約清單回傳清單 ] ===
def get_bookExpectingPage(user, password):
    return username, books

# === [ 第八步驟 - 如果前面使用 purgeSQS_userQueue 時發生像是 Only one PurgeQueue operation on <queue> is allowed every 60 seconds 的錯誤這個函式會被呼叫做為替代方案 ] ===
def failsafeSQS_batchDeletion(books_left, sqsQurl_for_user):
    pass

# === [ 第七步驟 - 清空 Purge 使用者的 SQS 裡的 Queue 內容，如果無法呼叫 purge_queue 則改用 failsafeSQS_batchDeletion 做為備案 ] ===
def purgeSQS_userQueue(userId, books_left, onerror):
    pass

# ===[ 第六步驟 - 從 SQS Queue 佇列裡取回書籍清單 ] ===
def reply_CarouselFlexReceiveQ(function_id, userId, books, books_total):
    return FlexSendMessage(alt_text="正在顯示書本清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第五步驟 - 從 SQS 取得使用者的 Queue 的 QurueUrl ] ===
def getSQS_userQueueUrl(userId):

# === [ 第四步驟(3) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_rankCarouselFlexMongo(mongoBooks, books_total):
    return FlexSendMessage(alt_text="正在顯示書本清單", contents={"type":"carousel", "contents":carouselBubbles})


# === [ 第四步驟(2.4) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_cartCarouselFlexMongo_4(mongoBooks, currentLibrary, currentClassifyNos):
    return FlexSendMessage(alt_text="正在待借清單清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第四步驟(2.3) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_cartCarouselFlexMongo_3(mongoBooks, currentLibrary):
    return FlexSendMessage(alt_text="正在待借清單清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第四步驟(2.2) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_cartCarouselFlexMongo_2(mongoBooks):
    return FlexSendMessage(alt_text="正在待借清單清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第四步驟(2.1) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_cartCarouselFlexMongo_1(mongoBooks):
    return FlexSendMessage(alt_text="正在待借清單清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第四步驟(1) - 從 MongoDB 取回的書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_bookCarouselFlexMongo(mongoBooks, books_total):
    return FlexSendMessage(alt_text="正在顯示書本清單", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 第三步驟 - 將未讀取的書籍清單傳到 SQS Queue 裡的主程式區段 ] ===
def sendQ_MongoBooks(userId, mongoBooks):
    # === [ 依據屬性的鍵值決定 SQS Queue 裡的屬性類別 ] ===
    def getQ_attributeType(attributeKey, attribValue):
        return {'DataType': 'Number', 'StringValue': attribValue} if '_id' in attributeKey else {'DataType': 'String', 'StringValue': attribValue}

# ===[ 第二步驟 - 取得 MongoDB(EC2) 伺服器並回傳 MongoClient ] ===
def get_MongoClient():
    return mongoClient

# ===[ 第一步驟 - 先取得 MongoDB(EC2) 伺服器連線，再依據功能 funtion_id (分類號/關鍵字/待借清單) 送出查詢參數並回傳指定查詢的書籍清單 ] ===
def get_MongoBooks(function_id, userId, **kwargs):
    return books_total, books_fromMongo[:books]

# === [ 回覆博客來類別選單書籍 - 依據使用者篩選出分類，從 MongoDB 取回書籍資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_splacardCarouselFlex(userId, selectedMongoCollection, epochTstamp, kind, level, choice, item):
    return reply_rankCarouselFlexMongo(replyMongoData, books_total)

# === [ 取得使用者操作 - 從 DynamoDb 的 dynamodbTb 表格取回使用者的操作 Operation 記錄 ] ===
def getDynamo_userEntireItem(userId, dynamodbTb):
    return response['Item'] if 'Item' in response else None

# === [ 寫入使用者操作 - 將使用者的操作 Operation 記錄寫入 DynamoDb 的 dynamodbTb_userop 表格 ] ===
def putDynamo_userOperation(userId, epochTstamp, kind, nkind, level, choice, item, **kwargs):
    return True

# === [ 更新使用者操作 - 將使用者的操作 Operation 記錄更新 DynamoDb 的 dynamodbTb_userop 表格 ] ===
def updateDynamo_userOperation(userId, epochTstamp, kind, nkind, level, choice, item, **kwargs):
    return response

# === [ 更新使用者操作的書本數 - 更新使用者 DynamoDb 的 dynamodbTb_userop 表格裡的 book 書本數目 ] ===
def updateDynamo_userBooksCount(userId, decreased_books):

# === [ 寫入使用者個人資料 - 將使用者的個人資料 User Profile 寫入 DynamoDb 的 dynamodbTb_userpf 表格 ] ===
def putDynamo_userpf(userId, epochTstamp):
    return True

# === [ 更新使用者常用分類號資料 - 更新使用者的 DynamoDb 的 dynamodbTb 使用者的表格 ] ===
def removeDynamo_usercnORbc(dynamodbTb, typestr, userId, epochTstamp, cnORbc):
    return True

# === [ 寫入使用者常用分類號資料 - 加入使用者的 DynamoDb 的 dynamodbTb 使用者的表格 ] ===
def putDynamo_usercnORbc(dynamodbTb, typestr, userId, epochTstamp, cnORbc):

# === [ 更新使用者常用分類號資料 - 更新使用者的 DynamoDb 的 dynamodbTb 使用者的表格 ] ===
def updateDynamo_usercnORbc(dynamodbTb, typestr, userId, epochTstamp, cnORbc, lastcnORbcLists):
    return True

# === [ 新增使用者常用分類號資料 - 新增使用者的 DynamoDb 的 dynamodbTb 使用者的表格 ] ===
def addDynamo_usercnORbc(dynamodbTb, typestr, userId, epochTstamp, cnORbc):
    return True

# === [ 新增或修改使用者常用分館清單 - 新增使用者的 DynamoDb 的 dynamodbTb 使用者的表格 ] ===
def addDynamo_userlb(dynamodbTb, typestr, userId, epochTstamp, cnORbc):
    return True, None

# === [ 寫入使用者個人資料 - 將使用者的個人資料 User Profile 寫入 DynamoDb 的 dynamodbTb_userpf 表格 ] ===
def putDynamo_userid(userId, epochTstamp, useraccount, password):
    return True

# === [ 回覆常用分類號資料 - 依據從 DynamoDb 取回的分類號資料，回傳組成 LINE 的 FlexBubble 頁面完整的輪播 Carousel Flex Bubbles 圖片元素 ] ===
def reply_classifyCarouselFlexDynamo(userId, lastclassifynoLists):
    return FlexSendMessage(alt_text="正在顯示分類號資料目錄", contents={"type":"carousel", "contents":carouselBubbles})

# === [ 選擇常用分類號資料 - 依據從 DynamoDb 取回的分類號資料，回傳組成 LINE 的 quickReply 元素 ] ===
def quick_Classify(userId, lastclassifynoLists):
    return TextSendMessage(text="請點選下列任一個常用分類號快速選單。點選完後請稍候書籍查詢。", quick_reply=QuickReply(items=quickReplies))

# === [ 回覆完整書目分類資料快速選單 - 依據使用者分類號快速選單，回傳組成 LINE QuickReply 的元素 ] ===
def quick_Dictionary(userId):
    return TextSendMessage(text="請點選下列第一層分類號選單。點選後請稍候顯示。", quick_reply=QuickReply(items=quickReplies))

# === [ 回覆完整圖書館分館快速選單 - 依據使用者分區分館資訊快速選單，回傳組成 LINE QuickReply 的元素 ] ===
def quick_Libraries(userId, level, choice, item):
    return TextSendMessage(text="請點選下列分區分館資訊選單。點選後請稍候顯示。", quick_reply=QuickReply(items=quickReplies))

# === [ 回覆臨近圖書館分館地圖 - 依據使用者地埋位址快速選單，回傳臨近的分館 ] ===
def quick_closestLibrary(district, latitude, longitude):
    return library, address[library]

# === [ 變更查詢書籍用的指定月份快速選單 - 修改當月顯示月份快速選單，回傳組成 LINE QuickReply 的元素 ] ===
def quick_changeDate(userId, level, choice, item, theyear, themonth):
    return TextSendMessage(text="目前正在使用的年/月份為 %d 年 %d 月。請點選下列要變更的月份，點選後請稍候顯示。" % (theyear, themonth), quick_reply=QuickReply(items=quickReplies))

# === [ 回覆博客來類別選項快速選單 - 依據使用者分篩選出類別快速選單，回傳組成 LINE QuickReply 的元素 ] ===
def quick_booksCategrories(userId, level, choice, item):
    return TextSendMessage(text="請選擇下列排行榜分類。", quick_reply=QuickReply(items=quickReplies))

# === [ 回覆使用者輸入的文字訊息 - 依據使用者狀態，回傳組成 LINE 的 Text 文字元素 ] ===
def compose_textReplyMessage(userId, epochTstamp, messageText, userInfoItem):
    pass

# === [ 回覆使用者與程式使用者界面互動時回傳結果後的訊息 - 依據使用者狀態，回傳組成 LINE 的 Template 元素 ] ===
def compose_postbackReplyMessage(userId, epochTstamp, messageData, userInfoItem):
    pass

# === [ 這裡才是 lambda_handler 主程式區段 ]====================================================================================
def lambda_handler(event, context):

    # ==== [ 處理文字 TextMessage 訊息程式區段 ] ===
    @handler.add(MessageEvent, message=TextMessage)
    def handle_text_message(event):
        messageText = event.message.text
        userId = event.source.user_id
        epochTstamp = event.timestamp
        userInfoItem = getDynamo_userEntireItem(userId, dynamodbTb_userop)
        logger.debug('收到 MessageEvent 事件 | 使用者 %s 輸入了 [%s] 內容' % (userId, messageText))
        line_bot_api.reply_message(event.reply_token, compose_textReplyMessage(userId, epochTstamp, messageText, userInfoItem))

    # ==== [ 處理影 VideoMessage 音 AudioMessage 訊息程式區段 ] ===
    @handler.add(MessageEvent, message=(ImageMessage, VideoMessage, AudioMessage))
    def handle_content_message(event):
        userId = event.source.user_id
        logger.debug('收到 ImageMessage, VideoMessage, AudioMessage 事件 | 使用者 %s' % userId)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到一個影音檔但目前沒有處理這個檔案的功能'))

    # ==== [ 處理檔案訊息 FileMessage 的程式區段 ] ===
    @handler.add(MessageEvent, message=FileMessage)
    def handle_file_message(event):
        userId = event.source.user_id
        logger.debug('收到 FileMessage 事件 | 使用者 %s' % userId)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='收到一個檔案但目前沒有處理這個檔案的功能'))

    # ==== [ 處理追縱 FollowEvent 的程式區段 ] ===
    @handler.add(FollowEvent)
    def handle_follow(event):
        pass

    # ==== [ 處理取消追縱 FollowEvent 的程式區段 ] ===
    @handler.add(UnfollowEvent)
    def handle_unfollow(event):
        pass

    # ==== [ 處理使用者按下相關按鈕回應後的後續動作 PostbackEvent 程式區段 ] ===
    @handler.add(PostbackEvent)
    def handle_postback(event):
        messageData = json.loads(event.postback.data)
        userId = event.source.user_id
        epochTstamp = event.timestamp
        userInfoItem = getDynamo_userEntireItem(userId, dynamodbTb_userop)
        line_bot_api.reply_message(event.reply_token, compose_postbackReplyMessage(userId, epochTstamp, messageData, userInfoItem))

    # ==== [ 處理 BeaconEvent 的程式區段 ] ===
    @handler.add(BeaconEvent)
    def handle_beacon(event):
        pass

    # ==== [ 處理成員加入 MemberJoinedEvent 程式區段 ] ===
    @handler.add(MemberJoinedEvent)
    def handle_member_joined(event):
        pass

    # ==== [ 處理機器人加入了一個新聊天室, 有人傳了第一個訊息, 沒有使用者 ID 的程式區段 ] ===
    @handler.add(JoinEvent)
    def handle_join(event):
        pass

    # ==== [ 使用者離開目前的群組, 事件裡沒有使用者ID的程式區段 ] ===
    @handler.add(LeaveEvent)
    def handle_leave():
        pass

    # ==== [ 使用者離開臨時聊天室, 事件裡使用者ID在不同位置的程式區段 ] ===
    @handler.add(MemberLeftEvent)
    def handle_member_left(event):
        pass

# === [ 這裡才是 lambda_handler 主程式 ]=====================================================================================
    try:
        signature = event['headers']['x-line-signature']  # === 取得 event (事件) x-line-signature 標頭值 (header value)
        body = event['body']  # === 取得事件本文內容(body)
        eventheadershost = event['headers']['host']
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