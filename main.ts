function count_down(seconds: number = 0) {
    seconds += 1
    for (let _ = 0; _ < seconds + 1; _++) {
        seconds += 0 - 1
        basic.showNumber(seconds)
        basic.pause(1000)
    }
}

basic.forever(function on_forever() {
    Kitronik_STOPbit.trafficLightLED(Kitronik_STOPbit.LightColours.Red, Kitronik_STOPbit.DisplayLights.On)
    count_down(3)
    Kitronik_STOPbit.trafficLightLED(Kitronik_STOPbit.LightColours.Red, Kitronik_STOPbit.DisplayLights.Off)
    Kitronik_STOPbit.trafficLightLED(Kitronik_STOPbit.LightColours.Green, Kitronik_STOPbit.DisplayLights.On)
    count_down(3)
    Kitronik_STOPbit.trafficLightLED(Kitronik_STOPbit.LightColours.Green, Kitronik_STOPbit.DisplayLights.Off)
})
