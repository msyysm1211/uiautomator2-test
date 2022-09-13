from xml.dom import minidom
import uiautomator2 as u2
from time import sleep
from os import system
from xml.etree.ElementTree import parse
from xml.dom.minidom import parseString
import os
d = u2.connect("192.168.185.103:5555")
xml = d.dump_hierarchy()#获取XML元素
#获取XML中所有元素
#dom = minidom.parse(r"C:\Users\26947\AndroidStudioProjects\EspressoTest\app\src\main\res\layout\activity_second.xml")
dom = parseString(xml)
list = []
testSuiteNodeListA = dom.firstChild
print (testSuiteNodeListA.nodeName)
list.append({"children":[],"name": testSuiteNodeListA.nodeName},)
def searchId(testSuiteNodeList):
    if type(testSuiteNodeList) == minidom.Element:
        if testSuiteNodeList.firstChild:
            for ts_node in testSuiteNodeList.childNodes:
                searchId(ts_node)
        else:
            if 'clickable' in (testSuiteNodeList.attributes.keys()) and 'long-clickable' in (testSuiteNodeList.attributes.keys()):
                if (testSuiteNodeList.attributes['clickable'].value) or (testSuiteNodeList.attributes['long-clickable'].value):
                    list[0]["children"].append({"name": testSuiteNodeList.attributes['resource-id'].value})

for ts_node in testSuiteNodeListA.childNodes:
    searchId(ts_node)
print (list)
print (list[0][0])
