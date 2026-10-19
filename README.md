🏦 Bank Management System

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
<img src="https://img.shields.io/badge/Database-JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Status-Active-2EA44F?style=for-the-badge" alt="Project status">
</p>

<p align="center">
A simple, interactive banking application built with <b>Python</b>, <b>Streamlit</b>, and <b>JSON</b>.
<br>
Create accounts, manage balances, and perform banking operations through a clean web interface.
</p>

<p align="center">
<a href="#-features">Features</a> •
<a href="#-screenshots">Screenshots</a> •
<a href="#-installation">Installation</a> •
<a href="#-author">Author</a>
</p>

✨ Features
Feature	Description
🆕 Account Creation	Create accounts with personal details and a PIN.
💰 Deposit Money	Add money and update account balances.
💸 Withdraw Money	Withdraw funds after PIN and balance verification.
👤 Account Details	View account information securely after PIN verification.
✏️ Update Details	Update account name and email.
🗑️ Delete Account	Remove accounts after verification and confirmation.
📊 Dashboard	View accounts and total balances.
💾 JSON Storage	Save account data locally in a JSON file.
📸 Screenshots

<p align="center">
<b>🏠 Dashboard</b>
<br><br>
<img src="screenshots/dashboard.png" alt="Bank Management System Dashboard" width="850">
</p>

<p align="center">
<b>🆕 Create Account</b>
<br><br>
<img src="screenshots/create-account.png" alt="Create Account Page" width="850">
</p>

<p align="center">
<b>👤 Account Details</b>
<br><br>
<img src="screenshots/account-details.png" alt="Account Details Page" width="850">
</p>

Note: Add your real application screenshots to the screenshots directory. GitHub cannot display local images that have not been uploaded to the repository.
🛠️ Tech Stack

<p>
<img src="https://skillicons.dev/icons?i=python" alt="Python" height="45">
&nbsp;
<img src="https://skillicons.dev/icons?i=git" alt="Git" height="45">
</p>

Python — Application logic and banking operations.
Streamlit — Interactive web interface.
JSON — Persistent local data storage.
Pathlib — File path handling.
📂 Project Structure
Bank-Management-System/
│
├── app.py                  # Main Streamlit application
├── data.json               # Account database
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
└── screenshots/
    ├── dashboard.png
    ├── create-account.png
    └── account-details.png

🚀 Installation
1. Clone the repository
git clone https://github.com/devankit624/Bank-Management-System.git

2. Navigate to the project folder
cd Bank-Management-System

3. Install dependencies
pip install -r requirements.txt

4. Initialize the database

Create data.json with an empty JSON list if the file does not already contain valid account data.

[]

5. Run the application
streamlit run app.py


Open the local URL displayed in your terminal, usually:

http://localhost:8501

📦 Requirements

Your requirements.txt should contain:

streamlit

💾 Data Storage

Account records are stored in data.json. The application reads the file on startup and saves successful account and balance changes.

Example database structure:

[
  {
    "name": "Example User",
    "age": 22,
    "email": "user@example.com",
    "pin": "1234",
    "account_no": 456789,
    "balance": 5000.0
  }
]


Use only fictional example data in public repositories.

🔒 Security Notice

This project is intended for educational purposes. The current implementation stores PINs in plain text and is not suitable for real banking.

For production use, implement secure PIN hashing, proper authentication and authorization, exact financial arithmetic, and a transactional database.

🔮 Future Improvements
📜 Transaction history
📈 Interactive financial charts
🔐 Secure authentication
🧾 Downloadable account statements
🗄️ SQLite or PostgreSQL integration
☁️ Online deployment
👨‍💻 Author

<p align="center">
<img src="https://img.shields.io/badge/Author-Devankit-blueviolet?style=for-the-badge" alt="Author Devankit">
<br><br>
<a href="https://github.com/devankit624">
<img src="https://img.shields.io/badge/GitHub-devankit624-181717?style=for-the-badge&logo=github" alt="GitHub Profile">
</a>
</p>

GitHub: @devankit624

📄 License

This project is intended for learning and educational use. Add a LICENSE file to specify the terms under which others may use, modify, or distribute the project.

<p align="center">
⭐ <b>If you find this project useful, consider starring the repository!</b>
<br><br>
Made with ❤️ using Python and Streamlit.
</p>
