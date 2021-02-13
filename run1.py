# coding:  utf8
'''

'''
import json


class message:
    def __init__(self, headstr, messtr):
        try:
            head = headstr.split(' ')
            self.data = head[0]  # 日期
            self.dayday = head[1]  # 上下午
            self.time = head[2]  # 时间
            self.name = head[-1].replace("\n", "")  # 名字
            self.mess = message.mestext(messtr)  # 消息文本
            self.right = True
        except:
            self.right = False

    @staticmethod
    def mestext(messtr):
        return messtr.replace(" ", "").replace("\n", "")

    def result(self):
        return (self.data, self.dayday, self.time, self.name, self.mess) if self.right == True else self.right


def readfile():
    your = []
    str4 = ""
    str5 = "\t"
    str6 = ""
    str6isstr3 = False

    def ishead(strr):
        lisss = strr.split(" ")
        if len(lisss) == 4 and lisss[0].find("202") > -1:
            return True
        else:
            return False

    while True:
        if str6isstr3 is False:
            str3 = file.readline()
        else:
            str3 = str6
            str6isstr3 = False
        if ishead(str3):
            while True:
                str5 = file.readline()
                if str5 == "":
                    break
                if ishead(str5) is False:
                    str4 += str5
                else:
                    str6 = str5
                    str6isstr3 = True
                    break
            your.append(message(str3, str4).result())
            str4 = ""
            continue
        if str5 == "":
            break
    return your


filepath = r"4405.txt"  # QQ聊天文件导出路径

file = open(filepath, encoding='utf8')
your = {"data": readfile()}

with open('chat_records.json', 'a', encoding='utf-8') as f:
    f.write(json.dumps(your, ensure_ascii=False) + '\n')
