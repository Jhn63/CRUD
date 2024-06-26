from flask import Flask, render_template
from store import StoreManager

app = Flask(__name__)
db = StoreManager()

@app.route('/')
@app.route('/main')
def main_page():
    return render_template('main.html')

@app.route('/clients')
def clients_page():
    result = db.search_tuples(table='cliente')
    return render_template('clients.html', result=result)

@app.route('/storage')
def storage_page():
    result = db.search_tuples(table='produto')
    return render_template('storage.html', result=result)
