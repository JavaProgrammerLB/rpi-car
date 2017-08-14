# encoding:utf-8

import RPi.GPIO as GPIO
import time
import httplib
import config

TRLG = 2
ECHO = 3
def dist_init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	#3号脚，GPIO2
	GPIO.setup(TRLG,GPIO.OUT,initial=GPIO.LOW)
	#5号脚，GPIO3
	GPIO.setup(ECHO,GPIO.IN)
	time.sleep(2)

def checkdistance():
	#发出触发信号
	GPIO.output(TRLG,GPIO.HIGH)
	#保持15us
	time.sleep(0.000015)
	GPIO.output(TRLG,GPIO.LOW)
	while not GPIO.input(ECHO):
		pass
	#发现高电平时开始计时
	t1 = time.time()
	while GPIO.input(ECHO):
		pass
	#高电平时结束计时
	t2 = time.time()
	#返回距离米
	return (t2 - t1)*340/2

if __name__ == '__main__':
    dist_init()
    print config.WEB_ADDRESS
    print '-------'
    print config.WEB_PORT
    while True:
	distance = checkdistance()
	print 'distance: %0.2f m' %distance
	if (distance - 0.3) < 0.000000001:
		conn = httplib.HTTPConnection(config.WEB_ADDRESS, config.WEB_PORT)
		conn.request("GET", "/handle?type=bizhang")
		response = conn.getresponse()
		print '避障日志： ' + response.reason
		conn.close()
	time.sleep(1)
