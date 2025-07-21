# inheritance
#
# 2 class-parent,child,
# child class get the features of the parent class
class A:#parent base class
    def printa(self,num1):
        self.num1=num1
        print("inside class A",self.num1)


class B(A):#inheritance child derived 
    def printb(self, num2):
        self.num2 = num2
        print("inside class B", self.num2)

obj1=B()
obj1.printb(30)
obj1.printa(34)#collceting A's feature by B