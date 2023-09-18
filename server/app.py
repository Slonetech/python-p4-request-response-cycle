# server/app.py
import os
from flask import Flask, request, current_app,g

app = Flask(__name__)

app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    return f'''<h1>The host for this page is {host}</h1>
               <h2>The name of this application is {appname}</h2>
               <h3>The path of this application is {g.path}</h3>'''

status_code = 200
headers = {'Content-Type': 'text/html'}
'this application only runs if the script is executed directly from the Python interpreter and not used as an imported module.'
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
