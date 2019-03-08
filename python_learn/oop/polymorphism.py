class Animal:
    def kind(self):
        print("I am animal")

class Dog(Animal):
    def kind(self):
        print("I am dog")

class Cat(Animal):
    def kind(self):
        print("I am cat")

def show_kind(animal):
    animal.kind()

dog = Dog()
cat = Cat()

show_kind(dog)
show_kind(cat)

#but if a class has a same function, this class still can be called successfully
class Job:
    def kind(self):
        print("This is a job")
job = Job()
show_kind(job)