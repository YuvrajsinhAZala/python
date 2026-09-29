#Write a program to illustrate instance variables and class variables.

class yuvraj():
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def display(self):
        print(self.roll)
        print(self.name)
   
y = yuvraj(1,'yuvraj')
print('----------instance variable----------')
y.display()


print('----------class variable----------')
class sinh():
    @classmethod
    def dis(cls,roll,name):
        cls.roll=roll
        cls.name=name
        print(cls.roll)
        print(cls.name)
sinh.dis(2,'sinh')




