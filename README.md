# 🔐 PassGuard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

A powerful Python-based command-line application for generating secure passwords and checking their strength, including detection of data breaches. Keep your digital life secure! 🛡️

## ✨ Features

- **🔑 Password Generation**: Create strong, random passwords with customizable length
- **🧠 Advanced Strength Checking**: Leverages the zxcvbn library for sophisticated analysis, detecting common patterns, dictionary words, and keyboard sequences
- **🚨 Breach Detection**: Instantly checks if your password has been compromised in known data breaches
- **🎨 User-Friendly Interface**: Clean, menu-driven console application with colorful output
- **⚡ Fast & Secure**: Efficient algorithms with privacy-preserving API calls

## 🏗️ How It Was Created

This project was crafted with Python 3, following modular design principles. The development process involved:

1. **Core Functionality**: Started with basic password generation and simple strength checks
2. **Advanced Analysis**: Integrated zxcvbn for professional-grade password evaluation
3. **Security Enhancement**: Added breach checking using secure API practices
4. **UI/UX Polish**: Implemented a beautiful console interface with colors and formatting

### 📁 Project Structure

```
Password-Checker/
├── main.py              # Main application entry point
├── password_generator.py # Password creation logic
├── password_checker.py   # Strength analysis with zxcvbn
├── breach_checker.py     # Have I Been Pwned API integration
├── utils.py             # Helper functions and styling
└── README.md           # This file
```

## 🔗 API Used

**Have I Been Pwned API** - The gold standard for breach detection:
- 🔒 **Privacy-First**: Uses k-anonymity - only sends first 5 characters of SHA-1 hash
- 📊 **Comprehensive**: Access to millions of breached passwords
- 🚀 **Fast**: Optimized for quick lookups
- 📖 [API Documentation](https://haveibeenpwned.com/API/v3)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Internet connection for breach checking

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/password-checker.git
   cd password-checker
   ```

2. **Install dependencies**
   ```bash
   pip install zxcvbn requests
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

## 📖 Usage

Launch the app and navigate the intuitive menu:

```
╔══════════════════════════════════════╗
║             Hoofdmenu                ║
╠══════════════════════════════════════╣
║  1. Password Generator               ║
║  2. Password Checker                 ║
║  3. Close                            ║
╚══════════════════════════════════════╝
```

### 🔑 Password Generator
Generate secure passwords with custom length (minimum 8 characters).

### 🔍 Password Checker
Analyze existing passwords for:
- Strength score (0-4 scale)
- Detailed improvement suggestions
- Breach status with red alerts ⚠️

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `zxcvbn` | 4.5.0+ | Advanced password strength estimation |
| `requests` | 2.25.0+ | HTTP client for API calls |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, open an issue first to discuss what you would like to change.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

**Made with ❤️ for cybersecurity enthusiasts**