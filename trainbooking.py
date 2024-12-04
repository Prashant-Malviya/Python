from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo
    
    def book(self,fro,to):
        print(f"Ticke is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

train = Train(12342)
train.book("Rampur","delhi")
train.getStatus()
train.getFare("rampur",'delhi')