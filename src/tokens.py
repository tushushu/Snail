from enum import Enum
from http.client import CONTINUE


class Tok(Enum):
    # Types
    INT = "int"
    FLOAT = "float"
    STRING = "str"
    BOOL = "bool"

    # Arithmetic operators
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"

    # Comparison operators
    EQ = "="
    NE = "!="
    GT = ">"
    GE = ">="
    LT = "<"
    LE = "<="

    # Punctuations
    DOT = "."
    COMMA = ","
    SEMI = ";"
    LPAR = "("
    RPAR = ")"
    LSQB = "["
    RSQB = "]"
    LB = "{"
    RB = "}"
    EOF = "EOF"

    # Keywords(alphabetically):
    AND = "and"
    BREAK = "break"
    CONTINUE = "continue"
    ELSE = "else"
    FALSE = "false"
    FN = "fn"
    FOR = "for"
    IF = "if"
    NOT = "not"
    OR = "or"
    RETURN = "return"
    TRUE = "true"
    WHILE = "while"
