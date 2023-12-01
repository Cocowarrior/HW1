from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/hi')
def hi():
    return 'Hi, world!'

@app.route('/ft2m')
def ft2m():
    return render_template("ft2m.html")

@app.route('/ft2m_action')
def ft2m_action():
    feets = request.args.get("feets")
    return "m="+str(float(feets)*0.3048)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)

