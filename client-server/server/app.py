from flask import Flask,jsonify
from flask_cors import CORS

import Models.basic
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello():
    return "Server running! Api on /api"


@app.route('/api')
def api():
    sample=Models.basic.dataCollect()
    return jsonify(sample)

if __name__ == '__main__':
    app.run(debug=True)