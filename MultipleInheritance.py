class A :

    def __init__(self):
        self.a=10
        print("Consructor Of A Executed")
    
    def fun1(self):
        print(self.a)

class B() :

    def __init__(self):
        self.b=20
        super().__init__()
        print("Consructor Of B Executed")

    def fun2(self):
        print(self.b)

class C(B,A) :
    
    def __init__(self):
        self.c=30
        super().__init__()
        print("Consructor Of C Executed")

    def fun3(self):
        print(self.a , "  " , self.b ,"   ",self.c)


Obj = C()
Obj.fun3()