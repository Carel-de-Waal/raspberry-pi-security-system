from bottle import route, run, static_file

@route('/')
def static_main():
    return static_file('main.html' , root='./static/')

@route('/cam01_script.js')
def static_main():
    return static_file('cam01_script.js' , root='./static/')

run(host='0.0.0.0', port=9977, debug=True)
