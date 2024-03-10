#Humanクラス作成
class Human:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    #check_adultメソッド作成
    def check_adult(self):
      if self.age >= 20:
        print(f"{self.name}は大人です。")
      else:
        print(f"{self.name}は未成年です。")

#インスタンスを登記するリストの作成
human1 = Human("勇次郎", 36)
human2 = Human("刃牙", 18)
human3 = Human("ジャック", 20)
humans = [human1, human2, human3]

#リストhumansからデータ抽出、check_adultメソッドをリスト分起動
for human in humans:
  human.check_adult()
