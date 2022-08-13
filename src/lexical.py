from dataclasses import dataclass
from typing import Optional, List


class Char(str):
    def __new__(cls, s: str) -> None:
        if len(s) != 1:
            raise ValueError("String length should be 1!")
        return super(Char, cls).__new__(cls, s)


class IndentationLevel:
    pass


class Spanned:
    pass


@dataclass
class Location:
    """A location somewhere in the sourcecode."""
    row: int
    column: int

    def __str__(self) -> str:
        return f"line {self.row} column {self.column}"

    def reset(self):
        self.row = 1
        self.column = 1

    def go_right(self):
        self.column += 1

    def go_left(self):
        self.column -= 1

    def newline(self):
        self.row += 1
        self.column = 1


@dataclass
class Lexer:
    chars: str
    at_begin_of_line: bool
    nesting: int  # Amount of parenthesis
    indentation_stack: List[IndentationLevel]
    pending: List[Spanned]
    chr0: Optional[Char]
    chr1: Optional[Char]
    chr2: Optional[Char]
    location: Location
