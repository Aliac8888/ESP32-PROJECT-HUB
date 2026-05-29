from machine import Pin
import time

# Pins (change if needed)
PIN_RED = 14
PIN_BLUE = 27
PIN_BUZZ = 26
PIN_BUTTON = 33

# Setup LEDs
red = Pin(PIN_RED, Pin.OUT)
blue = Pin(PIN_BLUE, Pin.OUT)
buzz = Pin(PIN_BUZZ, Pin.OUT)
button = Pin(PIN_BUTTON, Pin.IN, Pin.PULL_UP)

flag = 0
last_button_state = 1

red.on()
blue.off()
buzz.off()

while True:
    current_button_state = button.value()
    
    # Detect button press (transition from high to low)
    if last_button_state == 1 and current_button_state == 0:
        flag += 1
        # Debounce delay
        time.sleep(0.05)
    
    last_button_state = current_button_state
    if flag % 2 == 0:
        red.toggle()
        blue.toggle()
        buzz.toggle()
    else :
        red.on()
        blue.off()
        buzz.off()
    time.sleep(0.5)
