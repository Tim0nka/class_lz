from octagon import Octagon


def func():
    usr_inp = input('Введите сторону восьмиугольника:\n')
    oct = Octagon(int(usr_inp))
    print(f'Радиус описсанной около восьмиугольника окружности:{oct.rad_opisanoy()}')
    print(f'Радиус вписсаной в восьмиугольник окружности: {oct.rad_vpisanoy()}')
    oct.s()
    oct.s_opisanoy()
    oct.s_vpisanoy
    oct.paint()
    oct.perimetr()


def main():
    func()

if __name__ == '__main__':
    main()