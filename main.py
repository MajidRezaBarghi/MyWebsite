from flask import Flask, request , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

@app.route("/bacon", methods=['GET','POST'])
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"

if __name__ == "__main__":
    app.run()
