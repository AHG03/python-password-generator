# Simple Python Password Generator

A lightweight, customizable Python script that generates secure, random passwords based on user-defined criteria.

## 🚀 Features

* **Custom Length:** Choose exactly how long you want your password to be.
* **Character Variety:** Toggle between uppercase letters, numbers, and special characters.
* **Guaranteed Inclusion:** Ensures at least one character of each selected type is included in the result.
* **Security:** Uses Python’s `random` module to shuffle characters for unpredictable output.

## 📋 Prerequisites

Before running the script, ensure you have Python installed on your system:

* Python 3.6 or higher

## 🛠️ Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/password-generator.git

```


2. **Navigate to the directory:**
```bash
cd password-generator

```



## 💻 Usage

Run the script using the following command in your terminal:

```bash
python password_generator.py

```

### **How it works:**

1. **Length:** Enter the desired total character count.
2. **Criteria:** Answer `y` (yes) or `n` (no) for:
* Uppercase letters ()
* Numbers ()
* Special characters ()


3. **Output:** The script will instantly print your generated password.

> [!TIP]
> If you ask for a password length of 2 but require uppercase, numbers, and special characters, the script will throw a `ValueError` to ensure your security requirements are mathematically possible.

## 📄 Example

```text
Enter password length: 12
Include upper case letters? (y/n) y
Include numbers? (y/n) y
Include special characters? (y/n) y

Generated: k8#Pz2!vL9qR

```
 
