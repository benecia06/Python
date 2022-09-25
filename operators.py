#arithmetic operators
from ast import operator
import sqlite3


add= 3+4
sub= 3-2
mul= 3*2
div_quotient= 4/3
div_remainder= 4%3
power= 2**3
square_root= 4//2
# Precedence of Operators
# PEMDASLR(LEFT TO RIGHT)
# PARENTHESES->()
# EXPONENTS-> ** //
# MULTIPLICATION-> * DIVISION-> / 
# ADDITION-> + SUBTACTION-> - (IN CASE OF EQUAL PRECEDENCE THE OPERATOR ON THE LEFT IS GIVEN PRIORITY)
print(3 * (3 + 3) / 3 - 3)



