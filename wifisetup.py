import network
import config
import time

def setup():

	ap_if = network.WLAN(network.AP_IF)
	ap_if.active(False)
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
        	#print('Connecting to WiFi...')
	        sta_if.active(True)
	        sta_if.connect(config.SSID, config.PASS)
       		while not sta_if.isconnected():
	            time.sleep(1)

	return sta_if.isconnected()
