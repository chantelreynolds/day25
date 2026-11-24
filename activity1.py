class myClass:
    __privateVar = 27;
    def __privMeth(self):
        print("I'm inside class myClass")

foo = myClass()
foo.hello()
foo.__privMeth