import datetime
import json

import requests

cookie = ''        #在这输入cookie
new_cookie = None
date = None
time = None
Finished = False
push_token = ''   #push加推送 token


def fun1():
    global new_cookie
    global push_token
    url1 = 'http://jkttb.ycu.edu.cn:8082/microapp/health_daily/login?'
    header1 = {
        'Host': 'jkttb.ycu.edu.cn:8082',
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla / 5.0(Linux;Android10;EBG - AN00Build / HUAWEIEBG - AN00;wv) AppleWebKit / 537.36('
                      'KHTML, likeGecko) Version / 4.0Chrome / 89.0.4389.72MQQBrowser / 6.2TBS / 046125MobileSafari / '
                      '537.36wxwork / 4.0.16ColorScheme / DarkMicroMessenger / 7.0.1NetType / WIFILanguage / zhLang / '
                      'zh',
        'X-Requested-With': 'com.tencent.wework',
        'Content-Length': '0',
        'Origin': 'http://jkttb.ycu.edu.cn:8082',
        'Referer': 'http://jkttb.ycu.edu.cn:8082/front/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Cookie': cookie,
        'Accept': 'application/json, text/plain, */*'
    }
    parm = {
        'code': '7Bsw1tnzGQ2prrsdfl6V1fS5Wzig4ri26v5knWprSYo',
        'state': 'microapp'

    }

    r0 = requests.get(url=url1, headers=header1, params=parm)
    print(r0.status_code)
    print('获取SetCookie返回的响应是', r0.headers)

    print('获取ID和Time返回的json类型值', r0.content.decode())
    print(r0.request.url)
    print('header 是', r0.headers)

    try:
        print('SetCookie是', r0.headers['Set-Cookie'])
        new_cookie = r0.headers['Set-Cookie'][0:43]
        print(new_cookie)
    except KeyError:
        new_cookie = cookie
        parms1 = {
            'token': push_token,
            'content': 'Cookie is already up to date'
        }
        r4 = requests.get(url='http://www.pushplus.plus/send?', params=parms1)
        # 微信推送
        print(r4.status_code)
        print('没有新的Cookie')


# 获取 id 和 时间
def fun2():
    global new_cookie
    global push_token
    print('fun2', new_cookie)
    url2 = 'http://jkttb.ycu.edu.cn:8082/microapp/health_daily/alreadyReport?'
    header2 = {
        'Host': 'jkttb.ycu.edu.cn:8082',
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla / 5.0(Linux;Android10;EBG - AN00Build / HUAWEIEBG - AN00;wv) AppleWebKit / 537.36('
                      'KHTML, likeGecko) Version / 4.0Chrome / 89.0.4389.72MQQBrowser / 6.2TBS / 046125MobileSafari / '
                      '537.36wxwork / 4.0.16ColorScheme / DarkMicroMessenger / 7.0.1NetType / WIFILanguage / zhLang / '
                      'zh',
        'X-Requested-With': 'com.tencent.wework',
        'Content-Length': '0',
        'Origin': 'http://jkttb.ycu.edu.cn:8082',
        'Referer': 'http://jkttb.ycu.edu.cn:8082/front/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q=0.9,en;q=0.8,en-US;q=0.7',
        'Cookie': new_cookie,
        'Accept': 'application/json, text/plain, */*'
    }
    data = {

    }
    params = {
        'userid': '2020060514',
        'day': date
    }

    r5 = requests.post(url2, data=data, headers=header2, params=params)

    json_data = json.loads(r5.content.decode())
    print('获取ID和Time返回的数据', json_data)  # 将json转化为字典
    global time
    # global id1
    try:
        id1 = json_data['data'][0]['id']
        time = json_data['data'][0]['time']
        # print(type(id1))

        print('id 是', id1)
        print('time 是', time)
        return id1
    except TypeError:
        print(' Id 和 Time 获取错误')
        parms2 = {
            'token': push_token,
            'content': 'ID and Time Error'
        }
        r4 = requests.get(url='http://www.pushplus.plus/send?', params=parms2)
        # 微信推送
        print(r4.status_code)
        print('stacosde 类型', type(r4.status_code))


def fun3(id3, null=None):
    global time
    global id1
    global push_token
    print('fun3', new_cookie)
    url3 = 'http://jkttb.ycu.edu.cn:8082/microapp/health_daily/report'
    header3 = {
        'Host': 'jkttb.ycu.edu.cn:8082',
        'Connection': 'keep - alive',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla / 5.0(Linux;Android10;EBG - AN00Build / HUAWEIEBG - AN00;wv) AppleWebKit / 537.36('
                      'KHTML, likeGecko) Version / 4.0Chrome / 89.0.4389.72MQQBrowser / 6.2TBS / 046125MobileSafari / '
                      '537.36wxwork / 4.0.16ColorScheme / DarkMicroMessenger / 7.0.1NetType / WIFILanguage / zhLang / '
                      'zh',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://jkttb.ycu.edu.cn:8082',
        'Referer': 'http://jkttb.ycu.edu.cn:8082/front/',
        'X-Requested-With': 'com.tencent.wework',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN, zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Length': '1124',
        'Cookie': new_cookie

    }
    global Finished
    print(id3)
    print(time)
    if id3 is not None and time is not None:

        data2 = {
            "address": "", "locationErrorExplain": "运城学院", "province": "山西省", "city": "运城市",
            "county": "盐湖区",
            "distance": -1, "longitude": 0, "latitude": 0, "temperature": "37", "healthCondition": "正常",
            "healthConditionExplain": null, "familyCondition": "正常", "familyConditionExplain": null,
            "recentlyGoArea": "无", "recentlyGoAreaExplain": null, "ifContactCase": "无", "ifContactCaseExplain": null,
            "ifContactAreaBackPerson": "无", "ifContactAreaBackPersonExplain": null, "ifContactRjry": "无",
            "ifContactRjryExplain": null, "ifReturnToSchool": "无", "ifReturnToSchoolExplain": null,
            "startingPoint": null,
            "terminalPoint": null, "vehicle": null, "billingContactName": null, "billingContactNameTel": null,
            "specialSituation": null, "ifFromToFocusArea": "否", "ifFromToFocusAreaExplain": "", "fileUrl": "",
            "time": time,
            "plusinfo": "Mozilla/5.0 (Linux; Android 10; EBG-AN00 Build/HUAWEIEBG-AN00; wv) AppleWebKit/537.36 ("
                        "KHTML, "
                        "like Gecko) Version/4.0 Chrome/89.0.4389.72 MQQBrowser/6.2 TBS/046125 Mobile Safari/537.36 "
                        "wxwork/4.0.16 ColorScheme/Dark MicroMessenger/7.0.1 NetType/WIFI Language/zh Lang/zh",
            "id": id3
        }

        r6 = requests.post(url3, json=data2, headers=header3)
        Finished = True
    else:
        parms3 = {
            'token': push_token,
            'content': '获取不到 ID 和 Time ，可能因为超过了打卡时间'
        }

        print('获取不到id和time')
        r4 = requests.get(url='http://www.pushplus.plus/send?', params=parms3)
        # 微信推送
        print(r4.status_code)

    if Finished:
        parms4 = {
            'token': push_token,
            'content': '打卡成功！'

        }
        print('打卡成功')
        r4 = requests.get(url='http://www.pushplus.plus/send?', params=parms4)
        print('推送状态码', r4.status_code)
        # 微信推送
        exit()
    else:
        print('打卡失败')
        parms5 = {
            'token': push_token,
            'content': '打卡失败！！！'

        }
        r4 = requests.get(url='http://www.pushplus.plus/send?', params=parms5)
        print('推送状态码', r4.status_code)


def process():
    global date
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    fun1()
    id3 = fun2()  # 取id和time
    fun3(id3)  # 提交打卡


if __name__ == '__main__':
    # def handler(event, context):
    process()
