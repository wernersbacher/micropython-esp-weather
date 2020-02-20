import urequests
import config

PRECISION_MULTI = 10000

def send_temperature(temperature, humidity):
    print('Invoking log webhook')
    # my web api expects the values without decimal places and multiplied by 10,000
    # set PRECISION_MULTI to 1 to send the original data
    url = config.WEBHOOK_URL.format(int(temperature * PRECISION_MULTI), int(humidity * PRECISION_MULTI))

    response = urequests.get(url)
    if response.status_code < 400:
        print('Webhook invoked')
    else:
        print('Webhook failed')
        raise RuntimeError('Webhook failed')
