from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/name",defaults={'name' :"Anonim"})
@app.route("/name/<name>")
def name(name):
    return f"Hello {name}"

@app.route("/o_autorze")
def author():
    return render_template('author.html')

@app.route("/extract")
def extract():
    if request.method == 'POST':
        product_code = request.form.get('product_code')
        return redirect(url_for('product', code=product_code))
    return render_template('extract.html')

@app.route("/lista_produktow")
def productList():
    return render_template('product_list.html')

@app.route("/produkt")
def product():
    return render_template('product.html')

@app.route("/wykresy")
def charts():
    return render_template('charts.html')