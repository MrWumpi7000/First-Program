import sys
import time
import os
from random import randrange

def startup():
    print('Willkommen zum großen und umfassenden programmm von MrWumpi2000')
    print('Taschenrechner (T), File-Opener (F), Vierecks-Rechner (V)')
    start_variable_1 = input('Welches Programm möchten Sie Wählen? ')
    if start_variable_1.upper() == 'TASCHENRECHNER' or start_variable_1.upper() == 'T':
        print('Willkommen zum Taschenrechnerprogramm!')
        berechnung()
    elif start_variable_1.upper() == 'FILE-OPENER' or start_variable_1.upper() == 'F':
        print('Willkommen im File-Opener!')
        file_open()
    elif start_variable_1.upper() == 'VIERECKS-RECHNER' or start_variable_1.upper() == 'V':
        print('Willkommen zum Flächenrechnungsprogramm von Vierecken!')
        viereck_rechung()

def viereck_rechung():
    try: 
        seite_1 = input('Nennen sie mir ihre erste Seite zum Rechnen in cm: ')
        seite_2 = input('Nennen sie mit ihre zweite Seite zum Rechnen in cm: ')
        SEITE_1 = (int(seite_1))
        SEITE_2 = (int(seite_2))
        Ergebnis_for_write = SEITE_1 * SEITE_2
        Ergebnis = SEITE_1 * SEITE_2, 'cm²'
        print(seite_1 + 'cm' + ' * ' + seite_2 + 'cm' + ' = ', SEITE_1* SEITE_2, 'cm²')
        write(seite_1 + 'cm' + ' * ' + seite_2 + 'cm' + ' = ' + str(Ergebnis_for_write) + 'cm²')
        answer_vierecksrechner = ANTWORT('Wollen sie noch einen Flächeninhalt ausrechnen?')
        if answer_vierecksrechner == True:
            viereck_rechung()
        elif answer_vierecksrechner == False:
            sys.exit('Vierecks-Rechner wurde erfolgreich Geschlossen...')
    except:
        Bolean_Variable_1 = ANTWORT('Irgendetwas ist schief gelaufen... Wollen sie es nocheinmal versuchen? ')
           
        if  Bolean_Variable_1 == True:
            viereck_rechung()
        elif  Bolean_Variable_1 == False:
           sys.exit('Vierecks-Rechner wurde erfolgreich Geschlossen...')
def is_valid_task(task):
    try:
        eval(task)
        return True
    except (SyntaxError, ZeroDivisionError, NameError):
        return False

def file_open():
    for file in os.listdir():
        if file.endswith(".txt"):
            print(os.path.join(file))
            
    file = input('Welche Text-datei möchten sie öfnen und berechnen? ')
    
    if not file.endswith('.txt'):
        file = file + ".txt"

    if os.path.exists(file):        
            with open(file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    task = line.strip()
                    if is_valid_task(task):
                        result = eval(task)
                        print(f"{task} = {result}")
                    else:
                        print(task)     
    else:
        print(f"Datei {file} existiert nicht!")
    
    another_file = ANTWORT('Wollen Sie noch eine Datei öffnen? ')
    if another_file == True:
        file_open()
    elif another_file == False:
        sys.exit("File Opener wurde geschlossen")

def ANTWORT(text):
    Input_1 = input(text)
    if Input_1.upper() == 'JA' or Input_1.upper() == 'J':
        Bolean_answer_1 = True
        return Bolean_answer_1
    if Input_1.upper() == 'NEIN' or Input_1.upper() == 'N':
        Bolean_answer_1 = False
        return Bolean_answer_1
    else:
        return ANTWORT('Sie haben nicht mit Ja oder Nein Geantwortet... Bitte versuchen sie es erneut! ')

def write(loesung):
    Input_1 = ANTWORT('Wollen sie das Ergebnis als Text File Gespeichert haben ')
    if Input_1 == True:
        TEST = input('Wie soll ihr File genannt werden? ')
        if os.path.exists(TEST+'.txt'):
            fgs = ANTWORT('Die File gibt es schon... Soll ich die File Löschen? ')
            if fgs == True:
                os.remove(TEST+'.txt')
                file_2.write(loesung)
                file_2.close()
            else:
                return False
        else:
            file_2 = open(TEST+'.txt', "wb")
            file_2.write((loesung).encode('utf8'))

            file_2.close()

def berechnung (): 
    try:
        aufgabe = input('Sagen Sie mir welche Rechnung Sie berechnet haben wollen ')
        loesung = eval(aufgabe)
        print ('Ihr Ergebnis ist =', loesung)
    except:
            Bolean_Variable_1 = ANTWORT('Irgendetwas ist schief gelaufen... Wollen sie es nocheinmal versuchen? ')
            
            if  Bolean_Variable_1 == True:
                berechnung()
            elif  Bolean_Variable_1 == False:
                sys.exit("Taschenrechner wurde erfolgreich geschlossen...")
    else:
        print("Die Rechung wurde erfolgreich berechnetne")
        f_loesung = str(loesung)
        write(str(aufgabe + ' = ' + f_loesung))
        Bolean_Variable_1 = ANTWORT('Wollen sie noch eine weitere Rechnung rechnen? ')
        if  Bolean_Variable_1 == True:
            berechnung()
        elif  Bolean_Variable_1 == False:
            sys.exit("Taschenrechner wurde geschlossen")


startup()