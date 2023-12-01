from flask import Flask, render_template, request 

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world'

@app.route('/cm2inch')
def cm2inch():
    return render_template("cm2inch.html")

@app.route('/cm2inch_action')
def cm2inch_action():
    centimeters = request.args.get("centimeters")
    return "centimeters="+str(centimeters)+" inch="+float(centimeters)*2.54

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
