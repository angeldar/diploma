import bottle
from bottle import Bottle, request, response, route, run, template, static_file

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

@route('/ajax', method='GET')
def get_ajax():
    return {"value" : "string"}

@route('/')
def index():
    return static_file('index.html', root='views')
    # return "Hello World!"

run(host='localhost', port=8080, debug=True)