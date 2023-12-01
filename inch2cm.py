from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/inch2cm')
def inch2cm():
    return render_template("inch2cm.html")

@app.route('/inch2cm_action')
def inch2cm_action():
    inches = request.args.get("inches")
    return "cm="+str(float(inches)*2.54)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)

