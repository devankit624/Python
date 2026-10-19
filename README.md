🏦 Bank Management System

A simple and interactive Bank Management System built using Python, Streamlit, and JSON for storing account information. This project provides a user-friendly web interface to manage bank accounts and perform basic banking operations.

📸 Screenshots
Dashboard

!Bank Management System Dashboard

Create Account

!Create Account


Note: These are placeholder images. Replace them with actual screenshots of your running application for the best presentation on GitHub.
✨ Features
🆕 Create Account — Create an account with name, age, email, and PIN.
💰 Deposit Money — Add money to an existing account.
💸 Withdraw Money — Withdraw money after PIN verification and balance checks.
👤 Account Details — View account information after authentication.
✏️ Update Details — Update your name and email.
🗑️ Delete Account — Delete an account after verification and confirmation.
📊 Dashboard — View account information and total balances.
💾 JSON Storage — Save account data in a local JSON file.
🖥️ Streamlit Interface — Use banking features through a web interface.
🛠️ Technologies Used
Python — Core programming language.
Streamlit — Interactive web application framework.
JSON — Local data storage.
Pathlib — File and directory handling.
📁 Project Structure
Bank-Management-System/
│
├── app.py
├── data.json
├── requirements.txt
└── README.md

File	Description
app.py	Main Streamlit application
data.json	Stores bank account records
requirements.txt	Lists project dependencies
README.md	Project documentation
⚙️ Installation and Setup
1. Clone the repository
git clone https://github.com/devankit624/Bank-Management-System.git

2. Navigate to the project directory
cd Bank-Management-System

3. Install dependencies
pip install -r requirements.txt

4. Initialize the JSON database

Create a file named data.json containing:

[]


If you already have account records, keep your existing valid JSON data instead.

5. Run the application
streamlit run app.py


The application will open in your browser, usually at:

http://localhost:8501

📦 Requirements

Add the following to requirements.txt:

streamlit

💾 Data Storage

Account information is stored in data.json. The application loads existing records when it starts and saves changes when accounts are created, updated, deleted, or when balances change.

Important: JSON storage is intended for learning and demonstration. Do not use this application to store real banking credentials or financial information.

🔐 Security Notice

This project is an educational demonstration and is not suitable for production banking.

PINs should be securely hashed rather than stored as plain text.
Financial calculations should use integer paise or Python's Decimal.
Account data should be protected by proper authentication and authorization.
A transactional database should be used for a multi-user deployment.
Never commit real account information, PINs, or other secrets to GitHub.
🚀 Future Improvements
Transaction history and receipts.
Search and filter accounts.
Password hashing and improved authentication.
Export account statements.
SQLite or PostgreSQL database integration.
Responsive interface and additional dashboard charts.
👨‍💻 Author

Devankit

GitHub: @devankit624
📄 License

This project is available for educational purposes. Add an appropriate open-source license if you want others to reuse, modify, and distribute your code.

⭐ If you find this project useful, consider giving the repository a star!