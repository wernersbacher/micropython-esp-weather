import wifisetup
import boardhandling
import web

def run():
	try:
		wifisetup.setup()
		temperature, humidity = boardhandling.get_temperature_and_humidity()
		print('Temperature = {temperature}, Humidity = {humidity}'.format(
			temperature=temperature, humidity=humidity))
		web.send_temperature(temperature, humidity)
	except Exception as exc:
		print(exc)
		boardhandling.show_error()

	if not boardhandling.is_debug():
		pass
		#hardware.deepsleep()


run()
