a=54#global variable
def fun():
    global a
    print(f"print statment 1 {a}")
    a=44#local variable  
    print(f"print statment 2 {a}")
fun()
print(f"print statment 3 {a}")