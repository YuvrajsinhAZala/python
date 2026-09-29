#Write a program to illustrate instance variables and class variables.

class yuvraj():
    collage_name='MU'

    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    def sinh(self):
        print(self.roll)
        print(self.name)
        print(yuvraj.collage_name)
y1 = yuvraj(1,'yuvraj')
y1.sinh()
y2 = yuvraj(2,'sinh')
y2.sinh()
