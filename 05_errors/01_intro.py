# Name Error, not defined
#print(my_variable)
# Gives Trace (Stacktrace), where it occured
# Bottom: Error Description
# Line of Code raised the error
# Fuction / Stack Trace --> Caller, Caller, Caller...

#Example
#add_movie
#->show_movie
#->->show_movie_details Error

#Built in Errors
# IndexError
## Out of Range

# KeyError
## Dictionary has not key

# NameError
## Variable not defined

# AttributeError
## Wrong Attribute Object Access (intersect Lists) 

# NotImplementedError
## Self Raised "Not Implemented yet"

# RUntimeError
## Not often, essentially a base Error, others Inherit from that

# SyntaxError
## Messed up code / Illegal Syntax

# IndentationError
## Code not indended

# TabError
## 4x Space other Line 1x Tab, python doesnt like mixing indetation types

# TypeError
## Unsupported operand Types (add String and Number)

# ValueError
## Built in Functions Value of Correct Type but illegal Value
## int(20.5)
## Usually only BuiltIn Functions

# ImportError
## Circular Import A--<B--<C--<A(!)

# DeprecationWarning
## Threated as Error, but only warning
## No longer the best way to do
## Also raised by you