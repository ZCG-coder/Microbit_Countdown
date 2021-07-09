def count_down(seconds: int = 0):
    seconds += 1
    for _ in range(seconds + 1):
        seconds += 0 - 1
        basic.show_number(seconds)
        basic.pause(1000)

def on_forever():
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.RED,
        Kitronik_STOPbit.DisplayLights.ON)
    count_down(3)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.RED, Kitronik_STOPbit.DisplayLights.OFF)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
        Kitronik_STOPbit.DisplayLights.ON)
    count_down(3)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN, Kitronik_STOPbit.DisplayLights.OFF)

basic.forever(on_forever)