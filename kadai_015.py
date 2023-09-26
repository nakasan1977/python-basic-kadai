class Human:
  def __init__(self,name,age):
    self.name = name
    self.age= age
  def printinfo(self):
    print(self.name)
    print(self.age)

person1 = Human("近本光司",29)
person2 = Human("大山悠輔",29)
person3 = Human("村上頌樹",25)

person1.printinfo()
person2.printinfo()
person3.printinfo()