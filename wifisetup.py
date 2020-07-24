import network
import config
import time

def setup():

	ap_if = network.WLAN(network.AP_IF)
	ap_if.active(False)
	sta_if = network.WLAN(network.STA_IF)
	if not sta_if.isconnected():
        	print('Connecting to WiFi...')
	        sta_if.active(True)
		if config.STATIC:
			print("Setting static IP address..")
			sta_if.ifconfig((config.IP, config.SUBNET, config.GATEWAY, config.DNS))
	        sta_if.connect(config.SSID, config.PASS)
       		while not sta_if.isconnected():
        	    print('-')
	            time.sleep(1)

	return sta_if.isconnected()
