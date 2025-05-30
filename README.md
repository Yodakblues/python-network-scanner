# 🕵️‍♂️ Python Network Scanner Dashboard

This project is a full-featured Python-based network scanning tool with a web dashboard. It performs port scanning, detects running services and OS using Nmap, and stores scan results in SQLite. The web interface allows users to visualize and manage scan results easily.

---

## 🚀 Features

- 🔍 Port scanning (with socket)
- 🧠 Service and OS detection (via Nmap)
- 🗃 Results stored in SQLite database
- 🌐 Flask-powered web dashboard
- 🧾 Report export to `.txt` file

---

## 🛠 Technologies

- Python 3
- Nmap (`python-nmap`)
- SQLite3
- Flask (for the dashboard)

---

## 📦 Installation

### Clone the repo

```bash
git clone https://github.com/Yodakblues/python-network-scanner.git
cd python-network-scanner

Install requirements:
pip3 install -r requirements.txt

Or manually install:
pip3 install flask python-nmap

⚡ Usage
Run a full scan:

sudo python3 scanner_full.py --target 127.0.0.1 --start-port 20 --end-port 100

    ⚠️ Nmap features like OS detection require root privileges.

Launch the dashboard:

python3 app.py

Then open in your browser:

http://127.0.0.1:5000

📁 Project Structure

scanner_dashboard/
│
├── scanner_full.py           # Main scanner script
├── scan_results.db           # SQLite DB (auto-generated)
├── app.py                    # Flask dashboard app
├── requirements.txt          # Python dependencies
├── templates/
│   └── dashboard.html        # Web UI for dashboard
├── static/
│   └── (optional CSS/JS)
└── scan_report_<ip>.txt      # Generated scan report

✅ TODO

Basic port scanning

Nmap integration

SQLite storage

Flask dashboard

Add export as CSV/JSON

    Pagination for scan logs

👤 Kankomah (Yodakblues)

📧 [yodakblues75@gmail.com]

📄 License

This project is open-source and available under the MIT License.


---

