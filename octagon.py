from math import sqrt, pi, cos, sin
import matplotlib.pyplot as plt 


#Создаем класс
class Octagon:
    
    
    def __init__(self, storona:int):
        self.storona = storona
        self.grad = 45
        self.k = 1 + sqrt(2)
        

    #Радиус описанной окружности
    def  rad_opisanoy(self) -> float:
        rad = sqrt((1 + sqrt(2))/((1 + sqrt(2)) - 1)) * self.storona
        return rad
    

    #Радиус вписанной окружности
    def rad_vpisanoy(self) -> float:
        rad = (self.storona / 2)* (1 + sqrt(2))
        return rad
        

    #Площодь восьмиугольника
    def s(self):
        s = 2 * (self.storona ** 2) * (sqrt(2) + 1)
        print(f'Площадь восьмиугольника: {s}\n')

    def s_opisanoy(self):
        s1 = (self.rad_opisanoy() ** 2) * 3,14
        print(f'Площадь описаной около восьмиугольника окружности {s1}')

    def s_vpisanoy(self):
        s2 = (self.rad_vpisanoy() ** 2) * 3,14
        print(f'Площадь вписаной в восьмиугольник окружности {s2}')

    #Периметр восьмиугольника
    def perimetr(self):
        print(f'Периметр восьмиугольника: {self.storona * 8}\n')
    

    #Нахождение вершин
    def peaks(self) -> list:
        peaks_x = []
        #Список вершин
        peaks_y =[]


        #Создание списка вершин
        for i in range(8):
            x = self.rad_opisanoy() * cos((pi/8) + i * (pi/4))
            y = self.rad_opisanoy() * sin((pi/8) + i * (pi/4))
            peaks_x.append(x)
            peaks_y.append(y)


        peaks_x.append(peaks_x[0])
        peaks_y.append(peaks_y[0])
        return peaks_x, peaks_y
    

    #Рисование фигур
    def paint(self):
        #Описанная около восьмиугольника окружность
        circle1 = plt.Circle((0, 0 ), self.rad_opisanoy(), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle1)


        #Вписанная в восьмиугольник окружность
        circle2 = plt.Circle((0,0 ), self.rad_vpisanoy(), color='r', fill=False)
        ax=plt.gca()
        ax.add_patch(circle2)


        #Восьмиугольник построенный по вершинам
        x,y = self.peaks()
        plt.plot(x, y)


        #Отображение
        plt.axis('scaled')
        plt.show()


    def __del__(self):
        print('Otagon has been deleted')
    

def left():

    zn = input('Введите сторону восьмиугольника\n')
    oct = Octagon(int(zn))
    print(oct.rad_opisanoy())
    print(oct.rad_vpisanoy())
    oct.s()
    oct.paint()
    print('============')
    x,y = oct.peaks()
    print(x)
    print(y)


def main():
    left()

if __name__ == '__main__':
    main()