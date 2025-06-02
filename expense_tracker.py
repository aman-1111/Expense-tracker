import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# Database functions
def add_expense(amount, category, date, note):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO expenses (amount, category, date, note) VALUES (?, ?, ?, ?)',
                   (amount, category, date, note))
    conn.commit()
    conn.close()

def get_expenses():
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, category, date, note FROM expenses ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    conn.commit()
    conn.close()

# GUI App
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("700x500")

        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Amount:").grid(row=0, column=0, padx=5)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Category:").grid(row=0, column=2, padx=5)
        self.category_combo = ttk.Combobox(input_frame, values=[
            "Food", "Transport", "Entertainment", "Bills", "Others"])
        self.category_combo.current(0)
        self.category_combo.grid(row=0, column=3, padx=5)

        tk.Label(input_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.grid(row=1, column=1, padx=5, pady=5)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))

        tk.Label(input_frame, text="Note:").grid(row=1, column=2, padx=5)
        self.note_entry = tk.Entry(input_frame, width=30)
        self.note_entry.grid(row=1, column=3, padx=5)

        add_btn = tk.Button(input_frame, text="Add Expense", command=self.add_expense)
        add_btn.grid(row=2, column=3, pady=10)

        # Expense Listbox
        self.expense_listbox = tk.Listbox(root, width=90, height=20)
        self.expense_listbox.pack(padx=10, pady=10)

        self.expense_listbox.bind('<Delete>', self.delete_selected_expense)

        self.load_expenses()

    def add_expense(self):
        amount = self.amount_entry.get().strip()
        category = self.category_combo.get()
        date = self.date_entry.get().strip()
        note = self.note_entry.get().strip()

        try:
            amount_val = float(amount)
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number.")
            return

        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Invalid Input", "Date must be in YYYY-MM-DD format.")
            return

        add_expense(amount_val, category, date, note)
        self.clear_inputs()
        self.load_expenses()

    def load_expenses(self):
        self.expense_listbox.delete(0, tk.END)
        expenses = get_expenses()
        for e in expenses:
            eid, amount, category, date, note = e
            display_text = f"{eid}. ₹{amount:.2f} | {category} | {date} | {note}"
            self.expense_listbox.insert(tk.END, display_text)

    def clear_inputs(self):
        self.amount_entry.delete(0, tk.END)
        self.category_combo.current(0)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime('%Y-%m-%d'))
        self.note_entry.delete(0, tk.END)

    def delete_selected_expense(self, event):
        selection = self.expense_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        item_text = self.expense_listbox.get(idx)
        expense_id = int(item_text.split('.')[0])

        confirm = messagebox.askyesno("Delete Expense", "Are you sure you want to delete this expense?")
        if confirm:
            delete_expense(expense_id)
            self.load_expenses()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
