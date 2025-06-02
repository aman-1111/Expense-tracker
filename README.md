# 💰 Expense Tracker using Python

A simple and efficient Python application to track daily expenses, categorize them, and analyze spending patterns over time. Helps users gain better control over their personal finances.

## 📌 Features

- ➕ Add new expenses with amount, date, and category
- 📋 View all recorded expenses
- 🗑️ Delete individual or all records
- 📊 Generate expense summaries by category or month
- 💾 Data stored using SQLite or CSV
- 🖥️ Optional GUI using Tkinter
- 📈 Visual insights using Matplotlib (optional)

## 🛠️ Technologies Used

- Python 3
- `sqlite3` or `csv` for data storage
- `tkinter` for GUI (optional)
- `matplotlib` for visualizations (optional)
- `datetime` and `os` for system-level operations

## 📁 Project Structure

expense-tracker/
│
├── tracker.py # Main CLI or logic file
├── gui.py # GUI version using Tkinter (optional)
├── db_handler.py # Database handling logic
├── summary.py # Reporting and analytics
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/expense-tracker-python.git
cd expense-tracker-python

2. Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application

python tracker.py             # CLI version
python gui.py                 # GUI version (optional)

📊 Example Use Case

    Add an expense:

Amount: 150
Category: Food
Date: 2025-06-01

View a monthly summary:

    Total this month: ₹5000
    Food: ₹2000 | Travel: ₹1500 | Utilities: ₹1500

📄 License

This project is open-source and available under the MIT License.
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.
🔗 Connect with Me

Aman Chaurasia
📧 amanchaurasia687@gmail.com
🌐 theamanchaurasia07
