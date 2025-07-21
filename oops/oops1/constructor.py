


class preson:
    def __init__(self,id,fname,lname,age,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.age,self.loc)
person1=preson(101,'anu','k',26,'pta')
person1.printvalue()