from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/ratesherman')
def ratesherman():
    return render_template('ratesherman.html')

@app.route('/rateusdan')
def rateusdan():
    return render_template('rateusdan.html')

if __name__ == '__main__':
    app.run(debug=True)
