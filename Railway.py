class Railway:
    formType = "Railway Form"

    def __init__(self,name,seat):
        self.name = name
        self.seat = seat
        
    def getDetails(self):
        print(f"Train name is : {self.name}")
        print(f"Seats available are : {self.seat}")

    def bookInfo(self):
        if(self.seat > 0):
            print(f"Ticket Booked. Your Seat No. is : {self.seat}")
            self.seat = self.seat-1
        else:
            print("Sorry the train is full!")    

a = Railway("Rajdhani Express", 100)
a.getDetails()
a.bookInfo()
a.getDetails()
