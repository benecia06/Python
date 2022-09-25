#arithmetic operators
from ast import operator
import sqlite3


add= 3+4
sub= 3-2
mul= 3*2
div_quotient= 4/3
div_remainder= 4%3
power= 2**3
# Precedence of Operators
# PEMDASLR(LEFT TO RIGHT)
# PARENTHESES->()
# EXPONENTS-> ** //
# MULTIPLICATION-> * DIVISION-> / 
# ADDITION-> + SUBTACTION-> - (IN CASE OF EQUAL PRECEDENCE THE OPERATOR ON THE LEFT IS GIVEN PRIORITY)
print(3 * (3 + 3) / 3 - 3)

print(round(8/3, 2)) #round() is used to round off a number to specific decimal places by adding the required place after the comma
print(8//3) #// is used to chop off the decimal points in a number
print(8/3)
add+=1 #shorthand notation 
#fstring
score= 10
height= 1.8
isWinning= True
print(f"Your score is {score}, your height is {height} and you are winning is {isWinning}") #f-string is used to avoid unnecessary type conversions





