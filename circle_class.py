import matplotlib.pyplot as plt


class Circle1:


    def __init__ (self, x, y, r):
        self.x = x
        self.y = y 
        self.r = r


    def paint(self):
        figure, axes = plt.subplots()
        Drawing_uncolored_circle = plt.Circle( (self.x, self.y ),
                                            self.r ,
                                            fill = False )
        
        axes.set_aspect( 1 )
        axes.add_artist( Drawing_uncolored_circle )
        plt.title( 'Circle' )
        plt.show()


print("Введите параметры для круга")
x = float(input("Введите координату x = "))
y = float(input("Введите координату y = "))
r = float(input("Введите радиус r = "))



X = Circle1(x, y, r)
X.paint()
