from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/hi')
def hi():
    return 'Hi, world!'

@app.route('/mile2km')
def mile2km():
    return render_template("mile2km.html")

@app.route('/mile2km_action')
def mile2km_action():
    miles = request.args.get("miles")
    return "km="+str(float(miles)*1.60)

if __name__== '__main__':
   app.run(host='0.0.0.0',port=5001)

