#private and public class 
class instagram():
    def __init__(self,acc_passwrd,id):
        self._acc_passwrd=acc_passwrd
        self.id=id
    def resetpass(self):
       print(f" {self._acc_passwrd}")
user1 = instagram("abc123", "meeku")
print(user1.id) 
print(user1._acc_passwrd) #private__





    