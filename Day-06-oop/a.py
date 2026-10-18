#3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using ‘object.a = 0ʼ.̓ Does this change the class attribute?
class sample():
    a="mahak"#class attribute

obj=sample()
obj.a="meeku"
print(sample.a)
print(obj.a)
#4. Add a static method in problem 2, to greet the user with hello.
class student():
    @staticmethod
    def user():#self is not needed in static method
        print("hello ravi")
student.user()       

