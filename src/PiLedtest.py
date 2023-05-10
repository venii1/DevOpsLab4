from hal import hal_led as led
from hal import hal_input_switch as switch
import socket
import time
from time import sleep


def slide_sw():
    return switch.read_slide_switch()


def blink_led(b):
    if b == 1:
        for x in range(0, 5):
            led.set_output(24, 1)
            time.sleep(0.1)
            led.set_output(24, 0)
            time.sleep(0.1)

    if b == 2:
        for x in range(0, 50):
            led.set_output(24, 1)
            time.sleep(0.05)
            led.set_output(24, 0)
            time.sleep(0.05)


def main():
    switch.init()
    led.init()
    while 1:
        x = slide_sw()
        if x == 1:
            blink_led(1)
            #while slide_sw() == 1:
                #c = 1
        else:
            blink_led(2)
            while slide_sw() == 0:
                d = 1


if __name__ == "__main__":
    main()
