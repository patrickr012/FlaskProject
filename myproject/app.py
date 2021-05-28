from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)

@app.route('/celsius')
@app.route('/celsius/<fahrenheit>')
def celsius(fahrenheit = ""):
    celsius_temp = (int(fahrenheit) - 30)//2
    return "Temp in celsius is: " + str(celsius_temp) + " degrees"



if __name__ == '__main__':
    app.run()

