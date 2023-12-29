#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: 钉钉或微信pythontesting 钉钉群21734177 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21
import datetime
from collections import OrderedDict
from bidict import bidict

import sxtwl

Gan = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]

Zhi = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]

datouxiu = ("壬子", "癸丑", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉")

xiaotouxiu = ("壬午", "癸未", "庚子", "辛丑", "戊子", "己丑")

temps = {"甲":3, "乙":1, "丙":6, "丁":4, "戊":5, "己":-4, "庚":-1, "辛":-3, "壬":-5, "癸":-6,"子":-6, "丑":-4, "寅":3, "卯":1, "辰":-4, 
            "巳":5, "午":6, "未":3, "申":-2, "酉":-3,"戌":4, "亥":-5}


zhi_time = {"子":'23-1', "丑":'1-3', "寅":'3-5', "卯":'5-7', "辰":'7-9', 
            "巳":'9-11', "午":'11-13', "未":'13-15', "申":'15-17', "酉":'17-19',
            "戌":'19-21', "亥":'21-23'}

zhengs = "子午卯酉"

wuhangs = {
    '金':"庚辛申酉",
    '木':"甲乙寅卯",    
    '水':"壬癸子亥",
    '火':"丙丁巳午",     
    '土':"戊己丑辰未戌",         
}

ganzhi60 = bidict({
    1:"甲子", 13:"丙子", 25:"戊子", 37:"庚子", 49:"壬子", 2:"乙丑", 14:"丁丑", 26:"己丑", 38:"辛丑", 50:"癸丑", 
    3:"丙寅", 15:"戊寅", 27:"庚寅", 39:"壬寅", 51:"甲寅", 4:"丁卯", 16:"己卯", 28:"辛卯", 40:"癸卯", 52:"乙卯", 
    5:"戊辰", 17:"庚辰", 29:"壬辰", 41:"甲辰", 53:"丙辰", 6:"己巳", 18:"辛巳", 30:"癸巳", 42:"乙巳", 54:"丁巳", 
    7:"庚午", 19:"壬午", 31:"甲午", 43:"丙午", 55:"戊午", 8:"辛未", 20:"癸未", 32:"乙未", 44:"丁未", 56:"己未", 
    9:"壬申", 21:"甲申", 33:"丙申", 45:"戊申", 57:"庚申", 10:"癸酉", 22:"乙酉", 34:"丁酉", 46:"己酉", 58:"辛酉", 
    11:"甲戌", 23:"丙戌", 35:"戊戌", 47:"庚戌", 59:"壬戌", 12:"乙亥", 24:"丁亥", 36:"己亥", 48:"辛亥", 60:"癸亥"})


zhi5 = {
    "子":OrderedDict({"癸":8}), 
    "丑":OrderedDict({"己":5, "癸":2, "辛":1,}), 
    "寅":OrderedDict({"甲":5, "丙":2, "戊":1, }),
    "卯":OrderedDict({"乙":8}),
    "辰":OrderedDict({"戊":5, "乙":2, "癸":1, }),
    "巳":OrderedDict({ "丙":5, "戊":2, "庚":1,}),
    "午":OrderedDict({"丁":5, "己":3, }),
    "未":OrderedDict({"己":5, "丁":2, "乙":1,}),
    "申":OrderedDict({"庚":5, "壬":2, "戊":1, }),
    "酉":OrderedDict({"辛":8}),
    "戌":OrderedDict({"戊":5, "辛":2, "丁":1 }),
    "亥":OrderedDict({"壬":5, "甲":3, })}

ShX = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
numCn = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"]
Week = ["日", "一", "二", "三", "四", "五", "六"]
jqmc = ["冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑","白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪"]
jis = {0:'冬', 1:'春', 2:'夏', 3:'秋', 4:'冬'}
ymc = ["十一", "十二", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十" ]
rmc = ["初一", "初二", "初三", "初四", "初五", "初六", "初七", "初八", "初九", "初十", "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十", "廿一", "廿二", "廿三", "廿四", "廿五", "廿六", "廿七", "廿八", "廿九", "三十", "卅一"]


ten_deities = {
    '甲':bidict({'甲':'比', "乙":'劫', "丙":'食', "丁":'伤', "戊":'才',
                  "己":'财', "庚":'杀', "辛":'官', "壬":'枭', "癸":'印', "子":'沐', 
                  "丑":'冠', "寅":'建', "卯":'帝', "辰":'衰', "巳":'病', "午":'死', 
                  "未":'墓', "申":'绝', "酉":'胎', "戌":'养', "亥":'长', '库':'未_', 
                  '本':'木', '克':'土', '被克':'金', '生我':'水', '生':'火','合':'己','冲':'庚'}),
    '乙':bidict({'甲':'劫', "乙":'比', "丙":'伤', "丁":'食', "戊":'财',
                  "己":'才', "庚":'官', "辛":'杀', "壬":'印',"癸":'枭', "子":'病', 
                  "丑":'衰', "寅":'帝', "卯":'建', "辰":'冠', "巳":'沐', "午":'长',
                  "未":'养', "申":'胎', "酉":'绝', "戌":'墓', "亥":'死', '库':'未_',
                  '本':'木', '克':'土', '被克':'金', '生我':'水', '生':'火','合':'庚','冲':'辛'}),
    '丙':bidict({'丙':'比', "丁":'劫', "戊":'食', "己":'伤', "庚":'才',
                  "辛":'财', "壬":'杀', "癸":'官', "甲":'枭', "乙":'印',"子":'胎', 
                  "丑":'养', "寅":'长', "卯":'沐', "辰":'冠', "巳":'建', "午":'帝',
                  "未":'衰', "申":'病', "酉":'死', "戌":'墓', "亥":'绝', '库':'戌_',
                  '本':'火', '克':'金', '被克':'水', '生我':'木', '生':'土','合':'辛','冲':'壬'}),
    '丁':bidict({'丙':'劫', "丁":'比', "戊":'伤', "己":'食', "庚":'财',
                  "辛":'才', "壬":'官', "癸":'杀', "甲":'印',"乙":'枭', "子":'绝', 
                  "丑":'墓', "寅":'死', "卯":'病', "辰":'衰', "巳":'帝', "午":'建',
                  "未":'冠', "申":'沐', "酉":'长', "戌":'养', "亥":'胎', '库':'戌_',
                  '本':'火', '克':'金', '被克':'水', '生我':'木', '生':'土','合':'壬','冲':'癸'}),
    '戊':bidict({'戊':'比', "己":'劫', "庚":'食', "辛":'伤', "壬":'才',
                  "癸":'财', "甲":'杀', "乙":'官', "丙":'枭', "丁":'印',"子":'胎', 
                  "丑":'养', "寅":'长', "卯":'沐', "辰":'冠', "巳":'建', "午":'帝',
                  "未":'衰', "申":'病', "酉":'死', "戌":'墓', "亥":'绝', '库':'辰_',
                  '本':'土', '克':'水', '被克':'木', '生我':'火', '生':'金','合':'癸','冲':''}),
    '己':bidict({'戊':'劫', "己":'比', "庚":'伤', "辛":'食', "壬":'财',
                  "癸":'才', "甲":'官', "乙":'杀', "丙":'印',"丁":'枭',"子":'绝', 
                  "丑":'墓', "寅":'死', "卯":'病', "辰":'衰', "巳":'帝', "午":'建',
                  "未":'冠', "申":'沐', "酉":'长', "戌":'养', "亥":'胎', '库':'辰_',
                  '本':'土', '克':'水', '被克':'木', '生我':'火', '生':'金','合':'甲','冲':''}),
    '庚':bidict({'庚':'比', "辛":'劫', "壬":'食', "癸":'伤', "甲":'才',
                  "乙":'财', "丙":'杀', "丁":'官', "戊":'枭', "己":'印',"子":'死', 
                  "丑":'墓', "寅":'绝', "卯":'胎', "辰":'养', "巳":'长', "午":'沐',
                  "未":'冠', "申":'建', "酉":'帝', "戌":'衰', "亥":'病', '库':'丑_',
                  '本':'金', '克':'木', '被克':'火', '生我':'土', '生':'水','合':'乙','冲':'甲'}), 
    '辛':bidict({'庚':'劫', "辛":'比', "壬":'伤', "癸":'食', "甲":'财',
                  "乙":'才', "丙":'官', "丁":'杀', "戊":'印', "己":'枭', "子":'长', 
                  "丑":'养', "寅":'胎', "卯":'绝', "辰":'墓', "巳":'死', "午":'病',
                  "未":'衰', "申":'帝', "酉":'建', "戌":'冠', "亥":'沐', '库':'丑_',
                  '本':'金', '克':'木', '被克':'火', '生我':'土', '生':'水','合':'丙','冲':'乙'}),
    '壬':bidict({'壬':'比', "癸":'劫', "甲":'食', "乙":'伤', "丙":'才',
                  "丁":'财', "戊":'杀', "己":'官', "庚":'枭', "辛":'印',"子":'帝', 
                  "丑":'衰', "寅":'病', "卯":'死', "辰":'墓', "巳":'绝', "午":'胎',
                  "未":'养', "申":'长', "酉":'沐', "戌":'冠', "亥":'建', '库':'辰_',
                  '本':'水', '克':'火', '被克':'土', '生我':'金', '生':'木','合':'丁','冲':'丙'}),
    '癸':bidict({'壬':'劫', "癸":'比', "甲":'伤', "乙":'食', "丙":'财',
                  "丁":'才', "戊":'官', "己":'杀', "庚":'印',"辛":'枭', "子":'建', 
                  "丑":'冠', "寅":'沐', "卯":'长', "辰":'养', "巳":'胎', "午":'绝',
                  "未":'墓', "申":'死', "酉":'病', "戌":'衰', "亥":'帝', '库':'辰_',
                  '本':'水', '克':'火', '被克':'土', '生我':'金', '生':'木','合':'戊','冲':'丁'}), 

}

ju = {
    '本':'刃', '被克':'杀',  '克':'才', '生':'伤', '生我':'枭',
}

shengxiaos = bidict({
    "子":"鼠", "丑":"牛", "寅":"虎", "卯":"兔", "辰":"龙", "巳":"蛇", 
    "午":"马", "未":"羊", "申":"猴", "酉":"鸡", "戌":"狗", "亥":"猪"})


zhi_atts = {
    "子":{"冲":"午", "刑":"卯", "被刑":"卯", "合":("申","辰"), "会":("亥","丑"), '害':'未', '破':'酉', "六":"丑","暗":"",},
    "丑":{"冲":"未", "刑":"戌", "被刑":"未", "合":("巳","酉"), "会":("子","亥"), '害':'午', '破':'辰', "六":"子","暗":"寅",},
    "寅":{"冲":"申", "刑":"巳", "被刑":"申", "合":("午","戌"), "会":("卯","辰"), '害':'巳', '破':'亥', "六":"亥","暗":"丑",},
    "卯":{"冲":"酉", "刑":"子", "被刑":"子", "合":("未","亥"), "会":("寅","辰"), '害':'辰', '破':'午', "六":"戌","暗":"申",},
    "辰":{"冲":"戌", "刑":"辰", "被刑":"辰", "合":("子","申"), "会":("寅","卯"), '害':'卯', '破':'丑', "六":"酉","暗":"",},
    "巳":{"冲":"亥", "刑":"申", "被刑":"寅", "合":("酉","丑"), "会":("午","未"), '害':'寅', '破':'申', "六":"申","暗":"",},
    "午":{"冲":"子", "刑":"午", "被刑":"午", "合":("寅","戌"), "会":("巳","未"), '害':'丑', '破':'卯', "六":"未","暗":"亥",},
    "未":{"冲":"丑", "刑":"丑", "被刑":"戌", "合":("卯","亥"), "会":("巳","午"), '害':'子', '破':'戌', "六":"午","暗":"",},
    "申":{"冲":"寅", "刑":"寅", "被刑":"巳", "合":("子","辰"), "会":("酉","戌"), '害':'亥', '破':'巳', "六":"巳","暗":"卯",},
    "酉":{"冲":"卯", "刑":"酉", "被刑":"酉", "合":("巳","丑"), "会":("申","戌"), '害':'戌', '破':'子', "六":"辰","暗":"",},
    "戌":{"冲":"辰", "刑":"未", "被刑":"丑", "合":("午","寅"), "会":("申","酉"), '害':'酉', '破':'未', "六":"卯","暗":"",},
    "亥":{"冲":"巳", "刑":"亥", "被刑":"亥", "合":("卯","未"), "会":("子","丑"), '害':'申', '破':'寅', "六":"寅","暗":"午",},
}




kus = {'辰':"水土", '戌':'火土', '丑':'金', '未':'木',}

gan_hes = {
    ("甲", "己"): "中正之合 化土 尊崇重大,宽厚平直。如带煞而五行无气则多嗔好怒,性梗不可屈",
    ("乙", "庚"): '''仁义之合　化金 果敢有守, 不惑柔佞,周旋唯仁,进退唯义。''',
    ("丙", "辛"): '''威制之合　化水 ''',
    ("丁", "壬"): '''淫慝之合　化木 ''',    
    ("戊", "癸"): '''无情之合　化火''',    
}

gan_chongs = {("甲", "庚"): "相冲",   ("乙", "辛"): "相冲",
              ("丙", "壬"): "相冲", ("丁", "癸"): "相冲",}    

chongs = { 
    "甲":"庚", "庚":"甲","乙":"辛", "辛":"乙","丙":"壬", "壬":"丙", "丁":"癸",
    "癸":"丁", "子":"午", "午":"子", "丑":"未", "未":"丑", "寅":"申",  "申":"寅", 
    "卯":"酉",  "酉":"卯", "辰":"戌", "戌":"辰", "巳":"亥", "亥":"巳"
}


zhi_6hes = {
    "子丑": "土",
    "寅亥": "木",
    "卯戌": "火",
    "酉辰": "金",    
    "申巳": "水",    
    "未午": "土",        
}

zhi_3hes = {"申子辰": "水 寅","巳酉丑": "金 亥",  "寅午戌": "火 申", "亥卯未": "木 巳"}
gong_he = {"申辰": '子', "巳丑": '酉', "寅戌": '午', "亥未": '卯',
           "辰申": '子', "丑巳": '酉', "戌寅": '午', "未亥": '卯',}

zhi_half_3hes = {
    ("申", "子"): "化水  马在寅",
    ("子", "辰"): "化水  马在寅",
    ("申", "辰"): "化水  马在寅",    
    ("巳", "酉"): "化金 马在亥",  
    ("酉", "丑"): "化金 马在亥",  
    ("巳", "丑"): "化金 马在亥",      
    ("寅", "午"): "化火 马在申",    
    ("午", "戌"): "化火 马在申",   
    ("寅", "戌"): "化火 马在申",   
    ("亥", "卯"): "化木 马在巳",
    ("亥","未"): "化木 马在巳",
    ( "卯", "未"): "化木 马在巳",
}

zhi_hes = {
    "申子辰": "水",
    "巳酉丑": "金",  
    "寅午戌": "火", 
    "亥卯未": "木"
}

zhi_huis = {
    "亥子丑": "水",
    "寅卯辰": "木",  
    "巳午未": "火",       
    "申酉戌": "金",
}
gong_hui = {"亥丑": '子', "寅辰": '卯', "巳未": '午', "申戌": '酉',
           "丑亥": '子', "辰寅": '卯', "未巳": '午', "戌申": '酉',}

zhi_chongs = {
    ("子", "午"): "相冲",
    ("丑", "未"): "相冲",
    ("寅", "申"): "相冲",
    ("卯", "酉"): "相冲",
    ("辰", "戌"): "相冲",   
    ("巳", "亥"): "相冲",       
}

zhi_poes = {
    ("子", "酉"): "相破",
    ("午", "卯"): "相破",
    #("巳", "申"): "相破", 
    #("寅", "亥"): "相破",
    ("辰", "丑"): "相破",   
    ("戌", "未"): "相破",       
}

zhi_haies = {
    ("子", "未"): '''
    未害子 谓未旺土，亥子旺水，名势家相害。故子见未则为害。
    不利六亲骨肉。入贵格多妻妾之累,入贱格孤独无倚。''',
    ("丑", "午"): '''
    午害丑 谓午以旺火凌丑死金，名官鬼相害。故丑见午，而午更带丑干之真鬼则为害尤甚。 
    生旺,主好胜多怒,严毅不忍;死绝主毒害、伤惨、倾覆之事。入贵格 则主大权,司刑典狱;
    入贱格则谋生于不义之地。''',
    ("寅", "巳"): '''
    互相相害 生旺则主神洁貌俊,好争夺,喜激作;值死绝则多谋少成,强学人做事,兀兀趋进不厌。
    入贵格则有操守, 善机权;入贱格则多诈、爱贫、鄙吝。''',
    ("卯", "辰"): '''
    卯害辰 谓卯以旺木凌辰死土，此以少凌长相害。故辰见卯，而卯更带辰干真鬼则其害尤甚。 
    生旺,主好胜多怒,严毅不忍;死绝主毒害、伤惨、倾覆之事。入贵格 则主大权,司刑典狱;
    入贱格则谋生于不义之地。''',
    ("申", "亥"): '''
    互相相害 谓名恃临官，竞嫉才能，争进相害。故申见亥，亥见申均为害，更纳音相克者重。 
    生旺则主神洁貌俊,好争夺,喜激作;值死绝则多谋少成,强学人做事,兀兀趋进不厌。
    入贵格则有操守, 善机权;入贱格则多诈、爱贫、鄙吝。''',   
    ("酉", "戌"): '''
    戌害酉 戌以死火害酉旺金，此嫉妒相害，故酉人见戌则凶，戌人见酉无灾；
    若乙酉人得戊戌，乙为真金，戊为真火，为害尤甚。 生旺,不容物,多刚戾;死绝酷狠,憎善妒能。
    入贵格 罗怯无辜,结构入讼,颇多奸佞,入贱格残害、阴狡、性佞、 不良。''',       
}

zhi_xings = {
    ("寅", "巳"): "寅刑巳 无恩之刑 ",
    ("巳", "申"): "巳刑申 无恩之刑",
    ("申", "寅"): "申刑寅 无恩之刑",
    ("未", "丑"): "未刑丑 持势之刑",
    ("丑", "戌"): "丑刑戌 持势之刑",   
    ("戌", "未"): "戌刑未 持势之刑",  
    ("子", "卯"): "子刑卯　卯刑子 无礼之刑 女命见之，尤为不良 生旺主人威肃，面无和气，气强性暴，太察不容；死绝则侮慢忽略，狭劣刻剥，少孝悌，害妻子，吴越六亲。入贵格则多掌兵权，不利近侍；位居不久；入贱格则悖凶暴，多招刑祸。",       
}

xings = {"巳":"寅", "申":"巳",  "寅":"申", "丑":"未", "戌":"丑", "未":"戌",
         "子":"卯", "卯":"子", '辰':'辰', '午':'午','酉':'酉', '亥':'亥'}

zhi_zixings = ['辰', '午', '酉', '亥']



gan5 = {"甲":"木", "乙":"木", "丙":"火", "丁":"火", "戊":"土", "己":"土", 
        "庚":"金", "辛":"金", "壬":"水", "癸":"水"}

zhi_wuhangs = {"子":"水", "丑":"土", "寅":"木", "卯":"木", "辰":"土", "巳":"火", 
        "午":"火", "未":"土", "申":"金", "酉":"金", "戌":"土", "亥":"水"}

relations = {
    ("金", "金"): '=', ("金", "木"): '→', ("金", "水"): '↓', ("金", "火"): '←', ("金", "土"): '↑',
    ("木", "木"): '=', ("木", "土"): '→', ("木", "火"): '↓', ("木", "金"): '←', ("木", "水"): '↑',
    ("水", "水"): '=', ("水", "火"): '→', ("水", "木"): '↓', ("水", "土"): '←', ("水", "金"): '↑',    
    ("火", "火"): '=', ("火", "金"): '→', ("火", "土"): '↓', ("火", "水"): '←', ("火", "木"): '↑',
    ("土", "土"): '=', ("土", "水"): '→', ("土", "金"): '↓', ("土", "木"): '←', ("土", "火"): '↑',

}

guans = {
    "甲":('辛',"酉","戌","丑"), "乙":('庚',"申",'巳'), "丙":("癸",'丑','辰'), 
    "丁":('壬',"亥", '申'),"戊":('乙',"卯","戌","未"), "己":('甲',"寅", "亥"), 
    "庚":('丁',"午", "戌","未"), "辛":('丙',"寅",'巳'),
    "壬":('己',"午",'未','丑'), "癸":('戊',"寅","辰",'巳','申','戌'),}


gan_desc = {
    "甲":'''雷龙 梁栋 禄寅;斧斤斫削成其器。木不南奔;喜春运不喜西方,春生,处世安然,必寿。''', 
    "乙":'''风 树 禄卯 水泛木浮  秋令大吉''', 
    "丙":"电 冶 禄巳 火无西向", 
    "丁":"星 灯 禄午 火明则灭 喜遇秋. 丁巳日,多克父兄妻子,财忌比劫,兄屈弟下,巳有戊土,伤",
    "戊":"雾霞 山 禄巳 土虚则崩 四柱带水则为上格,霞水相辉而成文彩也;年月干见癸雨后霞现", 
    "己":"元气云 真土 禄午 火燥土裂  天降时雨,山川出云 贵坐酉,贵春生,贵见印,坐亥者不可见乙木,云升天,遇风则狼籍", 
    "庚":"月 铁 禄申 畏癸水 巳成钟鼎 水土沉埋则无声 金实无声 金沉水底 四柱有乙巳,月白风清, 秋上,冬次,春夏无取。",
    "辛":"霜 金 禄酉 土重金埋 辛人坐卯,未透乙, 大富,坐亥透丙则贵。爱冬生。", 
    "壬":"秋露云 泽 禄亥 死水横流", 
    "癸":"雨 泉脉 春霖 禄子 水不西流 癸卯日透己, 有云行雨有经济才也。春夏吉,秋冬不吉"}

zhi_desc = {
    "子":"墨池 正北 时喜见癸亥，谓之水归大海，又谓之双鱼游墨，必为文章士矣。",
    "丑":"柳岸 丑人时见己未，乃月照柳梢，极为上格",
    "寅":"广谷 寅生人而时戊辰者，谓之虎啸而谷风生 威震万里",
    "卯":"琼林 乙木 正东 仲春 卯年遇巳未时者，是为兔入月宫之象，主大贵。",
    "辰":"草泽 东方之次 辰逢壬戍、癸亥即龙归大海格",
    "巳":"大驿 巳生喜得辰时，蛇化轻龙，于格为千里龙驹",
    "午": "烽堠 南 属火、土，其色赤黄 时利见辰，真龙出则凡马空矣，谓之马化龙驹。",
    "未": "花园 卯乃木旺,自 成林麓;未乃木库,如人筑墙垣以护百花也,以百花言未中有 杂气耳;未年人双飞格,最妙,如辛未见戊戍,两干不杂是也。 ",
    "申":"名都 帝王所居；申宫壬水生 亥时，乃地天交泰",
    "酉":"寺钟 正西 见寅吉，谓之钟鸣谷应。",
    "戌": "烧原 戌与辰地皆贵人所不临也 戌生逢卯 春入烧痕",
    "亥":"悬河 即天门 日时见寅、辰二字，是乃水拱雷门",    
}

gan3 = {
    "甲":'天上贵，孤独守空房', 
    "乙":'多阴私，又要败祖业', 
    "丙":'人孤老，产中亡', 
    "丁":"多恶疾，手足也自伤",
    "戊":"子随出，离祖别家乡", 
    "己":"别父母，兄弟各一方", 
    "庚":"财郎，万里置田庄",
    "辛":"寿数长，财滞多灾郎", 
    "壬":"家业盛，有富不久长", 
    "癸":"一亥全，烈火烧屋房"}

gan4 = {
    "甲":'少夫妻', 
    "乙":'命早亡', 
    "丙":'子息空', 
    "丁":"寿不长",
    "戊":"人孤刑", 
    "己":"人忠良", 
    "庚":"他乡走",
    "辛":"寿限长", 
    "壬":"定富足", 
    "癸":"人夭亡"}


zhi3 = {
    "子":"婚事重",
    "丑":"四夫妻",
    "寅":"守孤寡",
    "卯":"凶恶多",
    "辰":"好斗伤",
    "巳":"遭刑害",
    "午": "克夫妻",
    "未": "守空房 ",
    "申":"人不足",
    "酉":"独居房",
    "戌": "讼事多",
    "亥":"孤苦怜", }


def getGZ(gzStr):
    tg = -1
    dz = -1
    for i, v in enumerate(Gan):
        if gzStr[0]  == v:
            tg = i
            break

    for i, v in enumerate(Zhi):
        if  gzStr[1] == v:
            dz = i
            break   
    return sxtwl.GZ(tg, dz)

def get_jizhu(gan, zhi):
    
    gan_index = Gan.index(gan)
    zhi_index = Zhi.index(zhi) 
    result = {}
    alls = []
    for i in range(6):
        ganzhi = "{}{}".format(Gan[(gan_index-6-i*9 )%10], Zhi[(zhi_index-6-i*9)%12])
        result[ganzhi] = get_year_of_ganzhi(ganzhi)
        alls += result[ganzhi]
    alls.sort()
    result['all'] = alls
    return result

def get_year_of_ganzhi(ganzhi):
    
    seq = ganzhi60.inverse[ganzhi]
    year = 1983 + seq
    current_year = get_current_year()
    result = [year - 60]
    if year <=  current_year:
        result.append(year)
    return result  

def get_current_year():
    
    current_date = datetime.date.today()
    return current_date.year

gan_health = {
    "金":'''
    秋天较走运
    申月、酉月、猴年和鸡年运气较好
    下午三点至下午七点是吉时
    
    西方是吉方
    住朝西的房子较吉利
    睡房在房子的西方较好
    睡房的西方有窗字较顺利
    金属床有利健康
    办公桌朝西有助工作效率
    吉祥颜色是白色
    室内装璜用白色系统
    穿衣用白色系列
    开白色车子较平安易发财
    勿伤心，注意呼吸系统、肺、肠, 筋
    武术、击搏、兵器运动、健身房运动也很好
    和金有关的工作较容易''',
                                     
    "木":'''
    春天或清风徐来的天气较走运
    卯月、寅月、兔年和虎年运气较好
    上午三点至上午七点是吉时
    东方是吉方
    住朝东的房子较吉利
    睡房在房子的东方较好
    睡房的东方有窗字较顺利
    木床有利健康
    办公桌朝东有助工作效率
    吉祥颜色是绿色
    室内装璜用绿色系统
    穿衣用绿色系列
    开绿色车子较平安易发财
    多喝点酸性饮料，忌生气，注意神精系统、肝、胆、头肩、肝胆
    多打高尔夫球、公园散步、徒步树林等户外运动
    和木有关的工作较容易。''',
                                        
    "水":'''
    身体需要注意: 胫足、膀胱肾(比如结石) 多喝水
    冬天或冷天气较走运
    亥月、子月、猪年和鼠年运气较好
    晚上九点至上午一点是吉时
    北方较冷是吉方
    住朝北的房子较吉利
    睡房在房子的北方较好
    睡房的北方有窗字较顺利
    金属床或水床有利健康
    办公桌朝北有助工作效率
    吉祥颜色是黑色
    室内装璜用黑色系统
    穿衣用黑色系列，带珠宝也不错
    开黑色车子较平安易发财
    多喝水，注意肾脏系统
    多做游泳、潜水、滑雪、钓鱼、溜冰等户外运动
    和水有关的工作较容易。''',    
                                        
    "火":'''
    夏天或热天气较走运
    午月、巳月、马年和蛇年运气较好
    上午九点至下午一点是吉时
    南方较热是吉方
    住朝南的房子较吉利
    睡房在房子的南方较好
    睡房的南方有窗字较顺利
    木床有利健康
    办公桌朝南有助工作效率
    吉祥颜色是红色
    室内装璜用红色系统
    穿衣用红色系列
    开红色车子较平安易发财
    要常笑，注意心脏系统、血液循环、眼睛、额齿
    多做打篮球、网球、排球、骑单车等户外运动
    和火有关的工作较容易''',
    
    "土":'''
    春、夏、秋、冬四季交接之时段较走运
    丑、辰、未、戌月和牛、龙、羊、狗年运气较好
    上午二点、八点左右和下午二点、八点左右都是吉时
    起居环境和气候不要太乾或太湿
    睡房在房子的中间较好
    办公桌靠房子的中间，有助工作效率
    吉祥颜色是棕黄色
    室内装璜用棕黄色系统
    穿衣用棕黄色系列，带古玉很不错
    开棕黄色车子较平安易发财
    勿常担心事情，太多虑 
    少吃些甜点，注意消化系统、脾、肌肉
    多做园艺、露营、走路等户外运动。下棋、宗教场所都好
    和土有关的工作较容易''',      
}

# 岁煞为三合对冲方的三会中的库，劫煞为三合对冲方的三会中的生
mu_years = { '灾煞': '酉', '坐煞': '庚辛','向煞': '甲乙','岁煞': '戌', '劫煞': '申',
    
}