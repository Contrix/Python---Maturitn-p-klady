"""
Implementujte deskovou hru Logik. Hracím kamenům budou odpovídat barvy.
Máme k dispozici
    8 druhů hracích kamemů
    2 druhy vyhodnocovacích kamenů -- tato informace lze sdělit i textově takže je nemusíte používat
Na začátku hry je náhodně rozmístěno 5 různých hracích kamenů. Druh hracího kamenu se nesmí opakovat. Hráč hádá rozmístění kamenů.
Program při každém pokusu hráči sdělí:
    kolik kamenů je použito správně, co do druhu i pozice (černé vyhodnocovací kameny)
    kolik kamenů je správného druhu, ale na nesprávné pozici (bílé vyhodnocovací kameny) Toto sdělení může být číslovkou nebo pomocí vyhodnocovacího kamene
Hráč má 10 pokusů na to, aby uhodl skrytou kombinaci. Po uhodnutí nebo po vyčerpání všech pokusů program ukáže zadanou kombinaci.
http://hroch.spseol.cz/~nozka/python/priklad_logik/
"""
import random


class App:
    def new_example(self):
        my_colors = "crgbwyop"
        self.colors = []
        while len(self.colors) < 5:
            new = my_colors[random.randint(0, 7)]
            if new not in self.colors:
                self.colors += new
        print(self.colors)

    def test(self, vstup):
        color = 0
        position = 0
        for i in range(0, 5):
            if self.colors[i] == vstup[i]:
                position += 1
            elif self.colors[i] in vstup:
                color += 1
        print(position, end="")
        print(" - ", end="")
        print(color)

    def show(self):
        for i in self.colors:
            print(i, end="")

app = App()
app.new_example()

for _ in range(0, 10):
    while True:
        print("Zadej 5 barevných kamenů (cyan, red, green, blue, white, yellow, orange, purple: ", end="")
        test = input()
        if len(test) == 5:
            break
        else:
            print("Nesprávný počet kamenů!")
    app.test(test)
app.show()
