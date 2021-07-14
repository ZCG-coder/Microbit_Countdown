function count_down(seconds: number = 0) {
    while (seconds > 0) {
        seconds -= 1
        basic.showNumber(seconds)
        basic.pause(1000)
    }
}

let COMMON_VOLTAGE = 0.5
let LESSTHAN30_VOLTAGE = 1
let distance = pins.pulseIn(DigitalPin.P1, PulseValue.High) / 58
basic.forever(function on_forever() {
    
    distance = pins.pulseIn(DigitalPin.P1, PulseValue.High) / 58
    //  1 = 1 voltage
    //  0.5 = 0.5 voltage
    if (distance > 50) {
        pins.digitalWritePin(DigitalPin.P0, 1)
        count_down(10)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P2, 1)
        count_down(10)
        pins.digitalWritePin(DigitalPin.P2, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P0, 0.5)
        count_down(10)
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P2, 0.5)
        count_down(10)
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    
})
