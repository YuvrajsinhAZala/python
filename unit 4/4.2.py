#Write a program to demonstrate constructor and destructor usage.

class yuvraj():
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
    def display(self):
        print(self.roll)
        print(self.name)
    def __del__(self):
        print('deleted')
y = yuvraj(1,'yuvraj')
y.display()

del y

