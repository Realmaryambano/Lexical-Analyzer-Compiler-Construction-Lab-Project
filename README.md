# Lexical Analyzer — Compiler Construction Lab Project

![Python](https://img.shields.io/badge/Python-3.x-blue) ![PLY](https://img.shields.io/badge/PLY-3.11-green) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange) ![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Description

This project is a complete and advanced Lexical Analyzer built as part of the Compiler Construction Lab course. A Lexical Analyzer is the first phase of a compiler. It reads raw source code as plain text, scans through it character by character, and breaks it down into meaningful units called tokens. Each token is classified by type and tracked with its exact line and column number. The project goes beyond basic tokenization by including a Symbol Table, an Error Recovery System, and a clean Graphical User Interface built with Tkinter.

---

## Features

- Tokenizes source code into a complete classified token stream
- Recognizes keywords, identifiers, integers, floats, strings, booleans, operators, and symbols
- Automatically distinguishes reserved keywords from user defined identifiers
- Tracks exact line number and column number for every token
- Symbol Table that records every identifier with its first occurrence line and reference count
- Error Recovery System that detects invalid characters and unterminated strings without crashing
- Clean dark themed GUI where users can type or load source code and view results instantly
- Export token stream, symbol table, and error log to a text file
- Supports single line comments using #

---

## Project Structure
LexicalAnalyzer/
│
├── lexer.py            # Core lexer engine built using PLY
├── symbol_table.py     # Symbol table to track identifiers
├── error_handler.py    # Error detection and recovery system
└── gui.py              # Graphical user interface built with Tkinter

---

## Technologies Used

- Python 3.x
- PLY (Python Lex-Yacc) Library
- Tkinter (GUI)

---

## Installation and Setup

1. Clone the repository
git clone https://github.com/Realmaryambano/Lexical-Analyzer-Compiler-Construction-Lab-Project.git

2. Navigate to the project folder
cd Lexical-Analyzer-Compiler-Construction-Lab-Project

3. Install the required library
pip install ply

4. Run the application
python gui.py

---

## How to Use

1. Open the application by running gui.py
2. Type source code directly into the input box or click Load File to load a .txt file
3. Click Run Lexer to analyze the source code
4. View the Token Stream, Symbol Table, and Error Log on the screen
5. Click Export Results to save the output to a text file
6. Click Clear to reset everything and start fresh

---

## Sample Input

```python
int x = 10;
int y = 20;
float z = 3.14;
string name = "Maryam";
bool flag = true;

if x > y {
    print x;
}
else {
    print y;
}

while x > 0 {
    x = x - 1;
}

int result = x + y;
return result;

# this is a comment
int error = @;
```
---

## Sample Output

- 66 tokens correctly identified and classified
- Symbol table with 7 identifiers tracked
- Error log reporting invalid character @ at Line 22 Column 13

---

## Course Information

- Course: Compiler Construction Lab
- Project Type: Complex Computing Activity
- Concepts Applied: Regular Expressions, Finite Automata, Token Classification, Symbol Table Design, Error Handling and Recovery

---

## License

This project is personally developed and owned by Maryam Bano. All rights reserved. Do not copy, reuse, or redistribute any part of this project without permission.