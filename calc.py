import tkinter as tk

def add_digit(digit):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + digit)

def add_operator(operator):
    current = entry.get()
    if current and current[-1] not in operators:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + operator)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_7 = tk.Button(root, text="7", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("7"))
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8 = tk.Button(root, text="8", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("8"))
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9 = tk.Button(root, text="9", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("9"))
button_9.grid(row=1, column=2, padx=5, pady=5)
button_divide = tk.Button(root, text="/", width=5, height=2, font=("Arial", 14), command=lambda: add_operator("/"))
button_divide.grid(row=1, column=3, padx=5, pady=5)

button_4 = tk.Button(root, text="4", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("4"))
button_4.grid(row=2, column=0, padx=5, pady=5)
button_5 = tk.Button(root, text="5", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("5"))
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6 = tk.Button(root, text="6", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("6"))
button_6.grid(row=2, column=2, padx=5, pady=5)
button_multiply = tk.Button(root, text="*", width=5, height=2, font=("Arial", 14), command=lambda: add_operator("*"))
button_multiply.grid(row=2, column=3, padx=5, pady=5)

button_1 = tk.Button(root, text="1", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("1"))
button_1.grid(row=3, column=0, padx=5, pady=5)
button_2 = tk.Button(root, text="2", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("2"))
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3 = tk.Button(root, text="3", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("3"))
button_3.grid(row=3, column=2, padx=5, pady=5)
button_subtract = tk.Button(root, text="-", width=5, height=2, font=("Arial", 14), command=lambda: add_operator("-"))
button_subtract.grid(row=3, column=3, padx=5, pady=5)

button_0 = tk.Button(root, text="0", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("0"))
button_0.grid(row=4, column=0, padx=5, pady=5)
button_decimal = tk.Button(root, text=".", width=5, height=2, font=("Arial", 14), command=lambda: add_digit("."))
button_decimal.grid(row=4, column=1, padx=5, pady=5)
button_equal = tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), command=calculate)
button_equal.grid(row=4, column=2, padx=5, pady=5)
button_add = tk.Button(root, text="+", width=5, height=2, font=("Arial", 14), command=lambda: add_operator("+"))
button_add.grid(row=4, column=3, padx=5, pady=5)

button_clear = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
button_clear.grid(row=5, column=0, padx=5, pady=5, columnspan=2)
button_blank = tk.Button(root, text="", width=5, height=2, font=("Arial", 14))
button_blank.grid(row=5, column=2, padx=5, pady=5)
button_blank = tk.Button(root, text="", width=5, height=2, font=("Arial", 14))
button_blank.grid(row=5, column=3, padx=5, pady=5)

operators = ["+", "-", "*", "/"]

root.mainloop()


