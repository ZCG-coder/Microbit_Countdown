def count_down(seconds: int = 0):
    while seconds > 0:
        seconds -= 1
        basic.show_number(seconds)
        basic.pause(1000)

def on_forever():
    pins.digital_write_pin(DigitalPin.P0, 1)
    count_down(10)
    pins.digital_write_pin(DigitalPin.P0, 0)
    pins.digital_write_pin(DigitalPin.P1, 1)
    count_down(10)
    pins.digital_write_pin(DigitalPin.P1, 0)

basic.forever(on_forever)