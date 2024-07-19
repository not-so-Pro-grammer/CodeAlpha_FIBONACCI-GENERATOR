import tkinter as tk
from tkinter import ttk

# Function to generate Fibonacci sequence iteratively
def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Function to handle the button click event
def generate_fibonacci():
    try:
        n = int(entry.get())
        if n < 0:
            raise ValueError("The number must be non-negative")
        fib_sequence = fibonacci_iterative(n)
        result.set(f"Fibonacci sequence: {', '.join(map(str, fib_sequence))}")
    except ValueError as e:
        result.set(f"Error: {e}")

# Create the main window
root = tk.Tk()
root.title("Fibonacci Generator")

# Create and place widgets
ttk.Label(root, text="Enter the number of Fibonacci numbers:").grid(row=0, column=0, padx=10, pady=10)
entry = ttk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)
ttk.Button(root, text="Generate", command=generate_fibonacci).grid(row=0, column=2, padx=10, pady=10)

result = tk.StringVar()
ttk.Label(root, textvariable=result).grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
