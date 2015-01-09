import bottle
from bottle import Bottle, request, response, route, run, template, static_file
from static import dinamic_tools as dt
import json

app = Bottle()

@route('/img/<filename:re:.*\.png>')
def send_image(filename):
    return static_file(filename, root='static/img', mimetype='image/png')

@route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css', mimetype='text/css')

@route('/js/<filename:re:.*\.js>')
def send_js(filename):
    return static_file(filename, root='static/js', mimetype='text/javascript')

@app.hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/musa', method='GET')
def get_musa():
    musa = dt.get_musa_data('G:/dev/diploma/static/datasets/dataset_6.txt')
    return json.dumps(musa)

@route('/musa-okumoto')
def musa_okumoto():
    return "Musa-Okumoto"

@route('/static_models')
def static_models():
    return "Jelinski-Moranda"

@route('/')
def index():
    return static_file('index.html', root='views')
    # return "Hello World!"

run(host='localhost', port=8080, debug=True)