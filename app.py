from msilib.schema import Binary


from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'