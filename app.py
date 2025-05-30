from flask import Flask, render_template, send_file
import sqlite3
import csv
from datetime import datetime

app = Flask(__name__)

# Route to show dashboard
@app.route('/')
def dashboard():
    conn = sqlite3.connect('../scan_results.db')  # Adjust path if needed
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans")
    results = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', results=results)

# Route to export as CSV
@app.route('/export')
def export_csv():
    conn = sqlite3.connect('../scan_results.db')
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
