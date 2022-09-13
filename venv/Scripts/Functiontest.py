import uiautomator2 as u2
from time import sleep
from os import system

d = u2.connect("192.168.185.103:5555")
xml = d.dump_hierarchy()
print(xml)
def login():#完成网易云音乐的登陆
    d(resourceId="com.netease.cloudmusic:id/pa").click()#打开菜单
    d(resourceId="com.netease.cloudmusic:id/af7").click()#打开登陆界面
    d(resourceId="com.netease.cloudmusic:id/p0").click()#打开登陆界面
    print("登陆成功")
login()
#def login():
#主要测试
# ifd()
# d(resourceId="com.netease.cloudmusic:id/bhz").click()
# com.netease.cloudmusic:id/bhz
# if d(resourceId="com.netease.cloudmusic:id/bhz").gettext()=="暂停成功"
#     login()