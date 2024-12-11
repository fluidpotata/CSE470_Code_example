from flask import Flask,render_template
import Models.basic
app = Flask(__name__)

@app.route('/')
def hello():
    sample=Models.basic.dataCollect()
    return render_template('index.html', data=sample)

if __name__ == '__main__':
    app.run(debug=True)