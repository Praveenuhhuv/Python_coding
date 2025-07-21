class student:
    coll='aranmula'
    def setvalue(self,id,fname,lname,age,cours):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.cours=cours


    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.cours,student.coll)

person1=student()
person1.setvalue('20','praveen','p',9000,'b.tech')
person1.printvalue()
person2=student()
person2.setvalue('34','prave',' badass',9000,'cs')
person2.printvalue()