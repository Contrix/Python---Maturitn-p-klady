"""
Vytvořte aplikaci, která čte uživatelem zadaný soubor a zapisuje do dalšího uživatelem zadaného souboru. Aplikace provádí následující akce:
    Převede soubor na malá písmena.
    Nahradí výskyt zadaného znaku jiným zadaný znakem.
    Statistika výskytu jednotlivých znaků v souboru.
    Generování náhodného textu. (Uživatel zadává počet slov. Slova mají náhodnou délku a střídají se v nich souhlásky a samohlásky.)
Aplikace se bude ovládat interaktivně pomocí jednoduchého menu.
http://hroch.spseol.cz/~nozka/python/priklad_soubory/
"""
import random


class App:
    def __init__(self):
        self.in_file_path = None
        self.out_file_path = None

    def transform(self):
        try:
            in_file = open(self.in_file_path, "r")
            out_file = open(self.out_file_path, "w")
            while True:
                line = in_file.readline()
                if line != "":
                    line = line.lower()
                    out_file.write(line)
                else:
                    break
        except IOError:
            print("Nepodařilo se otevřít soubory!")
        finally:
            in_file.close()
            out_file.close()

    def replace(self):
        print("Zadej znak, který chceš nahradit")
        old_letter = input()
        print("Zadej znak, kterým chceš nahradit")
        new_letter = input()
        try:
            in_file = open(self.in_file_path, "r")
            out_file = open(self.out_file_path, "w")
            while True:
                line = in_file.readline()
                if line != "":
                    line = line.replace(old_letter, new_letter)
                    out_file.write(line)
                else:
                    break
        except IOError:
            print("Nepodařilo se otevřít soubory!")
        finally:
            in_file.close()
            out_file.close()

    def statistic(self):
        stat = {}
        try:
            in_file = open(self.in_file_path, "r")
            out_file = open(self.out_file_path, "w")
            while True:
                line = in_file.readline()
                if line != "":
                    line = line.lower()
                    for i in line:
                        if i.isalpha():
                            if i not in stat:
                                stat.update({i: 1})
                            else:
                                stat[i] += 1
                else:
                    break

            for i in stat.keys():
                out_file.write("Znak - počet\n")
                out_file.write(i + " - " + str(stat.get(i)) + "\n")

        except IOError:
            print("Nepodařilo se otevřít soubory!")
        finally:
            in_file.close()
            out_file.close()

    def generate(self):
        consonant = "bcdfghjklmnpqrstvwxz"#čďřšťž
        vowel = "aeiouy" #áéěíóúůý
        try:
            print("Zadejte počet slov: ", end="")
            length = int(input())
        except:
            print("Zadaný špatný tvar přirozeného čísla čísla")

        try:
            out_file = open(self.out_file_path, "w")
            for _ in range(1, length):
                word = ""
                for i in range(1, random.randint(3, 10)):
                    if i % 2 != 0:
                        word += random.choice(consonant)
                    else:
                        word += random.choice(vowel)
                out_file.write(word + " ")
        except IOError:
            print("Nepodařilo se otevřít soubory!")
        finally:
            out_file.close()

    def in_file(self):
        while True:
            print("Zadej vstuní soubor: ", end="")
            self.in_file_path = input()
            try:
                in_file = open(self.in_file_path, "r")
            except IOError:
                print("Zadaný soubor neexistuje!")
            else:
                in_file.close()
                break

    def out_file(self):
        while True:
            print("Zadej výstupní soubor: ", end="")
            self.out_file_path = input()
            try:
                out_file = open(self.out_file_path, "r")
            except IOError:
                print("Zadaný soubor neexistuje!")
            else:
                out_file.close()
                break

    def run(self):
        while True:
            print("1 - Převod na malá písmena\n"
                  "2 - Nahrazení znaků\n"
                  "3 - Statistika souboru\n"
                  "4 - Generování náhodného textu\n"
                  "5 - Konec\n"
                  "Zadejte další příkaz: ", end="")
            election = input()

            if election == "1":
                app.transform()
            elif election == "2":
                app.replace()
            elif election == "3":
                app.statistic()
            elif election == "4":
                app.generate()
            elif election == "5":
                break
            else:
                print("Špatná volba!")
app = App()

app.in_file()
app.out_file()
app.run()
