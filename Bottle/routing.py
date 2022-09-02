from bottle import route, run, template

@route('/')
def index():
    return("<h1> On the Home page! </h1>")

@route('/login')
def login(): #json
    return({
        1:'a',
        2:'b',
        3:'c'
    })

@route('/greet/<name>')
def greet(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/greet/rashmi') #OVERRIDES  
def mom():
    return ('<h1> MOOOOMMMM </h1>')

@route('/<name>/<age>') #without age, error
def intro(name, age):
    return template("<h1> Your name is {{name}}, </h1> <p> Age: {{34}}</p>", name=name, age=age)

if __name__ == '__main__':
    run(debug=True, reloader=True)