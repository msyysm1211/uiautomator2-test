from xml.dom import minidom
import uiautomator2 as u2
from time import sleep
from os import system
from xml.etree.ElementTree import parse
from xml.dom.minidom import parseString
from sourceid import getsourceid,searchId
from compare import compare
import os
d = u2.connect("192.168.185.103:5555")
xml = d.dump_hierarchy()#获取XML元素
list2=[]
list=getsourceid(xml,list2)
print(list)
for i in range(len(list)):
        if list[i]!={''} and list[i]!={'com.android.systemui:id/wifi_signal_dark'}and list[i]!={'com.android.systemui:id/mobile_signal_dark'}and list[i]!={'com.android.systemui:id/battery'}and list[i]!={'com.android.systemui:id/clock'}and list[i]!={'com.android.systemui:id/scrim_behind'} and list[i]!={'com.android.systemui:id/scrim_in_front'}\
                and list[i]!={'com.android.systemui:id/wifi_signal'}and list[i]!='com.android.systemui:id/mobile_signal'and list[i]!={'com.android.systemui:id/mobile_signal'}and list[i]!={'com.android.systemui:id/notificationIcons'}:
            str1=str(list[i])
            print(str1[2:-2])
            print('测试')
            #sleep(5)
            d(resourceId=(str1[2:-2])).click()
         #d(resourceId=str1[1:-1]).click()
            sleep(2)
            xml2 = d.dump_hierarchy()
            if compare(xml,xml2):#判断是否点击按钮后界面发生变化
                d.press("back")
                sleep(2)
            else:
                sleep(2)
