# Napisz skrypt obliczający wartość iloczynu dwóch wektorów:
# a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów

def il_skalarny (a,b):
    il_skalar = 0
    for i in range(len(a)):
        il_skalar += a[i]*b[i]
    return il_skalar
if __name__ == "__main__":
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    print(il_skalarny(a,b))