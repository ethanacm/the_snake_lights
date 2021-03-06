# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time


import colorsys
from neopixel import *
import random as Random

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering



# Define functions which animate LEDs in various ways.
def loop(strip, color1, color2, wait_ms=100):
    for i in range(strip.numPixels() / 2):
        strip.setPixelColor(i, color1)
        strip.setPixelColor(strip.numPixels() - i, color1)
        strip.show()
        time.sleep(wait_ms/1000.0)
    for i in range(strip.numPixels() / 2):
        strip.setPixelColor(strip.numPixels() / 2 - i, color2)
        strip.setPixelColor(strip.numPixels() / 2 + i, color2)
        strip.show()
        time.sleep(wait_ms/1000.0)

def random(strip):
    for i in range(30):
        color = Color(Random.randint(0, 255), Random.randint(0, 255), Random.randint(0, 255), Random.randint(0, 255))
        for i in range(Random.randint(0,5)):

            strip.setPixelColor(Random.randint(0, strip.numPixels()), color)
            
        strip.show()

def allOneColor(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()


def twinkle(strip, color, wait_ms=100):
        for i in range(strip.numPixels() / 30):
            strip.setPixelColor(Random.randint(0, strip.numPixels()), color)
            strip.show()
            time.sleep(.5)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def HLSColor(hue, lightness, saturation):
    hue = hue / 360.0
    lightness = lightness / 100.0
    saturation = saturation / 100.0
    hls = colorsys.hls_to_rgb(hue, lightness, saturation)
    return Color(int(hls[0] * 255), int(hls[1]* 255), int(hls[2] * 255))


# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()


    print ('Press Ctrl-C to quit.')
    val = 1
    while True:
        white = Color(20, 20, 20)
        red = Color(127,   0,   0)
        blue = Color(  0,   255, 0)
        green = Color(0, 255, 0)
        #random(strip)
        #twinkle(strip, Color(255, 255, 255))
        # loop(strip, red, green, 100)
        
        #'''
        allOneColor(strip, HLSColor(val, 50, 100))
        #allOneColor(strip, Color(val, val, val))
        time.sleep(.05)
        print(val)
        val = (val + 1) % 360
        #'''
        
        #print ('Color wipe animations.')
        #colorWipe(strip, Color(255, 0, 0))  # Red wipe
        #colorWipe(strip, Color(0, 255, 0))  # Blue wipe
        #colorWipe(strip, Color(0, 0, 255))  # Green wipe
        #print ('Theater chase animations.')
        #theaterChase(strip, Color(127, 127, 127))  # White theater chase
        #theaterChase(strip, Color(127,   0,   0))  # Red theater chase
        #theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
        #print ('Rainbow animations.')
        #rainbow(strip)
        #rainbowCycle(strip)
        #theaterChaseRainbow(strip)

