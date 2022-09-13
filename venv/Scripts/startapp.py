import uiautomator2 as u2
from time import sleep
from os import system

d = u2.connect("192.168.185.103:5555")
d.healthcheck()
def startapp():
    if d.info.get('screenOn')==False:#判断当前屏幕是否打开
        d.screen_on()
        sleep(2)#适当的加上延时，可以确保脚本的健壮，不容易崩溃
        d.unlock()#这个解锁好像不是每个手机上都能用
    sleep(1)
#回到主界面
    d.press("home")
#回到主界面
    d.app_start("com.netease.cloudmusic")

startapp()