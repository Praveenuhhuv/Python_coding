class employee:
    dept='cs'
    comany_name='luminus'
    def setvalue(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,employee.dept,employee.comany_name)

employee1=employee()
employee1.setvalue('20','praveen','p',9000,)
employee1.printvalue()
employee2=employee()
employee2.setvalue('34','prave',' badass',9000)
employee2.printvalue()