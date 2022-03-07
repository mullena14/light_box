# written by Alicia Mullen, 2021

import tkinter
import screen_brightness_control as sbc
import devcon_win

TOUCHSCREEN_ID = '' # look through device manager to find id

def main():
    sbc.set_brightness(100) # set brightness to 100%
    window = tkinter.Tk()
    window.attributes('-fullscreen', True) # should add button to close window?
    window.configure(bg='white')
    window.mainloop()

if __name__ == "__main__":
    main()
