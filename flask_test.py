from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return "Hello world! \nIT WORKED, IT WORKED!!"

app.run(port = '8000')
