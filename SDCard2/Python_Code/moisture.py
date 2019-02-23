import keyboard

moisture = 0
button_pressed = 0

while True:
    if keyboard.is_pressed('q'):
        print('q is pressed')
    else:
        print ('q is not pressed')
