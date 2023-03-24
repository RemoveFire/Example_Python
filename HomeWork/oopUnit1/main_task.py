# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
import sys

import Binding
from oopUnit1.src.controll.controller import input_telefon


def oop_contin():
    while True:
        yes = {'yes', 'ye', 'y'}
        no = {'no', 'n'}
        phrase = input("\n\tIf you want to continue, type 'yes' or type 'no' to exit and end the program: "
                       "\n\tEnter the option you selected(y/n): ")
        if phrase in yes:
            print(f'\nYou have chosen: "{phrase}", therefore, the work of the program will continue \n')
            oopU7Task1()
        elif phrase in no:
            print(f'\nYou have chosen: "{phrase}", therefore, the program is terminated\n')
            Binding.UnitNumberTask()
        else:
            sys.stdout.write("\n\t\t!!!Please enter 'yes' or 'no'!!!"
                             "\n\t\t\t\t(either 'y' or 'n') \n")
            oop_contin()


def oopU7Task1():
    input_telefon()
    oop_contin()
