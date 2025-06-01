# 🔒 Scanner Dashboard Web App

A Flask-based web application that visualizes and exports port scan results in real time. Includes user authentication, dynamic charts, and CSV export functionality.

---

## 🚀 Features

- ✅ **User Login** – Secure admin login using Flask-Login
- 📊 **Interactive Dashboard** – Visualizes scan results using charts (grouped by ports)
- 📁 **Export as CSV** – Download scan results for offline analysis
- 🔐 **Session Management** – Logout functionality for secure session control
- 📄 **Modular Code** – Clean structure for easy maintenance and scalability

---

## 🧠 Tech Stack

- **Backend:** Python, Flask, Flask-Login
- **Frontend:** HTML, Bootstrap (optional), Chart.js
- **Database:** SQLite
- **Other Tools:** Git, GitHub

---

## 📂 Project Structure

scanner_dashboard/
│
├── templates/
│ ├── login.html
│ └── dashboard.html
│
├── static/
│ └── (optional: CSS/JS files)
│
├── app.py
├── scan_results.db
├── requirements.txt
└── README.md


---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/scanner_dashboard.git
cd scanner_dashboard

2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Requirements

pip install -r requirements.txt
2. Create Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install Requirements

pip install -r requirements.txt

