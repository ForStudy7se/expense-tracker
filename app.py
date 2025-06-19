from flask import Flask, render_template, redirect, session, url_for
from models import db
from auth import auth_bp
from api import expense_api
from models import Expense, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db.init_app(app)
app.register_blueprint(auth_bp)
app.register_blueprint(expense_api)

@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))

    expenses = Expense.query.filter_by(user_id=session['user_id']).all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    from flask import request
    if 'user_id' not in session:
        return redirect('/login')
    if request.method == 'POST':
        new_exp = Expense(
            category=request.form['category'],
            amount=float(request.form['amount']),
            date=request.form['date'],
            note=request.form['note'],
            user_id=session['user_id']
        )
        db.session.add(new_exp)
        db.session.commit()
        return redirect('/')
    return render_template('add_expense.html')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    if 'user_id' not in session:
        return redirect('/login')
    
    expense = Expense.query.get_or_404(id)

    if expense.user_id != session['user_id']:
        return "Unauthorized", 403

    db.session.delete(expense)
    db.session.commit()
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/login')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates tables based on models
    app.run(debug=True)

