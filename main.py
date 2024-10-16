import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33,
    board.IO34,
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

# main loop
while True:
    volume = microphone.value

    print(volume)

    # leds[0].value = not leds[0].value
    # leds[4].value = not leds[0].value
    #num_leds_on = min(len(leds), volume // (60000 // len(leds)))
    num_leds_on = len(leds) * volume // 50000

    for i in range(len(leds)):
        leds[i].value = i < num_leds_on

    sleep(0.1)


    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?