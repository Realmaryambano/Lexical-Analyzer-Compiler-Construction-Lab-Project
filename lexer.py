import ply.lex as lex
from symbol_table import SymbolTable
from error_handler import ErrorHandler

# Initialize symbol table and error handler
symbol_table = SymbolTable()
error_handler = ErrorHandler()

# All token types
tokens = [
    'IDENTIFIER',
    'INTEGER',
    'FLOAT',
    'STRING',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'ASSIGN',
    'EQUALS',
    'NOTEQUALS',
    'GREATERTHAN',
    'LESSTHAN',
    'GREATEREQUAL',
    'LESSEQUAL',
    'AND',
    'OR',
    'NOT',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'SEMICOLON',
    'COMMA',
    'COLON',
]

# Keywords
keywords = {
    'if'     : 'IF',
    'else'   : 'ELSE',
    'while'  : 'WHILE',
    'for'    : 'FOR',
    'return' : 'RETURN',
    'int'    : 'INT',
    'float'  : 'FLOAT_TYPE',
    'string' : 'STRING_TYPE',
    'bool'   : 'BOOL',
    'true'   : 'TRUE',
    'false'  : 'FALSE',
    'and'    : 'AND',
    'or'     : 'OR',
    'not'    : 'NOT',
    'print'  : 'PRINT',
}

tokens += list(set(keywords.values()))

# Simple token rules
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'/'
t_ASSIGN       = r'='
t_EQUALS       = r'=='
t_NOTEQUALS    = r'!='
t_GREATERTHAN  = r'>'
t_LESSTHAN     = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL    = r'<='
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_LBRACE       = r'\{'
t_RBRACE       = r'\}'
t_LBRACKET     = r'\['
t_RBRACKET     = r'\]'
t_SEMICOLON    = r';'
t_COMMA        = r','
t_COLON        = r':'

# Ignore whitespace and tabs
t_ignore = ' \t'

# Float number rule
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

# Integer number rule
def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# String literal rule
def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]
    return t

# Identifier and keyword rule
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in keywords:
        t.type = keywords[t.value]
    else:
        symbol_table.add(t.value, t.lexer.lineno)
    return t

# New line rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Single line comment rule
def t_COMMENT(t):
    r'\#.*'
    pass

# Error handling rule
def t_error(t):
    col = find_column(t.lexer.lexdata, t)
    error_handler.add_error(
        f"Invalid character '{t.value[0]}'",
        t.lexer.lineno,
        col
    )
    t.lexer.skip(1)

# Find column number
def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Build the lexer
lexer = lex.lex()

# Main tokenize function
def tokenize(source_code):
    symbol_table.table.clear()
    error_handler.errors.clear()
    lexer.lineno = 1
    lexer.input(source_code)

    tokens_list = []
    token_number = 1

    for tok in lexer:
        col = find_column(source_code, tok)
        tokens_list.append({
            "number"  : token_number,
            "type"    : tok.type,
            "value"   : str(tok.value),
            "line"    : tok.lineno,
            "column"  : col
        })
        token_number += 1

    return tokens_list