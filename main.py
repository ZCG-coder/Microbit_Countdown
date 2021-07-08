def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        """)
    basic.pause(5000)
    basic.show_leds("""
        . . # . .
        . # # # .
        # # # # #
        . . # . .
        . . # . .
        """)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.RED,
        Kitronik_STOPbit.DisplayLights.OFF)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
        Kitronik_STOPbit.DisplayLights.ON)
    basic.pause(5000)
    for index in range(5):
        Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
            Kitronik_STOPbit.DisplayLights.OFF)
        basic.pause(500)
        Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
            Kitronik_STOPbit.DisplayLights.ON)
        basic.pause(500)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
        Kitronik_STOPbit.DisplayLights.OFF)
    Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.RED,
        Kitronik_STOPbit.DisplayLights.ON)
input.on_button_pressed(Button.A, on_button_pressed_a)

def countDown(sec):
    for index2 in range(sec):
        sec -= 1
        basic.show_number(sec)
        basic.pause(1000)
sec = 0
basic.show_string("HI")
Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.GREEN,
    Kitronik_STOPbit.DisplayLights.OFF)
Kitronik_STOPbit.traffic_light_led(Kitronik_STOPbit.LightColours.RED,
    Kitronik_STOPbit.DisplayLights.ON)
countDown(10)