#!/usr/local/pyenv/shims/python
# coding:utf-8
 
import time
import re
from slackclient import SlackClient
 
class SlackBotMain:
 
    token = "xoxb-346303851888-410759035234-0TMSInWeKNGaJ1d5o3eJCbEg" # メモしておいたトークンを設定
    sc = SlackClient(token)
 
    def __init__(self):
        if SlackBotMain.sc.rtm_connect():
            while True:
                data = SlackBotMain.sc.rtm_read()
 
                if len(data) > 0:
                    for item in data:
                        SlackBotMain.sc.rtm_send_message("fyi", self.create_message(item))
 
                time.sleep(1)
        else:
            print ('Connection Failed, invalid token?')
 
 
    def create_message(self, data):
        if "type" in data.keys():
            if data["type"] == "message":
                if "text" in data.keys():
                    if re.search(u"(.*帰ります.*|.*帰宅.*)", data["text"]) is not None:
                        return "<@" + data["user"] + "> " + u"お疲れ様〜。気をつけて帰ってきてね！:wink:"
                    if re.search(u"(.*疲れた.*|.*つかれた.*)", data["text"]) is not None:
                        return "<@" + data["user"] + "> " + u"大丈夫？無理しないでね。"
                    if re.search(u"(.*欠席.*)", data["text"]) is not None:
                        return "<@" + data["user"] + "> " + u"そうなんだー、会えるの楽しみにしていたのに残念:cry:" 
 
sbm = SlackBotMain()
