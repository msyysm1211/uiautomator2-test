from sourceid import getsourceid,searchId
import uiautomator2 as u2
from xml.dom.minidom import parseString
def compare(xml1,xml2):
    dom1 = parseString(xml1)
    dom2 = parseString(xml2)
    testSuiteNodeListA = dom1.firstChild
    testSuiteNodeListB = dom2.firstChild
    list1=[]
    list2=[]
    list1=getsourceid(xml1,list1)
    list2 = getsourceid(xml2, list2)
    print(list1)
    print(list2)
    if list1==list2:
        print("无变化")
        return False
    else:
        print("有变化")
        return True