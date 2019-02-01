"""
Exceptions are errors
"""

def exceptionHandling():
    try:
        a = 10
        b = 20
        c = "a"

        d = (a + b) / c
        print(d)
    except:
        print("In the except block")
    #     to show stack trace
        raise Exception("this is an exception")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()
