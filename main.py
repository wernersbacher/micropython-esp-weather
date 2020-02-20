import wifisetup
import hardware
import web

def run():
	try:
		wifisetup.setup()
		temperature, humidity = hardware.get_temperature_and_humidity()
		print('Temperature = {temperature}, Humidity = {humidity}'.format(
			temperature=temperature, humidity=humidity))
		web.send_temperature(temperature, humidity)
	except Exception as exc:
		print(exc)
		hardware.show_error()

	if not hardware.is_debug():
		hardware.deepsleep()


run()
