# 🔐 Secure Code Review — VulnFlask

**Author:** Adithyan V  
**Language:** Python 3 | **Framework:** Flask  
**Tools:** Bandit | Manual Review | OWASP Top 10

---

## 📌 Overview

A comprehensive **static code review and security audit** performed on **VulnFlask** — an intentionally vulnerable Python/Flask web application. The audit combined automated static analysis using **Bandit** with manual code inspection techniques aligned with the **OWASP Top 10** and CWE/SANS guidelines.

**7 security vulnerabilities** were identified, documented, and remediated across 4 severity levels.

---

## 🔍 Vulnerabilities Found

| ID | Vulnerability | Severity | CWE |
|---|---|---|---|
| VUL-01 | SQL Injection | 🔴 CRITICAL | CWE-89 |
| VUL-02 | Command Injection (RCE) | 🔴 CRITICAL | CWE-78 |
| VUL-03 | Cross-Site Scripting (XSS) | 🟠 HIGH | CWE-79 |
| VUL-04 | Path Traversal | 🟠 HIGH | CWE-22 |
| VUL-05 | Hardcoded Credentials | 🟠 HIGH | CWE-798 |
| VUL-06 | Weak Password Hashing (MD5) | 🟡 MEDIUM | CWE-916 |
| VUL-07 | Debug Mode in Production | 🟡 MEDIUM | CWE-94 |

---

## 📁 Project Structure

```
Secure-Code-Review/
├── vulnerable_app.py                  # Target Flask app (intentionally vulnerable)
├── Secure_Code_Review_Report_AdithyanV.pdf   # Full audit report
└── README.md
```

---

## 📄 Audit Report

The full report (`Secure_Code_Review_Report_AdithyanV.pdf`) includes:

- Executive Summary with severity breakdown
- Scope & Methodology (Bandit + Manual Review)
- Detailed finding for each vulnerability:
  - Description
  - Vulnerable code snippet
  - Impact analysis
  - Remediated code
  - Recommendation
- Remediation Summary Table
- General Secure Coding Recommendations

---

## ⚙️ Run the Vulnerable App (in isolated environment only)

```bash
# Install dependencies
pip install flask

# Run the app
python3 vulnerable_app.py
```

> ⚠️ **WARNING:** This app is intentionally insecure. Run only in an isolated local environment. Never deploy to production or expose to the internet.

---

## 🛠️ How to Run Bandit Static Analysis

```bash
# Install bandit
pip install bandit

# Run against the vulnerable app
bandit vulnerable_app.py

# Save output to file
bandit vulnerable_app.py -f txt -o bandit_output.txt
```

---

## 🧠 Key Concepts Demonstrated

- **SQL Injection** — User input concatenated directly into SQL queries
- **Command Injection** — User input passed to shell commands via `subprocess`
- **XSS** — Unsanitized user input reflected in HTML responses
- **Path Traversal** — No validation on file paths allowing `../../` attacks
- **Hardcoded Secrets** — Credentials stored as plaintext in source code
- **Weak Cryptography** — MD5 used for password hashing (broken algorithm)
- **Insecure Configuration** — Flask debug mode enabled in production

---

## 📖 References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Bandit — Python Security Linter](https://bandit.readthedocs.io/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [Flask Security Best Practices](https://flask.palletsprojects.com/en/latest/security/)

---

## ⚠️ Legal Disclaimer

The vulnerable application in this repository was created **intentionally for educational purposes** to demonstrate common web application security flaws. Do not use any techniques demonstrated here on systems you do not own or have explicit permission to test.
