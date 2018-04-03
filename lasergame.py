# Code to create a 'laser game'. Press a-' on the keyboard to play while connected to lights.
# Author: Ethan Cassel-Mace (ethanacm@gmail.com)
#

import time
import colorsys
from neopixel import *
import pygame
import random as Random
import curses

# LED strip configuration:
LED_COUNT = 300  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 5  # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 150  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP = ws.WS2811_STRIP_GRB  # Strip type and colour ordering


# Define functions which animate LEDs in various ways.

def HLSColor(hue, lightness, saturation):
    hue = hue / 360.0
    lightness = lightness / 100.0
    saturation = saturation / 100.0
    hls = colorsys.hls_to_rgb(hue, lightness, saturation)
    return Color(int(hls[0] * 255), int(hls[1] * 255), int(hls[2] * 255))


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    stdscr = curses.initscr()

    curses.cbreak()
    stdscr.keypad(1)

    stdscr.addstr(0, 10, "Hit 'q' to quit")
    stdscr.refresh()

    key = ''
    while key != ord('q'):
        key = stdscr.getch()
        stdscr.addch(20, 25, key)
        stdscr.refresh()
        if key == curses.KEY_UP:
            stdscr.addstr(2, 20, "Up")
        elif key == curses.KEY_DOWN:
            stdscr.addstr(3, 20, "Down")

    curses.endwin()



