from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
import random
import time
import pickle
import joblib


eae = "деревянная удочка"
carb = True
iron = True
bambo = True
alu = True
money = 0
lvlfish = [0, 3, 3, 6, 6, 12]
fish1 = 0
fish2 = 0
fish3 = 0
verfish = []

#C:/Users/Asus/Desktop/всякое/кодики (pycharm)/Basic code/code/save_game.pkl



class int(GridLayout, BoxLayout):
    def fishing(self):
        global fish1
        global fish2
        global fish3

        fish1 = fish1 + random.randint(lvlfish[0], lvlfish[1])
        fish2 = fish2 + random.randint(lvlfish[2], lvlfish[3])
        fish3 = fish3 + random.randint(lvlfish[4], lvlfish[5])



        global verfish
        verfish = [fish1, fish2, fish3, eae]
        self.fishlvl1.text = str(verfish )



    def sell(self):
        global money
        global fish1
        global fish2
        global fish3

        for mon in range(fish1):
            money = money + 1
            fish1 = fish1 - 1

        for mon in range(fish2):
            money = money + 0.5
            fish2 = fish2 - 1

        for mon in range(fish3):
            money = money + 0.25
            fish3 = fish3 - 1

        self.lab_money.text = str(money)
        self.fishlvl1.text = str(verfish)

        #self.lab_money.text = str(verfish)

    def sel_carb(self):
        self.bayt.text = ("карбоновая удочка \n "
                         " 150000 ")

    def sel_iron(self):
        self.bayt.text = ("стальная удочка \n "
                                 " 25000 ")

    def sel_bamb(self):
        self.bayt.text = ("бамбуковая удочка \n "
                          " 5000 ")

    def sel_alu(self):
        self.bayt.text = ("алюминивая удочка \n "
                          " 75000 ")



    def buy(self):
        global money
        global lvlfish
        global eae
        global carb
        global iron
        global bambo
        global alu

        if carb == True:
            if money >= 150000:

                money = money - 150000
                lvlfish[0] = 10
                lvlfish[1] = 20
                lvlfish[2] = 20
                lvlfish[3] = 40
                lvlfish[4] = 40
                lvlfish[5] = 80

                eae = "карбованая удочка"
                carb = False

            else:
                self.bt_buy.text = "не достаточно денег"

        if iron == True:
            if money >= 25000:

                money = money - 25000
                lvlfish[0] = 3
                lvlfish[1] = 6
                lvlfish[2] = 6
                lvlfish[3] = 12
                lvlfish[4] = 12
                lvlfish[5] = 24

                eae = "стальная удочка"
                iron = False

            else:
                self.bt_buy.text = "не достаточно денег"

            if bambo == True:
                if money >= 5000:
                    money = money - 5000
                    lvlfish[0] = 2
                    lvlfish[1] = 4
                    lvlfish[2] = 4
                    lvlfish[3] = 8
                    lvlfish[4] = 8
                    lvlfish[5] = 16

                    eae = "бамбуковая удочка"
                    bambo = False

                else:
                    self.bt_buy.text = "не достаточно денег"

            if alu == True:
                if money >= 75000:
                    money = money - 75000
                    lvlfish[0] = 5
                    lvlfish[1] = 10
                    lvlfish[2] = 10
                    lvlfish[3] = 20
                    lvlfish[4] = 20
                    lvlfish[5] = 40

                    eae = "алюминивая удочка"
                    alu = False


                else:
                    self.bt_buy.text = "не достаточно денег"

class fishApp(App):
    def build(self):

        return int()




if __name__ == "__main__":
    fishApp().run()