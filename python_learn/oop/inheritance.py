class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name -", self.last_name)
        print("Eye Color -", self.eye_color)

class Son(Parent):
    def hello(self):
        print("Hello~")

class Daughter(Parent):
    def __init__(self, last_name, eye_color, toy_number):
        print("Daughter Constructor Called")

        Parent.__init__(self, last_name, eye_color)
        #another way to call parent constructor
        # super(Daughter, self).__init__(last_name, eye_color)

        self.toy_number = toy_number

    #override inherited method
    def show_info(self):
        print("Last Name -", self.last_name)
        print("Eye Color -", self.eye_color)
        print("Number of Toys -", str(self.toy_number))

billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()
print()

bell_cyrus = Son("Cyrus", "yellow")
print(bell_cyrus.last_name)
bell_cyrus.show_info()
print()

miley_cyrus = Daughter("Cyrus", "yellow", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.toy_number)
miley_cyrus.show_info()