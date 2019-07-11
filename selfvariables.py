class myclass :

    def variables(self):
        self.a=10
        self.b=5

    def __init__(self):
        self.variables() #it will allow u to give memory to all the class atributes if u 
        #have multiple constructors


    def fun(self):
        print(self.a,self.b)

x=myclass() 


x.fun()
