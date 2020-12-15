# Napisz skrypt obliczający pierwiastki równania kwadratowego
# w postaci : y = ax 2 + bx + c. Wejściem skryptu są wartości: a, b, c
import math 
import sys
def square_roots(a,b,c):
    delta = b*b - 4*a*c
    delta_root = math.sqrt(abs(delta))
    if (delta>0):
        print("The function has two real roots:")
        print((-b + delta_root)/(2 * a))  
        print((-b - delta_root)/(2 * a))  
    elif delta==0:
        print("The equation has one root")
        print(-b / (2 * a)) 
    else:
        print("The equation has only complex roots:")
        print(- b / (2 * a), " + i", delta_root)  
        print(- b / (2 * a), " - i", delta_root)  
  
if __name__ == "__main__":
    print (sys.argv)
    if len(sys.argv)!=4:
        print("Wrong number of arguments")
    else:
        
        coeffs = [int(i) for i in sys.argv[1:]]
        square_roots(*coeffs)  
