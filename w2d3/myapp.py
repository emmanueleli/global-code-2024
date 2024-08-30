from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello friend'

@app.route('/whereami')
def whereami():
    return 'Ghana!'

from flask import Flask, render_template
@app.route('/g')
def indexg():
    return render_template('index.html')

from flask import Flask, render_template
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')