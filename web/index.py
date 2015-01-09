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

@route('/jelinsky-moranda-model')
def musa_okumoto():
    return template('index', template_name = 'jelinsky_moranda.tpl', current_view = 'jelinsky_moranda')

@route('/musa-model')
def musa_model():
    return template('index', template_name = 'musa.tpl', current_view = 'musa')

@route('/musa-okumoto-model')
def musa_okumoto():
    return template('index', template_name = 'musa_okumoto.tpl', current_view = 'musa_okumoto')

@route('/static-models')
def static_models():
    return template('index', template_name = 'static_models.tpl', current_view = 'static_models')

@route('/')
@route('/index')
@route('/overview')
def index():
    return template('index', template_name = 'overview.tpl', current_view = 'overview')

run(host='localhost', port=8080, debug=True)