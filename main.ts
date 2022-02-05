let running = false
let start = 0
let time = 0
input.onButtonPressed(Button.A, function () {
    running = true
    start = input.runningTime()
})
input.onButtonPressed(Button.AB, function () {
    running = false
    time = 0
})
input.onButtonPressed(Button.B, function () {
    if (true) {
        time += input.runningTime() - start
    }
    running = false
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    if (!(running)) {
        basic.clearScreen()
        basic.showNumber(time / 1000)
    }
})
basic.forever(function () {
    if (running) {
        basic.showIcon(IconNames.Heart)
        basic.showIcon(IconNames.SmallHeart)
    } else {
        basic.showIcon(IconNames.Asleep)
    }
})
