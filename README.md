# 🔐 Decode Lab Cybersecurity Internship

A collection of cybersecurity projects developed as part of my **Cybersecurity Internship at Decode Labs**, focusing on practical Python programming, security concepts, and problem-solving.

---

# 🔑 Project 1: Password Strength Checker

> 🛡️ A simple Python-based password strength checker developed as part of my cybersecurity internship at Decode Labs.

## 📌 Project Overview

This program evaluates the strength of a password based on several security-related criteria and classifies it as **Weak, Medium, or Strong**.

It also provides suggestions to help improve password strength when specific requirements are missing.

## ✨ Features

- 📏 Checks password length
- 🔠 Detects uppercase letters
- 🔡 Detects lowercase letters
- 🔢 Detects numbers
- 🔣 Detects special characters
- 📊 Calculates a password strength score
- 💡 Provides suggestions for improvement
- 🛡️ Classifies passwords as **Weak, Medium, or Strong**

## 🛠️ Technologies Used

- 🐍 Python
- 🔤 String handling
- 🔀 Conditional statements
- 🔁 Loops
- ✅ Boolean logic

## 🧠 Concepts Practiced

- ⌨️ User input
- 🔤 String methods
- 🔀 `if`, `elif`, and `else`
- 🔁 `for` loops
- ✅ Boolean variables
- 📊 Conditional scoring
- 🔐 Basic cybersecurity concepts

## 🚀 How to Run

1. Make sure **Python** is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in **VS Code** or another Python-supported editor.
4. Run: `python "Password Strength Checker.py"`
5. Enter a password when prompted.

## 🧪 Example

| Strength | Description |
|---|---|
| 🔴 **Weak** | Lacks several required characteristics |
| 🟡 **Medium** | Meets some of the requirements |
| 🟢 **Strong** | Meets all the checked requirements |

## 🎓 Internship

This project was completed as **Project 1** during my **Cybersecurity Internship at Decode Labs**.

---

# 🔐 Project 2: Basic Encryption & Decryption

> 🛡️ A simple Python-based encryption and decryption program demonstrating the basic concept of data confidentiality using the **Caesar Cipher**.

## 📌 Project Overview

This program demonstrates the basic process of **encryption and decryption** by transforming user-provided text using a Caesar cipher.

The user enters a message and a **shift key**. The program encrypts the text by shifting alphabetic characters and then decrypts the encrypted text back to its original form.

## ✨ Features

- ⌨️ Takes text input from the user
- 🔑 Accepts a user-defined shift key
- 🔒 Encrypts text using the Caesar Cipher
- 🔓 Decrypts the encrypted text
- 🔠 Supports uppercase and lowercase letters
- ␠ Preserves spaces and other non-alphabetic characters
- 📤 Displays both encrypted and decrypted output

## 🛠️ Technologies Used

- 🐍 Python
- 🔤 String handling
- 🔀 Conditional statements
- 🔁 `for` loops
- 🔢 Character encoding and decoding
- ➗ Modulo operator `%`

## 🧠 Concepts Practiced

- ⌨️ User input
- 📦 Variables
- 🔤 Strings
- 🔁 `for` loops
- 🔀 `if`, `elif`, and `else`
- 🔢 `ord()` function
- 🔤 `chr()` function
- ➗ Modulo `%`
- 🧩 String building
- 🔐 Caesar Cipher
- 🔒 Encryption and decryption
- 🛡️ Data confidentiality

## ⚙️ How It Works

**Plaintext** ➡️ 🔒 **Encryption** ➡️ **Ciphertext** ➡️ 🔓 **Decryption** ➡️ **Plaintext**

A shift key determines how far each alphabetic character is moved.

Example with a shift key of **3**:

**HELLO** ➡️ 🔒 **KHOOR** ➡️ 🔓 **HELLO**

## 🚀 How to Run

1. Make sure **Python** is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in **VS Code** or another Python-supported editor.
4. Run: `python "Basic_Encryption_Decryption.py"`
5. Enter the text you want to encrypt.
6. Enter a shift key when prompted.
7. The program will display the encrypted and decrypted text.

