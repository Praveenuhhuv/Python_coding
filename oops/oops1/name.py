class person:
    def setvalue(self,fname,lname,age,prof,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc

    def printvalue(self):
        print(self.fname,self.lname,self.age,self.prof,self.loc)

person1=person()
person1.setvalue('praveen','k',28,'bigdata','pta')
person1.printvalue()
person2=person()
person2.setvalue('rave','p',208,'data','pta')
person2.printvalue()