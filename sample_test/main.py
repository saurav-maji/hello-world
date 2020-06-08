from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return 'Hi %s %s tried first deployment <br/> <a href="/">Back Home</a>' % (first_name, last_name)

if __name__ == '__main__':
    app.run(host = '127.0.0.2', port = 3000)