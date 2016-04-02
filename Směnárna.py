"""
Navrhněte a vytvořte aplikaci pro obsluhu směnárny -- pro nákup i prodej podle aktuálního kurzovního lístku.
Kurzovní lístek bude aplikace načítat ze souboru. Aplikace bude při čtení kurzovního lístku i uživatelského vstupu
akceptovat jako platný oddělovač desetinných míst jak desetinnou tečku, tak desetinnou čárku.
V případě nákupu zadává směnárna měnu a částku, kterou od zákazníka nakupuje, a výstupem je částka v Kč,
kterou zaplatí zákazníkovi. V případě prodeje zadává směnárna měnu a částku, kterou chce zákazník nakoupit a výstupem
je částka v Kč, kterou má zákazník zaplatit. Uživatel jako výstup uvidí směněnou částku zaokrouhlenou na celé koruny.
http://hroch.spseol.cz/~nozka/python/priklad_smenarna/
"""
from tkinter import *


class App:
    def __init__(self, master):
        self.v = IntVar()
        self.amount = IntVar()
        self.buy_price = DoubleVar()
        self.sell_price = DoubleVar()
        self.election = StringVar()
        currency = self.load_currency()
        self.values = self.load_values()

        frame = Frame(master)
        frame1 = Frame(frame)
        frame2 = Frame(frame)
        frame3 = Frame(frame)
        frame4 = Frame(frame)
        frame

        frame.pack()
        frame1.pack()
        frame2.pack()
        frame3.pack(fill=X)
        frame4.pack()

        radio_buy = Radiobutton(frame1, variable=self.v, value=1)
        label_buy = Label(frame1, text="Nákup")
        radio_sell = Radiobutton(frame1, variable=self.v, value=2)
        label_sell = Label(frame1, text="Prodej")

        option_menu = OptionMenu(frame3, self.election, *currency, command=self.change)
        option_menu.config(width=3)
        label_amount = Label(frame3, textvariable=self.amount, padx=25)
        label_buy_price = Label(frame3, textvariable=self.buy_price, padx=10)
        label_sell_price = Label(frame3, textvariable=self.sell_price)

        self.spin = Spinbox(frame4, width=8, from_=1, to=1000)
        self.entry_out = Entry(frame)
        self.entry_out.config(state=DISABLED)
        button = Button(frame4, text="Přepočet", command=self.calculate)

        label_title_currency = Label(frame2, text="Měna", padx=15)
        label_title_amount = Label(frame2, text="Množství", padx=5)
        label_title_buy_price = Label(frame2, text="Nákup", padx=5)
        label_title_sell_price = Label(frame2, text="Prodej")

        radio_buy.pack(side=LEFT)
        label_buy.pack(side=LEFT)
        radio_sell.pack(side=LEFT)
        label_sell.pack(side=LEFT)
        option_menu.pack(side=LEFT)
        label_amount.pack(side=LEFT)
        label_buy_price.pack(side=LEFT)
        label_sell_price.pack(side=LEFT)
        self.spin.pack(side=LEFT)
        button.pack(side=LEFT)
        self.entry_out.pack()

        label_title_currency.pack(side=LEFT)
        label_title_amount.pack(side=LEFT)
        label_title_buy_price.pack(side=LEFT)
        label_title_sell_price.pack(side=LEFT)

    def change(self, *args):
        for i in self.values:
            if i[0] == self.election.get():
                self.amount.set(i[1])
                self.buy_price.set(i[2])
                self.sell_price.set(i[3])
                break

    def load_currency(self):
        currency = ()
        try:
            file = open("listek.txt", "r")
            while True:
                line = file.readline()
                if line != "":
                    currency += (line[0:3],)
                    continue
                break

        except IOError:
            print("Nepodařilo se otevřít listek")
        finally:
            file.close()

        return currency

    def load_values(self):
        values = ()
        try:
            file = open("listek.txt", "r")
            while True:
                line = file.readline()
                if line != "":
                    line = line.replace(",", ".")
                    values += ((line.split()),)
                    continue
                break

        except IOError:
            print("Nepodařilo se otevřít listek")
        finally:
            file.close()
        return values

    def calculate(self):
        self.entry_out.config(state=NORMAL)
        self.entry_out.delete(0, END)

        if self.v.get() == 1:
            self.entry_out.insert(0, float(self.amount.get())*float(self.buy_price.get())*int(self.spin.get()))
        elif self.v.get() == 2:
            self.entry_out.insert(0, float(self.amount.get())*float(self.sell_price.get())*int(self.spin.get()))
        self.entry_out.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
