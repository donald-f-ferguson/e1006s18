# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# Modified by Donald F. Ferguson, Columbia University, 2018


# Import some frameworks that help us implement a web application.
from flask import Flask, request, make_response

import string

# The external file that implements my check and track correction functions.
import words
import json

#
# The main running program is the Flask application engine.
# We register URL endpoint functions below.
# There are some static content directories for serving HTML, CSS, JavaScript, etc.
#
app = Flask(__name__,
            static_url_path='',
            static_folder='web/static',
            template_folder='web/templates')


#
#
#
@app.route('/api/file', methods=['GET'])
def api_file():
    print("input = ", str(request.args))
    f = request.args['file']
    print("file = ", f)

    rsp = json.dumps({"status" : "CORRECT"})

    response = make_response(rsp)

    response.headers['Content-Type'] = 'application/json'

    return response



if __name__ == '__main__':
    app.run(debug=False)
