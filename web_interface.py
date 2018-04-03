# web interface to control LEDs
# @author Ethan Cassel-Mace

import StrandMethods
import json
from flask import Flask, render_template, request, make_response

app = Flask(__name__)
strip = StrandMethods.Strip(300, 150)

@app.route('/')
def index():
    return 'home. do other stuff for lights'

@app.route('/colors/<color>')
def colors(color):
    if color == 'blue':
        strip.allOneColor(StrandMethods.BLUE)
    elif color == 'red':
        strip.allOneColor(StrandMethods.RED)
    elif color == 'green':
        strip.allOneColor(StrandMethods.GREEN)
    else:
        strip.allOneColor(StrandMethods.BLUE)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/led/<i>')
def led(i):
    r = request.args.get('r')
    g = request.args.get('g')
    b = request.args.get('b')

    strip.set_pixel_color(int(i), int(r), int(g), int(b))
    strip.show()

# Run the app.
if __name__ == '__main__':
    app.run(host= '10.10.10.107',debug=True, port=8080)
