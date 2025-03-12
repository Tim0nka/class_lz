import math
import matplotlib.pyplot as plt
import numpy as np



class Uravnenie:

    def __init__ (self,a,b,c):
        self.a = a
        self.b = b 
        self.c = c 


    def resheba(self):
        discr = self.b ** 2 - 4 * self.a * self.c
        print("Дискриминант D = %.2f" % discr)

        if discr > 0:
            x1 = (-self.b + math.sqrt(discr)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discr)) / (2 * self.a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif discr == 0:
            x = -self.b / (2 * self.a)
            print("x = %.2f" % x)
        else:
            print("Корней нет")  
    
    def paint(self):
        #Создаём экземпляр класса figure и добавляем к Figure область Axes
        fig, ax = plt.subplots()
        #Добавим заголовок графика
        ax.set_title('График функции')
        #Название оси X:
        ax.set_xlabel('x')
        #Название оси Y:
        ax.set_ylabel('y')
        #Начало и конец изменения значения X, разбитое на 100 точек
        x = np.linspace(-5, 5, 100) # X от -5 до 5
        #Построение прямой
        y = x**2
        #Вывод графика
        ax.plot(x, y)
        plt.show()


class Proizvodnay(Uravnenie):


    def


class Integral(Uravnenie):


    def

            
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

x = Uravnenie(a, b, c)
x.resheba()
x.paint()