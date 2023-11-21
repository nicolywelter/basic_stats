# Script for the Raspberry Pi Camera Trap.

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

motion_sensor_pin = 7
camera = PiCamera()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motion_sensor_pin, GPIO.IN)

try:
    while True:
        motion_status = GPIO.input(motion_sensor_pin)
        print("Motion Status: {}".format(motion_status))

        if motion_status == 1:
            print("Motion Detected! Capturing Picture...")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            image_path = 'image_'+timestamp+'.jpg'
            camera.capture(image_path)
            print("Image captured and saved to: {image_path}")
        else:
            print("No Motion Detected.")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
    camera.close()