from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story
app = Flask(__name__)
app.debug= True
app.config['SECRET_KEY'] = "chickensareverycool42"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
     return """<a href="/home">click here<a/>"""

@app.route('/home')
def homepage_gen():
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('story.html', text=text)
#something like this im guessing
#COULD OF DONE WITH REUQEST . FORM BUT I THINK AN ISSUE IS NOT HARDOCDING THE STRING FOR MADLIB
#@app.route('/add-comment', methods=["POST"])
#def save_comment():
#    comment = request.form["comment"]
#    username = request.form["username"]
#    print(request.form)
#    return f"""
#     <h1>SAVED YUR COMMENT</h1>
#     <ul>
#        <li>Username:{username}</li>
#        <li>comment:{comment}</li>
#     </ul>
#    """
