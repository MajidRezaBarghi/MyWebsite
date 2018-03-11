from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html')


#if you want to turn off teh debug mode you just
#need to set the debuger to false.
if __name__=="__main__":
    app.run(debug=True)
