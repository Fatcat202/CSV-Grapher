import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd                                 #pip install pandas
import matplotlib.pyplot as plt                     #pip install matplotlib

# Initialize main window
root = tk.Tk()
root.title("CSV Grapher")
root.geometry("800x640")

# Global variable for DataFrame
df = pd.DataFrame()

# Function to load CSV file
def load_csv():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            display_data(df)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV: {e}")

# Function to display DataFrame in Treeview
def display_data(data):
    tree.delete(*tree.get_children())
    tree["columns"] = list(data.columns)
    tree["show"] = "headings"
    
    for col in data.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for _, row in data.iterrows():
        tree.insert("", "end", values=list(row))

# Function to plot data
def plot_data():
    
    try:
        # Gather name of first column, then use as x-axis
        x_name = df.columns[0]
        df.set_index(x_name, inplace=True)
        # Create and display line graph
        df.plot()
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to plot: {e}")

# Widgets
btn_load = tk.Button(root, text="Load CSV", command=load_csv)
btn_load.pack(pady=10)

btn_plot = tk.Button(root, text="Plot Graph", command=plot_data)
btn_plot.pack(pady=10)

# Treeview to display data
tree = ttk.Treeview(root)
tree.pack(expand=True, fill='both')

# Run loop
root.mainloop()