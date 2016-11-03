#coding=utf-8
# made by Salt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json
from Tkinter import *
#name = raw_input('LOL Name ?')

def getzhanli():
    name =  enter.get()
    a = requests.session()
    res = a.get('http://api.lolbox.duowan.com/api/v2/player/search/?player_name_list=%s&callback=jQuery111209546720427511086_1470496009407&_=1470496009408' %(name))
    html = res.text
    print type(html)
    html = html[html.index('{'):-1]
    dic = json.loads(html)
    print type(dic)
    player = dic[u'player_list']
    box.delete(0,END)
    for i in player:
        #print "Thanks for your support :)"
        a = '服务器:%s       区域:%s' %(i['game_zone']['alias'],i['game_zone']['server_name'])
        #print a
        b = '段位:%s %s      战力:%s' %(i['tier_rank']['tier']['full_name_cn'],i['tier_rank']['rank']['name'],i['box_score'])
        #print b
        box.insert(END,'Thanks for your support :)')
        box.insert(END,a)
        box.insert(END,b)
def check():
    name =  enter.get()
    if name == "":
        box.insert(END,'Thanks for your support :) \n\r 请输入召唤师名称 ！')
    else:
        getzhanli()
        
window = Tk()
window.geometry('600x400')

title = window.title('LOL战力查询      _by Salt')
#e = StringVar()
#e.set('召唤师名称')
enter = Entry(window,width = 50)
enter.pack()

butt = Button(window,text='战力查询',command = check ,width = 25)
butt.pack()

box = Listbox(window,width = 75,height = 50)
box.pack()

enter.focus()
window.mainloop()
