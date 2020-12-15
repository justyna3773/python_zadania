# Zdefiniuj klasę reprezentującą liczby zespolone (wraz z funkc-
# jami na nich działającymi np. dodawanie, odejmowanie itd.)
# Wykorzystaj powyzszą klasę do stworzenia prostego kalku-
# latora, parsującego i wykonującego równanie podane przez
# użytkownika

class complex_number(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, complex2):
        return complex_number(self.real + complex2.real, self.imaginary + complex2.imaginary)
    def __sub__(self, complex2):
        return complex_number(self.real - complex2.real, self.imaginary - complex2.imaginary)
    def conjugate(self):
        return complex_number(self.real, -self.imaginary)
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"
    

            
def calculate(x,y,z,v,inp2):
    
    result = complex_number(0,0)
    if(inp2=='+'):
        result = complex_number(x,y) + complex_number(z,v)
    elif inp2 == '-':
        result = complex_number(x,y) - complex_number(z,v)
    elif inp2 =='c':
        result = complex_number(x,y).conjugate()
    return result 


if __name__ == "__main__":
    # x = complex_number(3,4)
    # y = complex_number(4,5)
    # print(x.real)
    # print(x + y)
    x, y = [int(x) for x in input("Enter complex number in the form x,y ").split(',')]
    z,v = [int(z) for z in input("Enter complex number in the form x,y ").split(',')]
    inp2 = input('Choose what you want to do with them, "-" for subtraction, "+" for adding, "c" to conjugate')

    print(calculate(x,y,z,v,inp2))
    

  