import network
import config

def setup():

	ap_if = network.WLAN(network.AP_IF)
	ap_if.active(False)
	sta_if = network.WLAN(network.STA_IF)
	sta_if.active(True)
	sta_if.connect(config.SSID, config.PASS)

	return sta_if.isconnected()
