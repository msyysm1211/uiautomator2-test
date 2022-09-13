from xml.dom import minidom
import uiautomator2 as u2
from time import sleep
from os import system
from xml.etree.ElementTree import parse
from xml.dom.minidom import parseString
import os

#list.append({"children":[],"name": testSuiteNodeListA.nodeName},)
def getsourceid(xml,list):
    # 获取XML中所有元素
    # dom = minidom.parse(r"C:\Users\26947\AndroidStudioProjects\EspressoTest\app\src\main\res\layout\activity_second.xml")
    dom = parseString(xml)
    testSuiteNodeListA = dom.firstChild
    for ts_node in testSuiteNodeListA.childNodes:
        searchId(ts_node,list)
    return list

def searchId(testSuiteNodeList,list):
    if type(testSuiteNodeList) == minidom.Element:
        if testSuiteNodeList.firstChild:
            for ts_node in testSuiteNodeList.childNodes:
                searchId(ts_node,list)
        else:
            if 'clickable' in (testSuiteNodeList.attributes.keys()) and 'long-clickable' in (testSuiteNodeList.attributes.keys()):
                if (testSuiteNodeList.attributes['clickable'].value) or (testSuiteNodeList.attributes['long-clickable'].value):
                    list.append({testSuiteNodeList.attributes['resource-id'].value})

