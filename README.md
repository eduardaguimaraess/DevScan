# DevScan
Modular Web Security Scanner built with Python.

# 🔍 DevScan

DevScan is a modular web vulnerability scanner built with Python using Object-Oriented Programming principles.

The project analyzes websites for common security issues such as:

- Missing HTTPS
- Missing security headers
- Server information exposure
- Insecure HTML forms

DevScan was designed with a scalable and modular architecture, allowing new security checks to be added dynamically through decorators and automatic registration.

---

# 🚀 Features

✅ HTTPS analysis  
✅ Security headers analysis  
✅ Server information exposure detection  
✅ HTML forms security analysis  
✅ Security score system  
✅ JSON report generation  
✅ Dynamic CLI interface  
✅ Modular plugin architecture  
✅ Decorators for logging and automatic check registration  

---

# 🏗️ Architecture

DevScan uses a modular architecture based on:

- Abstraction
- Inheritance
- Polymorphism
- Decorators
- Plugin-based check registration

Each vulnerability check is automatically registered using decorators and executed dynamically by the scanner engine.

---

# 📁 Project Structure

```txt
DevScan/
│
├── checks/
├── core/
├── decorators/
├── models/
├── reports/
├── tests/
├── utils/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Technologies

- Python 3
- Requests
- BeautifulSoup4
- Colorama

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/devscan.git
```

Access the project folder:

```bash
cd devscan
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

## Windows

```bash
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 💻 Usage

Run DevScan:

```bash
python main.py --url https://example.com
```

Generate JSON report:

```bash
python main.py --url https://example.com --json
```

---

# 📊 Example Output

```txt
=== DEVSCAN REPORT ===

Security Score: 50/100
Total Checks: 4

[HIGH] HTTPS Not Enabled

[MEDIUM] Missing Security Headers

[LOW] Server Information Exposure
```

---

# 📄 JSON Report Example

```json
{
  "security_score": 50,
  "total_checks": 4,
  "vulnerabilities": [
    {
      "title": "HTTPS Not Enabled",
      "severity": "HIGH"
    }
  ]
}
```

---

# 🧠 OOP Concepts Applied

- Classes and Objects
- Abstraction
- Inheritance
- Polymorphism
- Decorators
- Encapsulation
- Modular Architecture

---

# 🔮 Future Improvements

- Cookie security analysis
- PDF reports
- Multi-threaded scans
- Dashboard interface
- Advanced vulnerability checks

---

# 📜 License

This project is licensed under the MIT License.
``
---
# 📦 Required Libraries

DevScan uses the following Python libraries:

- requests
- beautifulsoup4
- colorama

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install requests
pip install beautifulsoup4
pip install colorama
```
