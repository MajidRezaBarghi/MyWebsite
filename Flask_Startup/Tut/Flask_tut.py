from flask import Flask, request

app = Flask(__name__)

#what is going on here
#this procces is the routing or the mapping
#this ties a URL to a python function
#whenever we deliever a return statement
#can return a HTML file or some Json file
@app.route('/') #  @ signifies decorator wrap up a existing python function and modify it in a diffirent way this allows one to map a
def index():
    return 'Ricky is such a Bitch'

@app.route('/tuna')
def tuna():
    return '<h2> Tuna is good </h2>'

@app.route('/profile/<username>')
def profile(username):
    return "<h2>Hey there %s</h2>" %username

@app.route('/post/<int:post_id>') #integers need to written out this way
def show_post(post_id): # You don't need have the function the same name as the routing
    return "<h2>Post ID is %s</h2>" %post_id

@app.route("/bacon", methods=['GET','POST']) #This is how you would check if its Post or GET
def bacon():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"

#All this does is starts our web server
#our website will start running after this
if __name__=="__main__": # this line of code serves as a check to see if we are doing using this line of code correctly. Essentially only will run if you run the pythong file "main.py" directly
    app.run(debug=True)
