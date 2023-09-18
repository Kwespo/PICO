from machine import Pin
import utime

trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)


def ultra():
    trigger.low()
    utime.sleep(0.5)
    trigger.high()
    utime.sleep(0.5)
    trigger.low()
    while echo.value() == 0:
        SignalOn = utime.ticks_us()
    while echo.value() == 1:
        SignalOff = utime.ticks_us()

    timepassed = SignalOff - SignalOn
    distance = (timepassed * 0.0343) / 2
    distance = round(distance, 3)

    print(f"{round(distance, 2)} cm or {round((distance / 100), 3)} Meters")

while True:
    ultra()
