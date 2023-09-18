from machine import Pin
import utime

Trigger = Pin(21, Pin.OUT)
Echo = Pin(20, Pin.IN)


def ultra():
    Trigger.low()
    utime.sleep(0.5)
    Trigger.high()
    utime.sleep(0.5)
    Trigger.low()
    while Echo.value() == 0:
        SignalOn = utime.ticks_us()
    while Echo.value() == 1:
        SignalOff = utime.ticks_us()

    TimePassed = SignalOff - SignalOn
    Distance = (TimePassed * 0.0343) / 2
    Distance = round(Distance, 3)

    print(f"{round(Distance)} cm or {round((Distance / 100), 2)} Meters")

while True:
    ultra()
