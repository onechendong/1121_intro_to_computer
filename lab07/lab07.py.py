#因為助教課提到要自己改一點數字，因此以下註記各method更改後的狀態。

#FEED:
# animal    weight  mood
# Dog       +0.4    +2
# Cat       +0.3    +1

#WALK:
# animal    weight  mood
# Dog       -0.3    +3
# Cat       -0.2    -2

#BATH:
# animal    weight  mood
# Dog       -       -3
# Cat       -       -4


class Animal():
    def __init__(self, weight, mood):
        self.weight = weight
        self.mood = mood

    def feed(self):
        pass

    def walk(self):
        pass

    def bath(self):
        pass


class Dogs(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)#繼承父類別的初始化

    def feed(self):
        self.weight += 0.4
        self.mood += 2

    def walk(self):
        self.weight -= 0.3
        self.mood += 3

    def bath(self):
        self.mood -= 3

    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):#迴圈跑n_feed次，表示餵食n_feed次
            self.feed()
        for i in range(n_walk):#迴圈跑n_walk次，表示散步n_walk次
            self.walk()
        for i in range(n_bath):#迴圈跑n_bath次，表示洗澡n_bath次
            self.bath()
        print("狗狗現在的體重= " + str(round(self.weight, 1)) + " kg, 心情 " + str(self.mood))
        

class Cats(Animal):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)#繼承父類別的初始化

    def feed(self):
        self.weight += 0.3
        self.mood += 1

    def walk(self):
        self.weight -= 0.2
        self.mood -= 2

    def bath(self):
        self.mood -= 4

    def printf(self, n_feed, n_walk, n_bath):
        for i in range(n_feed):#迴圈跑n_feed次，表示餵食n_feed次
            self.feed()
        for i in range(n_walk):#迴圈跑n_walk次，表示散步n_walk次
            self.walk()
        for i in range(n_bath):#迴圈跑n_bath次，表示洗澡n_bath次
            self.bath()
        print("貓貓現在的體重= " + str(round(self.weight, 1)) + " kg, 心情 " + str(self.mood))

dog = Dogs(4.8, 65)
dog.printf(18, 10, 4) 

cat = Cats(8.2, 60) 
cat.printf(40, 7, 1) 