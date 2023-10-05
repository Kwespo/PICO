from machine import Pin
import utime

Trigger = Pin(21, Pin.OUT)
Echo = Pin(20, Pin.IN)


def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
        
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    distance = "{:.1f}".format(distance)
    
    print(distance + " cm")
    
    return str(distance)

    TimePassed = SignalOff - SignalOn
    Distance = (TimePassed * 0.0343) / 2
    Distance = round(Distance, 3)

    print(f"{round(Distance)} cm or {round((Distance / 100), 2)} Meters")

while True:
    ultra()
