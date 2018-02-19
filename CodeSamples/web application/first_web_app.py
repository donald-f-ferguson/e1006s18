# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# Modified by Donald F. Ferguson, Columbia University, 2018


# Import some frameworks that help us implement a web application.
from flask import Flask, render_template_string, request
from wtforms import Form, validators, TextField
import string


##############################################################################################################
# These are the two functions you will write.
# You will implement in a separate Python file and access via an import statement.
# The code here is a just a placeholder.


# 1. Check a dictionary to determine if word is correctly spelled.
# 2. If not, call a set of functions that generate "near by, correctly spelled words."
# 3. Return the 5 "best suggested corrections."
def check_word(word):
    # Your code and called functions go here.
    return "floccinaucinihilipilification, sesquipedalianism?"


# The user selected a correction, or entered a new correct spelling.
# We will record the correct spelling and score as a possible common correction for user.
def update_corrections(original_word, corrected_word):
    # Your code goes here.
    print("Correction for " + original_word + " is " + "corrected_word")

# End of where your code will go.
##############################################################################################################

# Include and initialize the Flask framework.
app = Flask(__name__)


# html page is the view. Putting templates directly in the application is a massive anti-pattern.
# Also, most programmers and applications do not use static HTML templates like this one.
# I will give you the HTML pages to "serve" in your application.
#
page = '''
<html>
   <head>
      <title>HW3 -- The Spelling Correction Suggester!</title>
      <script>
        function myFunction() {
            var x = document.getElementById("told_you_so");
            if (x.style.display === "none") {
                x.style.display = "block";
            }
            else {
                x.style.display = "none";
            }
        }
        </script>
   </head>

   <body>
      <h1>HW3 -- The Spelling Police</h1>
      <h2>Our Motto is, "To correct and serve!"</h2>

      <form method=post action="">
         So, you think you can spell?
      <br>
      Enter a word.
         {{ template_form.text_field }}
      <br>
        {% if result != None %}
        <br>
           Did you possibly mean? {{ result }}
        <br>
        {% endif %}
      <br>
        <input type=submit value=Check>
      </form>
       <button onclick="myFunction()">What does this button do?</button>
       <div id="told_you_so" style="display:none;">
        <p>
        <span style="color:red;font-size: 32px;">
        Told you web apps are in the textbook.
        </span>
        </div>
   </body>
</html>
'''


# InputForm and below is our controller
# form with a single TextField.
# This is part of the framework and you do not need to worry about it.
class InputForm(Form):
    text_field = TextField(validators=[validators.InputRequired()])


# This is the core of the web application server and implementing the page delivery and REST API.
@app.route('/', methods=['GET', 'POST'])
def index():
    spell_result = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        input_val = form.text_field.data
        spell_result = check_word(input_val)
    return render_template_string(page, template_form=form, result = spell_result)


if __name__ == '__main__':
    app.run(debug=True)
