#Write a program to demonstrate method overriding and polymorphism. 

class animal:
    def sound(self):
        print("animal make sound")
class dog(animal):
    def sound(self):
        print("dog barks")
class cat(dog):
    def sound(self):
        print("cat meows")

a=dog()
a.sound()

a=cat()
a.sound()
