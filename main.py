Ex1 

def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature())
    elif input.logo_is_pressed():
        input.light_level()
        basic.show_icon(IconNames.HEART)
    else:
        basic.clear_screen()
basic.forever(on_forever)

Ex2 

def on_forever():
    if input.logo_is_pressed():
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.pause(5000)
        basic.show_icon(IconNames.SMALL_SQUARE)
        basic.forever(on_forever)


    Ex 3 


def on_sound_loud():
    basic.show_icon(IconNames.LINE)
input.on_sound(DetectedSound.LOUD, on_sound_loud)




Ex 4 

degrees = 0

def on_sound_loud():
    basic.show_icon(IconNames.GHOST)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    elif degrees < 315:
        basic.show_string("W")
    else:
        basic.clear_screen()
basic.forever(on_forever)


Ex 5 
accel = 0

def on_forever():
    global accel
    if input.is_gesture(Gesture.TILT_LEFT):
        accel = input.acceleration(Dimension.X)
        basic.show_number(accel)
    else:
        if input.is_gesture(Gesture.TILT_RIGHT):
            accel = input.acceleration(Dimension.X)
            basic.show_number(accel)
basic.forever(on_forever)



 
