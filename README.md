# 🔐 AuthTester

**AuthTester** is an educational Python web authentication testing script using HTTP POST requests.

---

## ⚠️ Disclaimer
This tool is intended for educational purposes only and must only be used on systems that you own or have explicit permission to test.

---

## ✨ Features

- Tests web login forms using HTTP POST requests
- Fully customizable:
  - Login page URL
  - Username
  - Failure message text
  - Password wordlist

---

## 🛠️ Requirements

- Python 3.x
- `requests` library

Install the required library:

```bash
pip install requests
```
## 🚀 Usage
```bash
cd auth-tester
python3 AuthTester.py
```
You will be prompted to enter:

Login Page URL

Username

Failure Message Text (text shown when login fails)

Wordlist Path

## 📌 Example
```text
Enter Login Page Url: http://127.0.0.1/dvwa/login.php

Enter Username: admin

Enter Failure Message Text: Login failed

Enter Wordlist Path: /home/kali/wordlists/passwords.txt
```

## ✅ Successful Result
```text
[+] Found the password --> admin123
```

## ⚙️ Customization Notes

Make sure the field names in the script match the target login form:
```text
"username"

"password"
```
Some applications may use different names such as:
```text
uname

pass
```
Modify them accordingly in the code.

## 🔒 Legal & Ethical Notice

This project is intended only for learning and authorized penetration testing.

## 👨‍💻 Author

Ahmed Ramadan Mohamed

Information Security Researcher | Ethical Hacking Enthusiast
