import json
import tkinter as tk
from tkinter import messagebox
from api_client import APIClient

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("API Client")
        
        self.client = APIClient()
        
        self.create_widgets()
    
    def create_widgets(self):
        self.api_key_label = tk.Label(self.root, text="API Key:")
        self.api_key_label.pack()
        self.api_key_entry = tk.Entry(self.root, width=50)
        self.api_key_entry.pack()
        
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()
        
        self.orders_button = tk.Button(self.root, text="Get Orders", command=self.get_orders, state=tk.DISABLED)
        self.orders_button.pack()
        
        self.result_text = tk.Text(self.root, height=20, width=100)
        self.result_text.pack()
    
    def login(self):
        api_key = self.api_key_entry.get()
        if api_key:
            token = self.client.login(api_key)
            if token:
                messagebox.showinfo("Success", "Login successful!")
                self.orders_button.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Error", "Login failed. Please check your API key.")
        else:
            messagebox.showwarning("Warning", "API key is required.")
    
    def get_orders(self):
        orders = self.client.get_orders()
        if orders:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, json.dumps(orders, indent=4, ensure_ascii=False))
        else:
            messagebox.showerror("Error", "Failed to fetch orders.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()