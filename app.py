from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key'  # Needed for session management

# Database connection helper
def get_db_connection():
    conn = sqlite3.connect('college.db')
    conn.row_factory = sqlite3.Row  # Enables accessing rows as dictionaries
    return conn

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Professor login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM professors WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['professor_id'] = user['id']
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials. Please try again."
    return render_template('login.html')

# Dashboard route
@app.route('/dashboard')
def dashboard():
    if 'professor_id' not in session:
        return redirect(url_for('login'))
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('dashboard.html', students=students)

# Add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    if 'professor_id' not in session:
        return redirect(url_for('login'))
    name = request.form['name']
    division = request.form['division']
    conn = get_db_connection()
    conn.execute('INSERT INTO students (name, division) VALUES (?, ?)', (name, division))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# Mark attendance
@app.route('/mark_attendance', methods=['POST'])
def mark_attendance():
    if 'professor_id' not in session:
        return redirect(url_for('login'))
    student_id = request.form['student_id']
    date = request.form['date']
    status = request.form['status']
    conn = get_db_connection()
    conn.execute('INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)', (student_id, date, status))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
