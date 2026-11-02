def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("hy please enter number")
a=increment(2)
print(a)