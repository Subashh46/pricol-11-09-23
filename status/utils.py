import serial
import datetime
import time


def scan():
    device = 'COM5'
    arduino = serial.Serial(device, 9600, timeout=10)
    rfids = []
    time_end = time.monotonic() + 10
    while time_end > time.monotonic():
        data = arduino.readline()
        if data:
            string = ''
            for i in range(0, 12):
                string = string + chr(data[i])
            string = string.strip()
            if string not in rfids:
                rfids.append(string)
    return rfids


def time_now():
    return str(datetime.datetime.now())[:19]