## 🧪 Example

| Input | Output |
|---|---|
| Text: `HELLO` | Encrypted Text: `KHOOR` |
| Shift Key: `3` | Decrypted Text: `HELLO` |

## 🎓 Internship

This project was completed as **Project 2** during my **Cybersecurity Internship at Decode Labs**.

---

# 🎣 Project 3: Phishing Awareness Analysis

> 🛡️ A simple Python-based phishing awareness analyzer developed as part of my cybersecurity internship at Decode Labs.

## 📌 Project Overview

This program analyzes an email or message for common phishing indicators and identifies suspicious characteristics that may indicate a phishing attempt.

It checks the message for suspicious keywords, links, requests for sensitive information, urgent actions, authority-related terms, and potentially dangerous attachment types.

The program then calculates a risk score and classifies the message as **Safe, Suspicious, or Malicious**.

## ✨ Features

- 📩 Analyzes user-provided emails or messages
- 🚨 Detects suspicious keywords
- 🔗 Checks for suspicious links
- 🔐 Detects requests for sensitive information
- ⏰ Identifies urgent action requests
- 👤 Detects possible authority impersonation
- 📎 Checks for potentially dangerous attachment types
- 📊 Calculates a phishing risk score
- ⚠️ Classifies messages as **Safe, Suspicious, or Malicious**
- 📋 Displays detected red flags
- 💡 Provides a **Pause → Verify → Report** safety recommendation

## 🛠️ Technologies Used

- 🐍 Python
- 🔤 String handling
- 🔀 Conditional statements
- 🔁 `for` loops
- 📋 Lists
- ✅ Boolean logic
- 📊 Risk scoring
- 🛡️ Phishing awareness concepts

## 🧠 Concepts Practiced

- ⌨️ User input
- 🔤 String methods
- 🔀 `if`, `elif`, and `else`
- 🔁 `for` loops
- 📋 Lists
- 🔎 Keyword matching
- 🔗 Link detection
- 🔐 Sensitive information detection
- 📊 Conditional risk scoring
- 🚨 Phishing red flags
- 🛡️ Threat analysis
- 👤 Social engineering awareness

## ⚙️ How It Works

The program follows a simple phishing analysis process:

**📩 Message Input** ➡️ 🔍 **Analyze Message** ➡️ 🚨 **Detect Red Flags** ➡️ 📊 **Calculate Risk Score** ➡️ ⚠️ **Determine Risk Level**

The program checks the message for different phishing indicators. Each detected indicator contributes to the overall risk score.

Based on the final score, the program classifies the message as:

- 🟢 **Safe** — No obvious red flags detected
- 🟡 **Suspicious** — Some suspicious characteristics detected
- 🔴 **Malicious** — Multiple high-risk indicators detected

## 🚀 How to Run

1. Make sure **Python** is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in **VS Code** or another Python-supported editor.
4. Run: `python "Phishing Awareness Analyzer.py"`
5. Enter an email or message when prompted.
6. The program will display the risk level, detected red flags, risk score, and safety recommendation.

## 🧪 Example

| Test Message | Expected Risk Level |
|---|---|
| 🚨 Message containing multiple urgent requests, suspicious links, and sensitive-information requests | 🔴 **Malicious** |
| ⚠️ Message containing a suspicious link or keyword | 🟡 **Suspicious** |
| 🟢 Normal everyday message without suspicious indicators | 🟢 **Safe** |

## 🎓 Internship

This project was completed as **Project 3** during my **Cybersecurity Internship at Decode Labs**.

---

# 👩‍💻 Author

**Karishma**

🎓 **Program:** BSCS  
🏫 **University:** Air University Islamabad  
💻 **Role:** Cybersecurity Intern  
🏢 **Organization:** Decode Labs

---

⭐ *This repository documents my learning journey and practical projects completed during my cybersecurity internship.*
