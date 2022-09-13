from xml.dom import minidom
import uiautomator2 as u2
from time import sleep
from os import system
from xml.etree.ElementTree import parse
from xml.dom.minidom import parseString
import os
from  compare import compare
d = u2.connect("192.168.185.103:5555")
xml = d.dump_hierarchy()#获取XML元素
#获取XML中所有元素
#dom = minidom.parse(r"C:\Users\26947\AndroidStudioProjects\EspressoTest\app\src\main\res\layout\activity_second.xml")
dom = parseString(xml)
print(xml)
list = []
testSuiteNodeListA = dom.firstChild
print (testSuiteNodeListA.nodeName)
#list.append({"children":[],"name": testSuiteNodeListA.nodeName},)
def searchId(testSuiteNodeList):
    if type(testSuiteNodeList) == minidom.Element:
        if testSuiteNodeList.firstChild:
            for ts_node in testSuiteNodeList.childNodes:
                searchId(ts_node)
        else:
            if 'clickable' in (testSuiteNodeList.attributes.keys()) and 'long-clickable' in (testSuiteNodeList.attributes.keys()):
                if (testSuiteNodeList.attributes['clickable'].value) or (testSuiteNodeList.attributes['long-clickable'].value):
                    list.append({testSuiteNodeList.attributes['resource-id'].value})

for ts_node in testSuiteNodeListA.childNodes:
    searchId(ts_node)
list2=[]
print(list)
# for i in range(len(list)):
#         if list[i]!={''} and list[i]!={'com.android.systemui:id/wifi_signal_dark'}and list[i]!={'com.android.systemui:id/mobile_signal_dark'}and list[i]!={'com.android.systemui:id/battery'}and list[i]!={'com.android.systemui:id/clock'}and list[i]!={'com.android.systemui:id/scrim_behind'} and list[i]!={'com.android.systemui:id/scrim_in_front'}\
#                 and list[i]!={'com.android.systemui:id/wifi_signal'}and list[i]!='com.android.systemui:id/mobile_signal'and list[i]!={'com.android.systemui:id/mobile_signal'}and list[i]!={'com.android.systemui:id/notificationIcons'}:
#             str1=str(list[i])
#             print(str1[2:-2])
#             print('测试')
#             #sleep(5)
#             d(resourceId=(str1[2:-2])).click()
#          #d(resourceId=str1[1:-1]).click()
#             sleep(2)
#             n = d.dump_hierarchy()
#             if compare(xml,xml2):#判断是否点击按钮后界面发生变化
#                 d.press("back")
#                 sleep(2)
#             else:
#                 sleep(2)
        # d.press("back")`
        # sleep(3)
# d(resourceId='com.android.systemui:id/wifi_signal_dark').click()
# d.press('back')
#d(resourceId='com.android.systemui:id/wifi_signal_dark').click()
for i in range(len(list)):
            if list[i]!={''} and list[i]!={'com.android.systemui:id/wifi_signal_dark'}and list[i]!={'com.android.systemui:id/mobile_signal_dark'}and list[i]!={'com.android.systemui:id/battery'}and list[i]!={'com.android.systemui:id/clock'}and list[i]!={'com.android.systemui:id/scrim_behind'} and list[i]!={'com.android.systemui:id/scrim_in_front'}\
                and list[i]!={'com.android.systemui:id/wifi_signal'}and list[i]!='com.android.systemui:id/mobile_signal'and list[i]!={'com.android.systemui:id/mobile_signal'}and list[i]!={'com.android.systemui:id/notificationIcons'}:
                str1=str(list[i])
                print(str1[2:-2])
                print('测试')
            #sleep(5)
                d(resourceId=(str1[2:-2])).click()
         #d(resourceId=str1[1:-1]).click()
                sleep(1)
                xml2 = d.dump_hierarchy()
                if compare(xml,xml2):#判断是否点击按钮后界面发生变化
                #如果发生变化~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    #tag = tag + 1
                    d.press("back")

                    sleep(1)
                else:
                    sleep(1)