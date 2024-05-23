from flask import Flask, request, session, redirect, url_for, render_template
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

users = {
    'carlos': 'password123'
}

# Function to generate a 3-digit random MFA code
def generate_mfa_code():
    return '{:03d}'.format(random.randint(0, 999))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            session['mfa_code'] = generate_mfa_code()
            session['mfa_attempts'] = 0
            return redirect(url_for('login2'))
        return render_template('login.html', message='Invalid credentials')
    return render_template('login.html')

@app.route('/login2', methods=['GET', 'POST'])
def login2():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        mfa_code = request.form['mfa_code']
        session['mfa_attempts'] += 1
        if session['mfa_attempts'] > 2:
            session.pop('username', None)
            session.pop('mfa_code', None)
            session.pop('mfa_attempts', None)
            return redirect(url_for('login', message='Too many attempts. You have been logged out.'))
        
        if mfa_code == session['mfa_code']:
            return redirect(url_for('dashboard'))
        return render_template('login2.html', message='Invalid MFA code')
    
    return render_template('login2.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    return f'Welcome to your dashboard, {session["username"]}!'

@app.route('/')
def home():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
