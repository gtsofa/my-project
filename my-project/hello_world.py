#hello_world.py
import os


from flask import Flask
app = Flask(__name__)
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))

@app.route('/')
def hello_world():
    return 'Hello World!'
    
    
if __name__ == '__main__':
    app.run()
    app.debug(True)