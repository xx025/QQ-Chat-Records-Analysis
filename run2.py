import json
import pyecharts.options as opts
from pyecharts.charts import Line
from sorted import sortDictByKey, rankDate
import hanlp
from LAC import LAC
from numpy import sort


# 装载分词模型
lac = LAC(mode='seg')

with open('chat_records.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)['data']

ids = {'': '系统',
       '系统消息(10000)': '系统',
       '对方备注': '1111',
       '你的昵称': '2222'}

""" 如果你或者对方出现了多个昵称或备注
请将所有的备注和昵称写进字典，
并保证同一个人昵称对于的值相
同不同人之间不同 """


# 每日聊天字数统计
def day_word_count():
    ddata = []
    kait = dict()
    wordCount = []
    for i in json_data:  #
        if i[0] not in ddata:
            ddata.append(i[0])
    for i in json_data:
        if ids[i[3]] not in kait:
            kait[ids[i[3]]] = dict()
            for k in ddata:
                kait[ids[i[3]]][k] = 0
        kait[ids[i[3]]][i[0]] += len(i[4])
    ddata = sort(ddata)
    for i in ddata:
        wordCount.append([i, [kait[k][i]
                              for k in [i for i, j in kait.items()]]])
    c = (
        Line()
        .add_xaxis([i[0] for i in wordCount])
        .add_yaxis("A", [i[1][0] for i in wordCount])
        .add_yaxis("B", [i[1][1] for i in wordCount])
        .add_yaxis("C", [i[1][2] for i in wordCount])
        .set_global_opts(title_opts=opts.TitleOpts(title=""), datazoom_opts=opts.DataZoomOpts(type_="slider"))
        .render("line_.html")
    )


# day_word_count()


def basecount():
    kait = dict()
    ccot = dict()
    for i in json_data:
        if ids[i[3]] not in kait:
            kait[ids[i[3]]] = []
        kait[ids[i[3]]].append(i[4])
    for i in kait.items():
        ccot[i[0]] = (len(i[1]), len("".join(i[1])), ",".join(i[1]))
    return ccot


def cutwords(*ty):
    # seg_list = jieba.lcut("我来到北京清华大学", cut_all=False)  # 精确模式分割
    # 单个样本输入，输入为Unicode编码的字符串
    # text = u"LAC是个优秀的分词工具"
    # seg_result = lac.run(text)
    # return countwords(ty[0], jieba.lcut(ty[1]))
    return countwords(ty[0], lac.run(ty[1]))


def countwords(*ty):
    newdict = dict()
    for i in ty[1]:
        if i not in newdict:
            newdict[i] = ty[1].count(i)
        else:
            continue
    return sorted(newdict.items(), key=lambda x: x[1], reverse=True)


sler = basecount()
# 简单的分词没什么意义，大概需要更高级的表现方式
for i in sler.items():
    newlist = cutwords(i[0], i[1][2])
    print("=========================================")
    for i in newlist:
        print(i)
