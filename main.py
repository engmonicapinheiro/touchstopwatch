running = False
start = 0
time = 0

def on_button_pressed_a():
    global running, start
    running = True
    start = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global running, time
    running = False
    time = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global time, running
    if True:
        time += input.running_time() - start
    running = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    if not (running):
        basic.clear_screen()
        basic.show_number(time / 1000)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    if running:
        basic.show_icon(IconNames.HEART)
        basic.show_icon(IconNames.SMALL_HEART)
    else:
        basic.show_icon(IconNames.ASLEEP)
basic.forever(on_forever)
