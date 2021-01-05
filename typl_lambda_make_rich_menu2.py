from pymongo import MongoClient
import logging
import json
import os
import sys
import json
import uuid
import boto3
import errno
import logging
import datetime
import tempfile
import traceback
from errno import EEXIST
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (LineBotApiError, InvalidSignatureError)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage, RichMenu)


line_bot_api = LineBotApi('***')
handler = WebhookHandler('***')
rich_menu_initial = {
                "size":{
                    "width":2500,
                    "height":1686
                },
                "selected":True,
                "name":"請點選選單上的服務",
                "chatBarText":"請點選選單上的服務",
                "areas":[
                    {
                        "bounds":{
                            "x":179,
                            "y":218,
                            "width":587,
                            "height":558
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 1, 0)
                        }
                    },
                    {
                        "bounds":{
                            "x":988,
                            "y":224,
                            "width":563,
                            "height":547
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 2, 0)
                        }
                    },
                    {
                        "bounds":{
                            "x":1754,
                            "y":233,
                            "width":556,
                            "height":538
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 3, 0)
                        }
                    },
                    {
                        "bounds":{
                            "x":186,
                            "y":842,
                            "width":579,
                            "height":519
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 4, 0)
                        }
                    },
                    {
                        "bounds":{
                            "x":989,
                            "y":842,
                            "width":562,
                            "height":508
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 5, 0)
                        }
                    },
                    {
                        "bounds":{
                            "x":1763,
                            "y":848,
                            "width":545,
                            "height":520
                        },
                        "action":{
                            "type":"postback",
                            "data":'{"kind":"menu","level":"%d","choice":"%d","item":"%d"}' % (0, 6, 0)
                        }
                    }
                ]
            }
rich_menu_list = line_bot_api.get_rich_menu_list()
if rich_menu_list:
    print('rich_menu_list', rich_menu_list)
    line_bot_api.delete_rich_menu(line_bot_api.get_default_rich_menu())
else:
    myRichMenu_Id = line_bot_api.create_rich_menu(rich_menu=RichMenu.new_from_json_dict(rich_menu_initial))
    print('myRichMenu_Id:', myRichMenu_Id)
    uploadImageFile=open('D:/rich_menu_forallusers.jpg', 'rb')
    setImageResponse = line_bot_api.set_rich_menu_image(myRichMenu_Id, 'image/jpeg', uploadImageFile)
    if setImageResponse:
        print('setImageResponse:', setImageResponse)
    setImageResponse = line_bot_api.set_default_rich_menu(myRichMenu_Id)
    default_rich_menu = line_bot_api.get_default_rich_menu()
    print('default_rich_menu', default_rich_menu)
