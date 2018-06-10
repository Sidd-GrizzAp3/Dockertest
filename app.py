from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
  
@app.route("/first_route")
def first_route():
    return "Hello From the Other Side"

@app.route("/first_route/<param>")
def first(param):
    return param

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')