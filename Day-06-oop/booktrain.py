"""5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
fare information of train running under Indian Railways."""
class train():
    def __init__(self,user,ticket,noofseat,price):
        self.user=user
        self.ticket=ticket
        self.noofseat = noofseat
        self.price=price
    def book(self):
      if self.noofseat>0:
        print("TICKET BOOK SUCCESSFULLY")
        self.noofseat=self.noofseat-1
      else:
        print("no seat available")
  
    def checkstatus(self):
     print("Avilable seats",self.noofseat)

    def fare(self):
     print("ticket price",self.price)
t1 = train("Mahak", "Sleeper", 3, 250)

t1.book()
t1.checkstatus()
t1.fare()