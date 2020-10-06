# --- The MIT License (MIT) Copyright (c) alvinconstantine(alvin.constantine@outlook.com), Tue Oct 6 14:15pm 2020 ---

import boto3
import json
import prettytable as pt

region_name = 'ap-east-1'
client = boto3.client('logs', region_name=region_name)
logGroupName = '/aws/lambda/typl-lambda-linebot'

log_streams_response = client.describe_log_streams(logGroupName=logGroupName, orderBy='LastEventTime', descending=True, limit=5)
for no_, i in enumerate(log_streams_response['logStreams']):
    logStreamName = i['logStreamName']
    log_events_response = client.get_log_events(
        logGroupName=logGroupName,
        logStreamName=logStreamName,
        startFromHead=True
    )
    filenameprefix = logGroupName.split('/')[-1]
    filenamepostfix = logStreamName.split(']')[-1]
    filename = ('%d_' % (no_+1)) + filenameprefix+'.'+filenamepostfix
    counter = 1
    cloudWatchTable = pt.PrettyTable(encoding='utf-8')
    cloudWatchTable.field_names = ['順序', '記錄類型', '日期', '時間', '內容']
    cloudWatchTable.align['內容'] =  'l'
    for i in log_events_response['events']:
            if i['message'].startswith('['):
                    iMessage = i['message'].strip('')
                    sMessage = iMessage.split('\t')
                    if len(sMessage) != 1:
                        eMessage = sMessage.pop(2)
                        tMessage = sMessage.pop(1)
                        dMessage = tMessage.split('T')
                        dMessage[-1] = dMessage[-1].replace('Z', '')
                        sMessage.insert(1, dMessage[-1])
                        sMessage.insert(1, dMessage[0])
                    else:
                        capturedMessage = sMessage.copy()
                        errQuote = sMessage[0][sMessage[0].find('['):sMessage[0].find(']')+1]
                        sMessage[0] = sMessage[0].replace(errQuote+' ', '')
                        sMessage = [errQuote, '', '', sMessage[0].replace('\r', '\n').replace('\xa0', ' ')]
                    cloudWatchTable.add_row([counter]+sMessage)
                    counter += 1
            elif i['message'].startswith('START RequestId'):
                if counter>1:                      
                        cloudWatchTable.add_row(['----', '-------', '---------', '------------', '-'*160])
    print('=== 正在儲存 CloudWatch 記錄 %s 檔案 ===' % filename)
    with open(filename+'.txt', 'w', encoding =' utf-8-sig') as f:
        f.write(str(cloudWatchTable))
