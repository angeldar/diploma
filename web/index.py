from bottle import route, run, template, static_file

@route('/')
@route('/hello')
def index():
    return static_file('index.html', root='views')
    # return "Hello World!"

run(host='localhost', port=8080, debug=True)