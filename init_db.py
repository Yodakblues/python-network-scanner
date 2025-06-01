import sqlite3

conn = sqlite3.connect('scan_results.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS scans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    port INTEGER,
    service TEXT,
    status TEXT,
    scan_time TEXT
)
''')

conn.commit()
conn.close()
print("✅ 'scans' table created successfully.")
