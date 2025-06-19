from flask import Blueprint, jsonify, request, session
from models import db, Expense

expense_api = Blueprint('expense_api', __name__, url_prefix='/api')

@expense_api.route('/expenses', methods=['GET'])
def get_expenses():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    expenses = Expense.query.filter_by(user_id=session['user_id']).all()
    return jsonify([{
        'id': e.id,
        'category': e.category,
        'amount': e.amount,
        'date': e.date,
        'note': e.note
    } for e in expenses])

@expense_api.route('/expenses', methods=['POST'])
def add_expense_api():
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    data = request.json
    exp = Expense(
        category=data['category'],
        amount=data['amount'],
        date=data['date'],
        note=data.get('note', ''),
        user_id=session['user_id']
    )
    db.session.add(exp)
    db.session.commit()
    return jsonify({'message': 'Expense added'}), 201
