class person:
    def pers(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age

class employe(person):

    def emp(self,prof,department,salary):
        self.prof=prof
        self.department=department
        self.salary=salary
    def printvlue(self):
        print(self.id, self.fname, self.lname,self.salary,self.department,self.prof,)
obj1=employe()
obj1.pers(34,'praveen','p',22)
obj1.emp('data analyst','cse',1000000000)
obj1.printvlue()
