#3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using ‘object.a = 0ʼ.̓ Does this change the class attribute?
class sample():
    a="mahak"#class attribute

obj=sample()
obj.a="meeku"
print(sample.a)
print(obj.a)
        

