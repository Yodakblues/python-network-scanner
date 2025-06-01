from flask import Flask, render_template, send_file, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import sqlite3
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy user class
class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "admin"
        self.password = "admin123"

    def __repr__(self):
        return f"{self.id}/{self.name}"

# User loader
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == "admin" and password == "admin123":
            user = User(1)
            login_user(user)
            return redirect(url_for('dashboard'))
        return "Invalid credentials"
    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Dashboard route - main page
@app.route('/')
@login_required
def dashboard():
    conn = sqlite3.connect('scan_results.db')
    cur = conn.cursor()
    
    # Get port statistics
    cur.execute("SELECT port, COUNT(*) FROM scans GROUP BY port")
    stats = cur.fetchall()

    # Get full scan results
    cur.execute("SELECT * FROM scans")
    results = cur.fetchall()

    conn.close()

    labels = [str(row[0]) for row in stats]
    data = [row[1] for row in stats]

    return render_template('dashboard.html', results=results, labels=labels, data=data)

# Export to CSV route
@app.route('/export')
@login_required
def export_csv():
    conn = sqlite3.connect('scan_results.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans")
    results = cursor.fetchall()
    conn.close()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"scan_export_{timestamp}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Target IP', 'Port', 'Service', 'OS Guess'])
        writer.writerows(results)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

