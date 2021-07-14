function count_down(seconds: number = 0) {
    while (seconds > 0) {
        seconds -= 1
        basic.showNumber(seconds)
        basic.pause(1000)
    }
}

basic.forever(function on_forever() {
    pins.digitalWritePin(DigitalPin.P0, 1)
    count_down(10)
    pins.digitalWritePin(DigitalPin.P0, 0)
    pins.digitalWritePin(DigitalPin.P1, 1)
    count_down(10)
    pins.digitalWritePin(DigitalPin.P1, 0)
})
