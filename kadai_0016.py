class Human:
    def __init__(self,name,age):
        self.name = name
        self.age= age
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は{self.age}才、大人です。")
        else:
            print(f"{self.name}は{self.age}才、大人ではありません。")


humans = []
humans.append(Human("ガブリエル・スロニナ",19))
humans.append(Human("リコ・ルイス",19))
humans.append(Human("三浦知良",56))
humans.append(Human("石川雅規",43))

for human in humans:
    human.check_adult()