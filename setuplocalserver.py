from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Just for setup local server"

if __name__=='__main__':
    app.run(debug=True, port=4555)
