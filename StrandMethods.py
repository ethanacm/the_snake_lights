# abstractions for LED strip

import time
import colorsys
import random as Random
from neopixel import *


# LED strip configuration:
# LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
## LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
# LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

# useful colors:
RED = Color(127,   0,   0)
BLUE = Color(  0,   255, 0)
GREEN = Color(0, 255, 0)

class Strip:
    def __init__(self, count, brightness):
        self.count = count
        self.brightness = brightness
        self.strip = Adafruit_NeoPixel(self.count, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, self.brightness, LED_CHANNEL, LED_STRIP)
        self.strip.begin()

    def loop(self, color1, color2, wait_ms=100):
        for i in range(self.strip.numPixels() / 2):
            self.strip.setPixelColor(i, color1)
            self.strip.setPixelColor(self.strip.numPixels() - i, color1)
            self.strip.show()
            time.sleep(wait_ms/1000.0)
        for i in range(self.strip.numPixels() / 2):
            self.strip.setPixelColor(self.strip.numPixels() / 2 - i, color2)
            self.strip.setPixelColor(self.strip.numPixels() / 2 + i, color2)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def random(self):
        for i in range(30):
            color = Color(Random.randint(0, 255), Random.randint(0, 255), Random.randint(0, 255), Random.randint(0, 255))
            for i in range(Random.randint(0,5)):

                self.strip.setPixelColor(Random.randint(0, self.strip.numPixels()), color)

            self.strip.show()

    def allOneColor(self, color):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
        self.strip.show()


    def twinkle(self, color, wait_ms=100):
            for i in range(self.strip.numPixels() / 30):
                self.strip.setPixelColor(Random.randint(0, self.strip.numPixels()), color)
                self.strip.show()
                time.sleep(.5)

    def colorWipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, color)
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, wheel((i+j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def rainbowCycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256*iterations):
            for i in range(self.strip.numPixels()):
                self.strip.setPixelColor(i, self.wheel((int(i * 256 / self.strip.numPixels()) + j) & 255))
            self.strip.show()
            time.sleep(wait_ms/1000.0)

    def theaterChaseRainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, wheel((i+j) % 255))
                self.strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, self.strip.numPixels(), 3):
                    self.strip.setPixelColor(i+q, 0)


def HLSColor(hue, lightness, saturation):
    hue /= 360.0
    lightness /= 100.0
    saturation /= 100.0
    hls = colorsys.hls_to_rgb(hue, lightness, saturation)
    return Color(int(hls[0] * 255), int(hls[1]* 255), int(hls[2] * 255))


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