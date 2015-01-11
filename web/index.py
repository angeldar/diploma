import bottle
from bottle import Bottle, request, response, route, run, template, static_file
from static import dinamic_tools as dt
from radon import static_tools as st
import os, sys
import json

app = Bottle()

bottle.TEMPLATE_PATH.insert(0, './views')

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

@route('/musa-ajax', method='GET')
def get_musa():
    musa = dt.get_musa_data('G:/dev/diploma/static/datasets/dataset_6.txt')
    return json.dumps(musa)

@route('/musa-okumoto-ajax', method='GET')
def get_musa_okumoto():
    musa_okumoto = dt.get_musa_okumoto_data('G:/dev/diploma/static/datasets/dataset_6.txt')
    return json.dumps(musa_okumoto)

@route('/jelinsky-moranda-ajax', method='GET')
def get_jelinsky_moranda():
    jm = dt.get_jelinski_moranda_data('G:/dev/diploma/static/datasets/dataset_6.txt')
    return json.dumps(jm)

@route('/static-models-ajax', method='POST')
def get_static_models():
    path_to_repo = request.forms.get("path")
    if os.path.isdir(path_to_repo):
        project_name = os.path.split(path_to_repo)[-1]

        static_models_data = st.get_static_data_for_repo(repo_path = path_to_repo, proj_name = project_name,
            exclude = ['G:/dev/bottle/test/test_importhook.py', 'G:/dev/bottle/test/test_wsgi.py'])

        return json.dumps(static_models_data)
    else:
        return json.dumps({'error': 'No such folder'})

@route('/')
@route('/index')
@route('/overview')
def index():
    return template('index', template_name = 'overview.tpl', current_view = 'overview')

run(host='localhost', port=8080, debug=True)