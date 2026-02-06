import requests
import time
import re
import os

from datetime import datetime
from fn_print import fn_print
from get_env import get_env
from sendNotify import send_notification_message_collection

# 从环境变量中获取 Cookie
COOKIES = os.getenv('jiaoyuepan_COOKIE', '')
#SERVER_CHAN_KEY = os.getenv('SERVER_CHAN', '') // Service酱推送的key

headers = {
  'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
  'cache-control': "max-age=0",
  'origin': "https://vip.jiaoyupan.cc",
  'priority': "u=0, i",
  'referer': "https://vip.jiaoyupan.cc/dsu_paulsign-sign.html",
  'sec-ch-ua': "\"Not;A=Brand\";v=\"99\", \"Microsoft Edge\";v=\"139\", \"Chromium\";v=\"139\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Windows\"",
  'sec-fetch-dest': "iframe",
  'sec-fetch-mode': "navigate",
  'sec-fetch-site': "same-origin",
  'sec-fetch-user': "?1",
  'upgrade-insecure-requests': "1",
  'Cookie': COOKIES
}

params = {
  'id': "dsu_paulsign:sign",
  'operation': "qiandao",
  'infloat': "1",
  'inajax': "1"
}

payload = {
  'formhash': "30e41d56",
  'qdxq': "kx"
}

#def publish_wechat(SERVER_CHAN_KEY, sign_result_vo, duration):
#    if SERVER_CHAN_KEY is None:
 #       print("SERVER_CHAN 未设置")
  #      return
 
   # title = f"百度网盘签到：{sign_result_vo}"
#推送给链接有问题
 #   if duration is not None:
  #      title += f"，耗时 {duration}ms"
 
   # try:
    #    print('测试',sign_result_vo,duration)
     #   url = f"https://sc.ftqq.com/{SERVER_CHAN_KEY}.send"
      #  params = {
       #     "text": title,
        #    "desp": duration
        #}
        #response = requests.get(url, params=params)
        #response.raise_for_status()
    #except Exception as e:
     #   print(e)
        
def signin():
    url = 'https://vip.jiaoyupan.cc/plugin.php'
    #response = requests.get(url, headers=HEADERS)
    #response = requests.post(url, data=payload, headers=HEADERS)
    response = requests.post(url, params=params, data=payload, headers=headers)
    if response.status_code == 200:
        #sign_point = re.search(r'points":(\d+)', response.text)
        #signin_error_msg = re.search(r'"error_msg":"(.*?)"', response.text)
        #print(f"签到成功, 获得积分: {sign_point.group(1) if sign_point else '未知'}")
        #publish_wechat(SERVER_CHAN_KEY, f"签到成功",f"获得积分")
        #if signin_error_msg:
            #print(f"签到错误信息: {signin_error_msg.group(1)}")
        #print(response.text)
        fn_print(response.text.encode().decode("unicode_escape"))
    else:
        #print("签到失败")
        fn_print("签到失败")
       

def main():
    signin()

if __name__ == "__main__":
    main()
    send_notification_message_collection(f"安鹿轩签到通知 - {datetime.now().strftime('%Y/%m/%d')}")

# 云函数入口
def handler(event, context):
    main()
