from xml.dom import minidom

#获取XML中所有元素
dom = minidom.parse(r"C:\Users\26947\AndroidStudioProjects\EspressoTest\app\src\main\res\layout\activity_second.xml")
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
            if 'Button' in (testSuiteNodeList.attributes.keys()) and 'long-clickable' in (testSuiteNodeList.attributes.keys()):
                if (testSuiteNodeList.attributes['Button'].value) or (testSuiteNodeList.attributes['long-clickable'].value):
                    list[0]["children"].append({"name": testSuiteNodeList.attributes['class'].value})

for ts_node in testSuiteNodeListA.childNodes:
    searchId(ts_node)
print (list)