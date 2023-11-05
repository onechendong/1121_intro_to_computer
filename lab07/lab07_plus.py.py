#因為助教課提到要自己改一點數字，因此以下註記各method更改後的狀態。

#FEED:
# animal    weight  mood
# Dog       +0.4    +2
# Shiba     +0.5    +5

#WALK:
# animal    weight  mood
# Dog       -0.3    +3

#BATH:
# animal    weight  mood
# Dog       -       -3


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
        super().__init__(weight, mood)#繼承class Animal的初始化

    def feed(self, n_feed):
        self.weight += (n_feed*0.4)
        self.mood += (n_feed*2)

    def walk(self, n_walk):
        self.weight -= (n_walk*0.3)
        self.mood += (n_walk*3)

    def bath(self, n_bath):
        self.mood -= (n_bath*3)

    def printf(self, n_feed, n_walk, n_bath):
        pass #這裡用不到，就不寫了!


class Shiba(Dogs):
    def __init__(self, weight, mood):
        super().__init__(weight, mood)#繼承class Dogs的初始化
        
    def feed(self, n_feed):
        self.weight += (n_feed*0.5)
        self.mood += (n_feed*5)
        
    def printf(self, n_feed, n_walk, n_bath):
        self.feed(n_feed) #因為class Shiba有自己的feed method，所以這裡引用的是class Shiba的feed method
        self.walk(n_walk) #因為class Shiba繼承class Dogs，所以這裡引用的是class Dogs的walk method
        self.bath(n_bath) #因為class Shiba繼承class Dogs，所以這裡引用的是class Dogs的bath method
        print("柴犬現在的體重= " + str(round(self.weight, 1)) + " kg, 心情 " + str(self.mood))
        
    def mood_constraint(self, constraint):
        self.constr = constraint
        print("mood最高只能為=" ,self.constr )
        if (self.mood>self.constr):
            print("所以，柴犬現在的心情", self.constr)

shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3) 
shiba.mood_constraint(100) #第2小題mood最大值改為100
print("\n")
shiba = Shiba(5, 70) 
shiba.printf(20, 10, 3)
shiba.mood_constraint(200) #第3小題mood最大值改為200