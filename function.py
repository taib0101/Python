# callback function
def function1(x, y, callback):
    callback(x*10, y*20)

def function2(x, y):
    print(x + y)

function1(3, 2, function2)

# closure function
def outer():
    def inner():
        print("Bro this is closure, means it return function")
    return inner

closure = outer()
closure()

# Anonymous Function

def Function1(x, y, callaback):
    callaback(x*2, y*2)

Function1(30, 40, lambda x, y: print(x + y))