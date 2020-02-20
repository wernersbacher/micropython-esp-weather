
import wifisetup
import hardware



# connect to the wifi
is_connected = wifisetup.setup()

if is_connected:
	blinking.blink(2)
else:
	blinking.blink(10)
