def count_down(seconds: int = 0):
    while seconds > 0:
        seconds -= 1
        basic.show_number(seconds)
        basic.pause(1000)


COMMON_VOLTAGE = 0.5
LESSTHAN30_VOLTAGE = 1
distance = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 58
def on_forever():
    global distance
    distance = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 58
    # 1 = 1 voltage
    # 0.5 = 0.5 voltage
    if distance > 50:
        pins.digital_write_pin(DigitalPin.P0, 1)
        count_down(10)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P2, 1)
        count_down(10)
        pins.digital_write_pin(DigitalPin.P2, 0)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0.5)
        count_down(10)
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P2, 0.5)
        count_down(10)
        pins.digital_write_pin(DigitalPin.P2, 0)

basic.forever(on_forever)