# encoding:utf-8

import RPi.GPIO as gpio
import config as c
import time

class Car:
    def __init__(self, dir, flag):
	self.flag = flag
        self.dir = dir # 1-forward 2-backward 3-left 4-right
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        # setup I/O OUT
        gpio.setup(c.IN1, gpio.OUT)
        gpio.setup(c.IN2, gpio.OUT)
        gpio.setup(c.IN3, gpio.OUT)
        gpio.setup(c.IN4, gpio.OUT)
        # init
        self.stop()

    def forward(self):
        gpio.output(c.IN1, False)
        gpio.output(c.IN2, True)
        gpio.output(c.IN3, False)
        gpio.output(c.IN4, True)
        self.dir = 1
        print 'car forward'

    def backward(self):
        gpio.output(c.IN1, True)
        gpio.output(c.IN2, False)
        gpio.output(c.IN3, True)
        gpio.output(c.IN4, False)
        self.dir = 2
        print 'car backward'

    def left(self):
        gpio.output(c.IN1, False)
        gpio.output(c.IN2, True)
        gpio.output(c.IN3, True)
        gpio.output(c.IN4, False)
        self.dir = 3
        print 'car left'

    def trueFlag(self):
        self.flag = True
        print 'flat true'

    def falseFlag(self):
        self.flag = False
        print 'flag false'

    def right(self):
        gpio.output(c.IN1, True)
        gpio.output(c.IN2, False)
        gpio.output(c.IN3, False)
        gpio.output(c.IN4, True)
        if self.flag:
        	self.dir = 4
        print 'car right'

    def stop(self):
        gpio.output(c.IN1, False)
        gpio.output(c.IN2, False)
        gpio.output(c.IN3, False)
        gpio.output(c.IN4, False)
        self.dir = 0
        print 'car stop'

    def shutdown(self):
        self.dir = 0
        self.stop()
        gpio.cleanup()

    def dir(self):
        print "director is: " + self.dir
        return self.dir

    def before(self):
        print 'car before'
        dir = self.dir
        if dir == 1:
            self.forward()
        elif dir == 2:
            self.backward()
        elif dir == 3:
            self.left()
        elif dir == 4:
            self.right()
        elif dir == 0:
            self.stop()
    
    def bizhang(self):
	if self.dir !=  0:
        	# 让车右转，且不修改车的当前方向
        	self.falseFlag()
        	self.right()
		time.sleep(1.5)
        	self.trueFlag()
       		 # 让车恢复原来的前进方向
        	self.before()
