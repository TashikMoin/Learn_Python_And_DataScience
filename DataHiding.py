class A :
    def __init__(self):
        self.x=10
        print(id(self.x))""" Its different from the attribute x of class B & Has Different Memory """
        print("Constructor Of A Is Called")
    
    def PrintA(self):
        print(self.x)

class B(A):
    def __init__(self):
        print("Constructor Of B Is Called")
        self.x=20 """ Its different from the attribute x of class A & Has Different Memory """
        print(id(self.x))
        super().__init__() """ If we would've called it earlier , then Obj.x , self.x all the 
        functions that are printing any variable named 'x' then they will print the value of 
        class B's x bcz A's constructor was called earlier & B consructor got executed later 
        so the data of parent will hide and x will always print the value it has in class B 
        but if would have called the super method for parent class at the end of B's constructor
        or after the attribute x Of B in B's Constructor then it would've given the value of the
        parent class attritube x"""

    def PrintB(self):
        print(self.x)

Obj = B() 
print(Obj.x)
Obj.PrintA()
Obj.PrintB()

""" 
       Output 
Consructor Of B Is Called
Address of B Class attribute x = 9079616
Address of B Class attribute x = 9079296
Consructor Of A Called
10
10
10
"""

