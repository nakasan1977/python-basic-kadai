class Human():
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def check_adult(self):
    if self.age > 20:
      print(f"{self.name}は{self.age}なので大人です。")
    else:
      print(f"{self.name}は{self.age}なので未成年です。")
      
person1 = Human("芦田愛菜",19)
person2 = Human("ミイヒ",18)
person3 = Human("梅野隆太郎",32)
person4 = Human("山本由伸",25)
person5 = Human("大山悠輔",29)     
person6 = Human("岡田彰布",65)
    
persons =[person1,person2,person3,person4,person5,person6]

for person in persons:
  person.check_adult()