from bibliopixel import LEDStrip
from bibliopixel.drivers.LPD8806 import * 
from bibliopixel.animation import BaseStripAnim
#from bibliopixel import log
#log.setLogLevel(log.DEBUG)

class KnightRiderScanBar(BaseStripAnim):
    def __init__(self, led):
        super(KnightRiderScanBar, self).__init__(led)
        self._tail = 7
        self._pos = 0
        self._direction = 1
        self._ledCount = 24
	self._internalDelay=20

    def step(self, amt=1):
	if self._direction == 1:
            for j in range(self._pos):
       	        diff = min(self._tail, abs(j - self._pos)) 
                brightness = (512 >> diff) -1
                self._led.set(min(self._ledCount-1, j), (brightness, 0, 0))
            self._pos = self._pos+1

	    if self._pos >= self._ledCount + self._tail:
		self._direction = 0

	if self._direction == 0:
	    for j in range(self._ledCount-1, self._pos, -1):
                diff = min(self._tail, abs(j - self._pos))
                brightness = (512 >> diff) - 1
                self._led.set(max(0, j), (brightness, 0, 0))
            self._pos = self._pos-1
	
	    if self._pos <= -self._tail:
		self._direction = 1

driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)
led = LEDStrip(driver, threadedUpdate = True)
anim = KnightRiderScanBar(led)

try:
    anim.run()
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()
