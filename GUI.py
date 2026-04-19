import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from lexer import tokenize, symbol_table, error_handler

# Main window
root = tk.Tk()
root.title("Advanced Lexical Analyzer")
root.geometry("1100x700")
root.configure(bg="#1e1e1e")

# Fonts
FONT_TITLE  = ("Courier New", 16, "bold")
FONT_NORMAL = ("Courier New", 11)
FONT_SMALL  = ("Courier New", 10)

# Title label
title_label = tk.Label(root, text="Advanced Lexical Analyzer", font=FONT_TITLE, bg="#1e1e1e", fg="#00ff99")
title_label.pack(pady=10)

# Top frame for input
top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(fill="x", padx=20)

input_label = tk.Label(top_frame, text="Source Code Input:", font=FONT_NORMAL, bg="#1e1e1e", fg="white")
input_label.pack(anchor="w")

input_text = tk.Text(top_frame, height=10, font=FONT_SMALL, bg="#2d2d2d", fg="#ffffff", insertbackground="white")
input_text.pack(fill="x", pady=5)

# Buttons frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=5)

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as f:
            content = f.read()
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, content)

def export_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            f.write("--- TOKEN STREAM ---\n")
            f.write(f"{'No.':<6} {'Type':<20} {'Value':<20} {'Line':<8} {'Column':<8}\n")
            f.write("-" * 65 + "\n")
            for row in token_tree.get_children():
                values = token_tree.item(row)["values"]
                f.write(f"{values[0]:<6} {values[1]:<20} {values[2]:<20} {values[3]:<8} {values[4]:<8}\n")

            f.write("\n--- SYMBOL TABLE ---\n")
            f.write(f"{'Name':<20} {'First Line':<15} {'References':<10}\n")
            f.write("-" * 45 + "\n")
            for row in symbol_tree.get_children():
                values = symbol_tree.item(row)["values"]
                f.write(f"{values[0]:<20} {values[1]:<15} {values[2]:<10}\n")

            f.write("\n--- ERROR LOG ---\n")
            f.write(error_text.get("1.0", tk.END))

        messagebox.showinfo("Export Successful", "Results exported successfully.")

def run_lexer():
    source = input_text.get("1.0", tk.END).strip()
    if not source:
        messagebox.showwarning("Empty Input", "Please enter or load source code first.")
        return

    # Clear previous results
    for row in token_tree.get_children():
        token_tree.delete(row)
    for row in symbol_tree.get_children():
        symbol_tree.delete(row)
    error_text.config(state="normal")
    error_text.delete("1.0", tk.END)

    # Run lexer
    tokens_list = tokenize(source)

    # Fill token stream table
    for token in tokens_list:
        token_tree.insert("", tk.END, values=(
            token["number"],
            token["type"],
            token["value"],
            token["line"],
            token["column"]
        ))

    # Fill symbol table
    for name, info in symbol_table.get_table().items():
        symbol_tree.insert("", tk.END, values=(
            name,
            info["line"],
            info["references"]
        ))

    # Fill error log
    errors = error_handler.get_errors()
    if not errors:
        error_text.insert(tk.END, "No errors found.", "green")
    else:
        for error in errors:
            error_text.insert(tk.END,
                f"Line {error['line']}, Column {error['column']}: {error['message']}\n",
                "red"
            )
    error_text.config(state="disabled")

# Buttons
run_btn    = tk.Button(btn_frame, text="Run Lexer",     font=FONT_NORMAL, bg="#00ff99", fg="#1e1e1e", width=15, command=run_lexer)
load_btn   = tk.Button(btn_frame, text="Load File",     font=FONT_NORMAL, bg="#0099ff", fg="#ffffff", width=15, command=load_file)
export_btn = tk.Button(btn_frame, text="Export Results",font=FONT_NORMAL, bg="#ff9900", fg="#ffffff", width=15, command=export_results)
clear_btn  = tk.Button(btn_frame, text="Clear",         font=FONT_NORMAL, bg="#ff4444", fg="#ffffff", width=15,
                       command=lambda: [input_text.delete("1.0", tk.END),
                                        [token_tree.delete(r) for r in token_tree.get_children()],
                                        [symbol_tree.delete(r) for r in symbol_tree.get_children()],
                                        error_text.config(state="normal"),
                                        error_text.delete("1.0", tk.END),
                                        error_text.config(state="disabled")])

run_btn.grid   (row=0, column=0, padx=10)
load_btn.grid  (row=0, column=1, padx=10)
export_btn.grid(row=0, column=2, padx=10)
clear_btn.grid (row=0, column=3, padx=10)

# Bottom frame for output
bottom_frame = tk.Frame(root, bg="#1e1e1e")
bottom_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Token stream table
token_label = tk.Label(bottom_frame, text="Token Stream:", font=FONT_NORMAL, bg="#1e1e1e", fg="white")
token_label.grid(row=0, column=0, sticky="w")

token_tree = ttk.Treeview(bottom_frame, columns=("No.", "Type", "Value", "Line", "Column"), show="headings", height=10)
for col in ("No.", "Type", "Value", "Line", "Column"):
    token_tree.heading(col, text=col)
    token_tree.column (col, width=100)
token_tree.grid(row=1, column=0, sticky="nsew", padx=(0, 10))

# Symbol table
symbol_label = tk.Label(bottom_frame, text="Symbol Table:", font=FONT_NORMAL, bg="#1e1e1e", fg="white")
symbol_label.grid(row=0, column=1, sticky="w")

symbol_tree = ttk.Treeview(bottom_frame, columns=("Name", "First Line", "References"), show="headings", height=10)
for col in ("Name", "First Line", "References"):
    symbol_tree.heading(col, text=col)
    symbol_tree.column (col, width=120)
symbol_tree.grid(row=1, column=1, sticky="nsew", padx=(0, 10))

# Error log
error_label = tk.Label(bottom_frame, text="Error Log:", font=FONT_NORMAL, bg="#1e1e1e", fg="white")
error_label.grid(row=0, column=2, sticky="w")

error_text = tk.Text(bottom_frame, height=10, font=FONT_SMALL, bg="#2d2d2d", fg="white", state="disabled", width=35)
error_text.tag_config("red",   foreground="#ff4444")
error_text.tag_config("green", foreground="#00ff99")
error_text.grid(row=1, column=2, sticky="nsew")

bottom_frame.columnconfigure(0, weight=2)
bottom_frame.columnconfigure(1, weight=1)
bottom_frame.columnconfigure(2, weight=1)
bottom_frame.rowconfigure(1, weight=1)

# Run the app
root.mainloop()