# 📈 Stock Portfolio Tracker

A simple and interactive Stock Portfolio Tracker built using Python.  
This project allows users to enter stock symbols and quantities, calculate investment values, and optionally save portfolio details into a CSV file.

---

## ✨ Features

- 📊 Track multiple stock investments
- 💰 Calculate total portfolio value
- 🧮 Uses hardcoded stock prices
- 📁 Export portfolio data to CSV
- ✅ Input validation for stock symbols
- 🎯 Beginner-friendly Python project

---

## 🛠 Technologies Used

- Python 3
- CSV File Handling

---

## 📚 Python Concepts Used

- Dictionaries
- Loops
- Conditional Statements
- Functions
- Input/Output
- Arithmetic Operations
- File Handling

---

## 📂 Available Stocks

| Stock Symbol | Price |
|--------------|-------|
| AAPL | $180 |
| TSLA | $250 |
| GOOG | $140 |
| MSFT | $320 |
| AMZN | $150 |

---

## ▶ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/stock-portfolio-tracker.git
```

### 2. Open Project Folder

```bash
cd stock-portfolio-tracker
```

### 3. Run the Program

```bash
python stock_tracker.py
```

---

## 🖥 Example Output

```text
=============================================
📈 STOCK PORTFOLIO TRACKER 📈
=============================================

Available Stocks:
AAPL : $180
TSLA : $250
GOOG : $140

How many stocks do you want to add? 2

Stock #1
Enter stock symbol: AAPL
Enter quantity: 3

Stock #2
Enter stock symbol: TSLA
Enter quantity: 2

📊 PORTFOLIO SUMMARY

AAPL | Quantity: 3 | Investment: $540
TSLA | Quantity: 2 | Investment: $500

💰 Total Investment Value: $1040
```

---

## 📁 CSV Export

If the user selects `yes`, the program creates:

```text
portfolio.csv
```

containing portfolio details.

---

## 🚀 Future Improvements

- Real-time stock prices using APIs
- GUI version with Tkinter
- Portfolio profit/loss tracking
- Database integration
- Charts and analytics

.
