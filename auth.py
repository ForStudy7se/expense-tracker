from flask import Blueprint, render_template, request, redirect, session, url_for
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            session['user_id'] = user.id
            return redirect('/')
        return 'Invalid credentials'
    return render_template('login.html')

from flask import flash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 🔍 Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("⚠️ Username already taken. Please choose another.", "error")
            return redirect(url_for('auth_bp.register'))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()
        flash("✅ Registered successfully! Please log in.", "success")
        return redirect(url_for('auth_bp.login'))

    return render_template('register.html')