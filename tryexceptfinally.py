# sample try/except/finally processing
def f():
    try:
       tmp = input("Enter a number and I'll square it: ")
       print(float(tmp)**2)
    except:
       print("dude. I asked you for a number and %s is not a number." % tmp)
    finally:
       print("thanks for playing!")

f()

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as detail:
    print 'this is the run-time error handled in the except block:', detail

# Python exceptions
# https://docs.python.org/2/library/exceptions.html
'''
Enter a number and I'll square it: "fgh"
dude. I asked you for a number and fgh is not a number.
thanks for playing!
this is the run-time error handled in the except block: integer division or modulo by zero
'''