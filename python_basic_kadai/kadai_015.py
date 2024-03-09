class Human:
    def __init__(self):
       self.name = ""
       self.age = ""
    def set_name(self, name):
       self.name = name
    def set_age(self, age):
       self.age = age
    def printinfo(self):
       print(self.name, self.age)

human = Human()
human.set_name("taro")
human.set_age(77)
human.printinfo()
