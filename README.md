# PASSWORD_CHECKER
🔐 Password Breach Checker

A Python project that checks if your password has ever been exposed in a data breach using the Have I Been Pwned (HIBP) API.
It works by hashing your password with SHA-1, sending only the first 5 characters of the hash to the API (for privacy), and checking if the rest of the hash appears in leaked password databases.

📌 Features

Uses SHA-1 hashing for secure password handling.

Implements k-Anonymity model → only the first 5 hash characters are sent to the API (your password is never exposed).

Tells you how many times your password has appeared in breaches.

Simple command-line interface.

⚙️ How It Works

You enter a password.

The password is hashed using SHA-1.

The first 5 characters of the hash are sent to the HIBP API.

The API returns a list of matching hashes with counts.

Your hash’s tail is checked against the response.

If found, you get the number of times your password was leaked.

🚀 Installation & Usage
1. Clone this repository
git clone https://github.com/YashKumarSharma646/password-breach-checker.git
cd password-breach-checker

2. Install requirements

This project uses only requests:

pip install requests

3. Run the script
python password_checker.py


You’ll be prompted to enter a password, and the tool will tell you whether it has been leaked.

🛡️ Example
Enter a password: password123
✅ Oh no! "password123" was found 12034 times. You should probably change your password!

📚 Concepts Learned

Using APIs in Python.

Working with requests and parsing API responses.

Hashing with SHA-1 in Python.

Understanding the k-Anonymity privacy model.

Writing clean functions & modular code.

📌 Notes

Never share your real passwords while testing this. Use dummy or test passwords if possible.

The script does not store or log any password you enter.
