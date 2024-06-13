from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/clients')
def clients_page():
    return render_template('clients.html')

@app.route('/storage')
def storage_page():
    return render_template('storage.html')
