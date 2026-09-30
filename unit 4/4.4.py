#Write a program to demonstrate instance methods class methods and static methods.

class Yuvraj:
    def instancem(self):
        print("instance method")
    @classmethod
    def classm(cls):
        print("class method")
    @staticmethod
    def staticm():
        print("static method")
y=Yuvraj()
y.instancem()

Yuvraj.classm()

y.staticm()
