import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random
import threading
import time
import six


# Mock function to simulate data for strike price and volume
def get_mock_data():
    # Generates random data for demonstration purposes
    return {
        "strike_price": random.choice([19000, 19500, 20000, 20500]),
        "price": random.uniform(100, 500),
        "volume": random.randint(500, 2000)
    }


# Function to check for spikes
def check_for_spike(data, price_threshold=300, volume_threshold=1500):
    if data["price"] > price_threshold and data["volume"] > volume_threshold:
        return f"Spike Alert! Strike {data['strike_price']} - Price: {data['price']:.2f}, Volume: {data['volume']}"
    return None


# Login validation function
def validate_login(username, password):
    if username == "admin" and password == "password":  # Simple check, replace with secure validation
        return True
    else:
        return False


# Login page
def login_page():
    def attempt_login():
        user = username_entry.get()
        pwd = password_entry.get()
        if validate_login(user, pwd):
            messagebox.showinfo("Login", "Login successful!")
            root.destroy()  # Close login window
            dashboard_page()  # Open dashboard
        else:
            messagebox.showerror("Login", "Invalid credentials")

    root = tk.Tk()
    root.title("Login")
    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)

    username_entry = tk.Entry(root)
    password_entry = tk.Entry(root, show="*")

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    tk.Button(root, text="Login", command=attempt_login).grid(row=2, column=1)

    root.mainloop()


# Dashboard page with mock data and spike detection
def dashboard_page():
    def start_monitoring():
        def monitor_data():
            while monitoring:
                data = get_mock_data()
                signal = check_for_spike(data)
                if signal:
                    signal_text.set(signal)
                else:
                    signal_text.set("Monitoring...")
                update_table(data)
                time.sleep(2)  # Simulate a delay for data fetching

        threading.Thread(target=monitor_data, daemon=True).start()

    def update_table(data):
        df = pd.DataFrame([data])
        for widget in table_frame.winfo_children():
            widget.destroy()
        for i, col in enumerate(df.columns):
            tk.Label(table_frame, text=col, relief="ridge").grid(row=0, column=i)
            tk.Label(table_frame, text=df[col][0], relief="ridge").grid(row=1, column=i)

    dashboard = tk.Tk()
    dashboard.title("Dashboard")

    tk.Label(dashboard, text="Options Price Spike Dashboard", font=("Arial", 16)).pack(pady=10)

    signal_text = tk.StringVar()
    signal_text.set("Monitoring...")
    tk.Label(dashboard, textvariable=signal_text, font=("Arial", 14), fg="red").pack(pady=10)

    tk.Button(dashboard, text="Start Monitoring", command=start_monitoring).pack()

    global monitoring
    monitoring = True
    dashboard.protocol("WM_DELETE_WINDOW", lambda: stop_monitoring(dashboard))

    table_frame = tk.Frame(dashboard)
    table_frame.pack(pady=10)

    dashboard.mainloop()


def stop_monitoring(dashboard):
    global monitoring
    monitoring = False
    dashboard.destroy()


login_page()
