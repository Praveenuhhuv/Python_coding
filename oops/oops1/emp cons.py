


class employe:
    comp_name='luminus'
    def __init__(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

    def printvalue(self):
        print(self.id,self.fname,self.lname,self.age,self.age,employe.comp_name)
person1=employe(101,'anu','k',2)
person1.printvalue()