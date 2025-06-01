import sqlite3
from datetime import datetime

conn = sqlite3.connect('scan_results.db')
cur = conn.cursor()

cur.execute("INSERT INTO scans (ip, port, service, status, scan_time) VALUES (?, ?, ?, ?, ?)",
            ('127.0.0.1', 80, 'http', 'open', datetime.now().isoformat()))

conn.commit()
conn.close()
print("✅ Sample scan record added.")
