#Write a program to illustrate method resolution order and magic methods.

class a:
    def show(self):
        print("class A")
class b(a):
    def show(self):
        print("class B")
class c(a):
    def show(self):
        print("class C")
class d(b,c):
    pass

obj = d()
obj.show()

print(d.mro())
