import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14, 15
instance_1 = dht11.DHT11(pin=14)
instance_2 = dht11.DHT11(pin=15)



try:
        while True:
            result = instance_1.read()
            if result.is_valid():
                print("Last valid input: " + str(datetime.datetime.now()))

                print("Temperature: %-3.1f C" % result.temperature)
                print("Humidity: %-3.1f %%" % result.humidity)

            time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

