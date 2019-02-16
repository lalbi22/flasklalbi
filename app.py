from flask import Flask, render_template, request
from search_erritem import ErrSearchItem

app = Flask(__name__, static_folder='static')
# app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    text1 = ["index", "element"]
    obj = ErrSearchItem(text1)
    obj.set("tag")
    return obj.get()
    # return "Hello About!"

@app.route("/search")
def search():
    text1 = ["first", "second", "third"]
    obj = ErrSearchItem(text1)
    return render_template("search.html", obj=obj)

@app.route("/ework")
def ework():
    return render_template("app.html")

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port='5500', debug=True)
    app.run(debug=True)
