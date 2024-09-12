# **0x00. Personal Data - Backend Project**

## **Project Overview**
This project focuses on the secure handling of personal data in backend systems. It covers key concepts such as **Personally Identifiable Information (PII)**, **logging** with obfuscation of sensitive data, **password encryption**, and **authentication** using environment variables to connect to a secure MySQL database. 

The tasks in this project ensure compliance with security best practices and demonstrate how to securely manage and log sensitive user data, such as passwords, emails, phone numbers, and more.

---

## **Table of Contents**
- [Project Overview](#project-overview)
- [Learning Objectives](#learning-objectives)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Modules Description](#modules-description)
  - [filtered_logger.py](#filtered_loggerpy)
  - [encrypt_password.py](#encrypt_passwordpy)
- [Requirements](#requirements)
- [Resources](#resources)

---

## **Learning Objectives**
By the end of this project, I learned the following:
1. Understanding what **Personally Identifiable Information (PII)** is and how to handle it.
2. Implementing log filtering to **obfuscate PII fields** from logs.
3. Encrypt passwords using the **bcrypt** package and validate passwords securely.
4. Authenticate to a database using environment variables.
5. Log user data with **secure formatting** and safely manage sensitive information in logs.
6. Connecting securely to a MySQL database without exposing credentials in the code.

---

## **Features**
- **Secure Logging**: Logging of sensitive fields is obfuscated using a custom `RedactingFormatter`.
- **Database Connection**: Securely connect to a MySQL database using environment variables for credentials.
- **Password Encryption**: Salt and hash passwords using `bcrypt` to ensure security.
- **Password Validation**: Verify user credentials by securely comparing a hashed password with the original.
- **Formatted Logs**: Log user data with specific formatting and ensure that sensitive fields such as passwords, emails, and phone numbers are hidden.

---

## **Installation and Setup**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Gideon-Phiri/alx-backend-user-data.git
   cd 0x00-personal_data
   ```

2. **Install Dependencies**
   - You will need **Python 3.7+** and **pip** installed.
   - Install the required Python packages:
     ```bash
     pip install mysql-connector-python bcrypt
     ```

3. **Set Up MySQL Database**
   - Create a database and a `users` table following the schema provided in the project.
   - Make sure to set environment variables for database credentials:
     ```bash
     export PERSONAL_DATA_DB_USERNAME='root'
     export PERSONAL_DATA_DB_PASSWORD='your_password'
     export PERSONAL_DATA_DB_HOST='localhost'
     export PERSONAL_DATA_DB_NAME='your_db_name'
     ```

4. **Run the Project**
   - To run the logging and filtering tasks:
     ```bash
     python3 ./main.py
     ```
   - To test password hashing and validation:
     ```bash
     python3 ./main.py
     ```

---

## **Usage**

### **1. Logging with PII Obfuscation**
- **`filtered_logger.py`** handles logging user information securely by hiding sensitive fields such as names, emails, passwords, and more.
- Logs are output in a custom format that includes timestamps and log levels.

### **2. Password Encryption and Validation**
- **`encrypt_password.py`** hashes passwords and securely checks if a given password matches the stored hash.
- Use `hash_password` to encrypt passwords and `is_valid` to validate them.

---

## **Code Structure**

```plaintext
0x00-personal_data/
├── filtered_logger.py  # Handles logging, PII obfuscation, and DB connection
├── encrypt_password.py # Handles password encryption and validation
├── README.md           # Documentation of the project
└── main.py             # Example usage of the modules
```

---

## **Modules Description**

### **1. `filtered_logger.py`**
This module handles logging securely by obfuscating sensitive fields such as names, emails, passwords, and phone numbers. It includes functions for database connection and log filtering.

- **Functions**:
  - `filter_datum(fields: List[str], redaction: str, message: str, separator: str)`: Obfuscates sensitive fields in the log message using regex.
  - `get_logger() -> logging.Logger`: Returns a logger with custom PII obfuscation.
  - `get_db() -> mysql.connector.connection.MySQLConnection`: Connects securely to a MySQL database using environment variables.
  - `main()`: Logs user data retrieved from the `users` table with sensitive fields obfuscated.

- **Classes**:
  - `RedactingFormatter`: A custom logging formatter that redacts sensitive information from log messages.

### **2. `encrypt_password.py`**
This module is responsible for hashing and validating passwords using **bcrypt**.

- **Functions**:
  - `hash_password(password: str) -> bytes`: Hashes a given password with a salt.
  - `is_valid(hashed_password: bytes, password: str) -> bool`: Validates if a given password matches the hashed password.

---

## **Requirements**

- **Python**: 3.7 or higher.
- **Pip**: Python package manager.
- **Python Packages**:
  - **bcrypt**: For password hashing and validation.
  - **mysql-connector-python**: For MySQL database connections.
- **Operating System**: **Ubuntu 18.04 LTS**.
- All Python files must be executable.

---

## **Resources**

- **What Is PII, non-PII, and Personal Data?**
- **Logging Documentation**
- **Bcrypt Package**
- **Logging to Files, Setting Levels, and Formatting**
- **Python MySQL Connector Documentation**

For more details on these topics, refer to the above resources.

---

## **Author**
- **Gideon Phiri** - Software Engineer

Feel free to contribute, raise issues, or suggest improvements to this project. This project demonstrates best practices for handling personal data securely in backend systems.
