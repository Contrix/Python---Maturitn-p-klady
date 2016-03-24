"""
Navrhněte a vytvořte aplikaci realizující jednoduchý kalkulátor s posfixovou notací. Kalkulátor bude umožňovat tyto matematické operace:
sčítání -- +
odčítání -- -
násobení -- *
dělení -- / nebo :
druhou mocninu !
druhou mocninu #
"""

import math

zasobnik = []


def fce2argumenty(funkce):
    if len(zasobnik) >= 2:
        b = zasobnik.pop()
        a = zasobnik.pop()
        try:
            zasobnik.append(funkce(a, b))
        except Exception as e:
            print("chyba", e.__class__)
            print("chyba", e.message__)
            zasobnik.extend([a, b])
    else:
        print("Operaci nelze provést")


def fce1argumenty(funkce):
    if len(zasobnik) >= 1:
        a = zasobnik.pop()
        try:
            zasobnik.append(funkce(a))
        except Exception as e:
            print("chyba", e.__class__)
            print("chyba", e.message__)
            zasobnik.extend([a])
    else:
        print("nelze provést")


while True:
    try:
        radek = input (str(zasobnik) + " : ")
        for token in radek.split():
            try:
                zasobnik.append(float(token))
            except ValueError:
                if token == '+':
                    fce2argumenty(lambda a, b: a + b)
                elif token == '-':
                    fce2argumenty(lambda a, b: a - b)
                elif token == '*':
                    fce2argumenty(lambda a, b: a * b)
                elif token == '/':
                    fce2argumenty(lambda a, b: a / b)
                elif token == 's':
                    fce1argumenty(lambda a: math.sin(a))
                elif token == 'c':
                    fce1argumenty(lambda a: math.cos(a))
                elif token == 'm':
                    fce2argumenty(lambda a, b: math.pow(a, b))
                elif token == 'o':
                    fce2argumenty(lambda a, b: math.pow(a, 1/b))

    except EOFError:
        exit(0)
    except KeyboardInterrupt:
        exit(1)
