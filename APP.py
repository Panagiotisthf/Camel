from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Dashboard')
def Dashboard():
    return render_template('Dashboard.html')

@app.route('/Cashflow')
def CashFlow():
    return render_template('Cashflow.html')

@app.route('/Aggreements')
def Aggreements():
    return render_template('Aggreements.html')

@app.route('/Contracts')
def Contracts():
    return render_template('Contracts.html')

@app.route('/Expenses')
def Expenses():
    return render_template('Expenses.html')

@app.route('/Suppliers')
def Suppliers():
    return render_template('Suppliers.html')

@app.route('/Agents')
def Agents():
    return render_template('Agents.html')
@app.route('/Cars')
def Cars():
    return render_template('Cars.html')

if __name__ == '__main__':
    app.run(debug=True)