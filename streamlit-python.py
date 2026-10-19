
import json
import random
from pathlib import Path

import streamlit as st


# ---------------- DATABASE ----------------

DATABASE = Path(__file__).parent / "data.json"


def load_data():
    if not DATABASE.exists():
        save_data([])
        return []

    try:
        with open(DATABASE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Database must contain a list of accounts.")

        return data

    except (json.JSONDecodeError, OSError, ValueError) as err:
        st.error(f"Could not load database: {err}")
        st.stop()


def save_data(data):
    try:
        temp_file = DATABASE.with_suffix(".tmp")

        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        temp_file.replace(DATABASE)
        return True

    except OSError as err:
        st.error(f"Could not save database: {err}")
        return False


def find_account(data, account_no):
    for account in data:
        if account.get("account_no") == account_no:
            return account
    return None


def verify_pin(account, pin):
    return account.get("pin") == pin


def format_money(amount):
    return f"₹{amount:,.2f}"


# ---------------- STREAMLIT CONFIG ----------------

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

if "accounts" not in st.session_state:
    st.session_state.accounts = load_data()

accounts = st.session_state.accounts


def refresh_data():
    st.session_state.accounts = load_data()


# ---------------- SIDEBAR ----------------

st.sidebar.title("🏦 My Bank")
st.sidebar.caption("Bank Management System")

page = st.sidebar.radio(
    "Choose an operation",
    [
        "Dashboard",
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Data is stored in data.json")


# ---------------- DASHBOARD ----------------

if page == "Dashboard":
    st.title("🏦 Bank Management System")
    st.write("Welcome to your banking dashboard!")

    total_accounts = len(accounts)
    total_balance = sum(
        float(account.get("balance", 0))
        for account in accounts
    )

    col1, col2 = st.columns(2)

    col1.metric("Total Accounts", total_accounts)
    col2.metric("Total Deposits", format_money(total_balance))

    st.subheader("All Accounts")

    if accounts:
        public_accounts = [
            {
                "Account Number": account["account_no"],
                "Name": account["name"],
                "Age": account["age"],
                "Email": account["email"],
                "Balance": format_money(
                    float(account.get("balance", 0))
                )
            }
            for account in accounts
        ]

        st.dataframe(
            public_accounts,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("No accounts found. Create your first account.")


# ---------------- CREATE ACCOUNT ----------------

elif page == "Create Account":
    st.title("Create a New Account")

    with st.form("create_account_form"):
        name = st.text_input("Full Name")
        age = st.number_input(
            "Age", min_value=0, max_value=120, value=18
        )
        email = st.text_input("Email Address")
        pin = st.text_input(
            "4-digit PIN", type="password", max_chars=4
        )
        confirm_pin = st.text_input(
            "Confirm PIN", type="password", max_chars=4
        )

        submitted = st.form_submit_button(
            "Create Account", use_container_width=True
        )

    if submitted:
        if not name.strip() or not email.strip():
            st.error("Name and email are required.")

        elif age < 18:
            st.error("You must be at least 18 years old.")

        elif (
            len(pin) != 4
            or not pin.isascii()
            or not pin.isdigit()
        ):
            st.error("PIN must contain exactly 4 digits.")

        elif pin != confirm_pin:
            st.error("PINs do not match.")

        else:
            account_no = random.randint(100000, 999999)

            while find_account(accounts, account_no) is not None:
                account_no = random.randint(100000, 999999)

            account = {
                "name": name.strip(),
                "age": int(age),
                "email": email.strip(),
                "pin": pin,
                "account_no": account_no,
                "balance": 0.0
            }

            updated_accounts = accounts + [account]

            if save_data(updated_accounts):
                st.session_state.accounts = updated_accounts
                st.success("Account created successfully!")
                st.code(str(account_no), language=None)
                st.warning("Save your account number securely.")


# ---------------- DEPOSIT ----------------

elif page == "Deposit Money":
    st.title("Deposit Money")

    with st.form("deposit_form"):
        account_no = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )
        amount = st.number_input(
            "Deposit Amount (₹)",
            min_value=0.0,
            value=0.0,
            step=100.0
        )
        submitted = st.form_submit_button("Deposit")

    if submitted:
        account = find_account(accounts, int(account_no))

        if account is None:
            st.error("Account not found.")

        elif amount <= 0:
            st.error("Amount must be greater than zero.")

        else:
            account["balance"] = (
                float(account.get("balance", 0)) + amount
            )

            if save_data(accounts):
                st.success(
                    f"Deposit successful! New balance: "
                    f"{format_money(account['balance'])}"
                )
            else:
                refresh_data()


# ---------------- WITHDRAW ----------------

elif page == "Withdraw Money":
    st.title("Withdraw Money")

    with st.form("withdraw_form"):
        account_no = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input(
            "Withdrawal Amount (₹)",
            min_value=0.0,
            value=0.0,
            step=100.0
        )
        submitted = st.form_submit_button("Withdraw")

    if submitted:
        account = find_account(accounts, int(account_no))

        if account is None:
            st.error("Account not found.")

        elif not verify_pin(account, pin):
            st.error("Incorrect PIN.")

        elif amount <= 0:
            st.error("Amount must be greater than zero.")

        elif amount > float(account.get("balance", 0)):
            st.error("Insufficient balance.")

        else:
            old_balance = float(account["balance"])
            account["balance"] = old_balance - amount

            if save_data(accounts):
                st.success(
                    f"Withdrawal successful! New balance: "
                    f"{format_money(account['balance'])}"
                )
            else:
                account["balance"] = old_balance
                refresh_data()


# ---------------- ACCOUNT DETAILS ----------------

elif page == "Account Details":
    st.title("Account Details")

    with st.form("details_form"):
        account_no = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )
        pin = st.text_input("PIN", type="password", max_chars=4)
        submitted = st.form_submit_button("View Details")

    if submitted:
        account = find_account(accounts, int(account_no))

        if account is None:
            st.error("Account not found.")

        elif not verify_pin(account, pin):
            st.error("Incorrect PIN.")

        else:
            st.subheader("Your Account")

            st.write("**Name:**", account["name"])
            st.write("**Age:**", account["age"])
            st.write("**Email:**", account["email"])
            st.write("**Account Number:**", account["account_no"])
            st.metric(
                "Current Balance",
                format_money(float(account.get("balance", 0)))
            )


# ---------------- UPDATE DETAILS ----------------

elif page == "Update Details":
    st.title("Update Account Details")

    with st.form("update_form"):
        account_no = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )
        pin = st.text_input("Current PIN", type="password", max_chars=4)
        name = st.text_input("New Name (optional)")
        email = st.text_input("New Email (optional)")
        submitted = st.form_submit_button("Update Details")

    if submitted:
        account = find_account(accounts, int(account_no))

        if account is None:
            st.error("Account not found.")

        elif not verify_pin(account, pin):
            st.error("Incorrect PIN.")

        elif not name.strip() and not email.strip():
            st.info("Enter a new name or email to update.")

        else:
            old_name = account["name"]
            old_email = account["email"]

            if name.strip():
                account["name"] = name.strip()

            if email.strip():
                account["email"] = email.strip()

            if save_data(accounts):
                st.success("Account details updated successfully!")
            else:
                account["name"] = old_name
                account["email"] = old_email
                refresh_data()


# ---------------- DELETE ACCOUNT ----------------

elif page == "Delete Account":
    st.title("Delete Account")

    st.warning(
        "Deleting an account permanently removes its record "
        "from the JSON database."
    )

    with st.form("delete_form"):
        account_no = st.number_input(
            "Account Number",
            min_value=100000,
            max_value=999999,
            step=1
        )
        pin = st.text_input("PIN", type="password", max_chars=4)
        confirm = st.checkbox(
            "I understand that this action cannot be undone."
        )
        submitted = st.form_submit_button("Delete Account")

    if submitted:
        account = find_account(accounts, int(account_no))

        if account is None:
            st.error("Account not found.")

        elif not verify_pin(account, pin):
            st.error("Incorrect PIN.")

        elif not confirm:
            st.error("Please confirm account deletion.")

        else:
            updated_accounts = [
                item for item in accounts
                if item["account_no"] != int(account_no)
            ]

            if save_data(updated_accounts):
                st.session_state.accounts = updated_accounts
                st.success("Account deleted successfully!")
