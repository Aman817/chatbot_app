import os
import time
import pyttsx3
import commands
import speech_recognition as sr
import start1

def start():
        os.system("cls")
        
        print("\n\n\n\t\t           ###>>+++...  ,,,,.._____")
        print("\t\t           ###########  ###########     #####       ##       ##            ##         ######################    ")
        print("\t\t           ###########  ###########    ##    ##     ##       ##          ##  ##                 ##         ")
        print("\t\t           ###########  ###########   ##      ###   ##       ##         ##    ##                ##      ")
        print("\t\t           ###########  ###########   ##            ##       ##        ##       ##              ##     ")
        print("\t\t           ^^^^^^^^^^^  ^^--++::###   ##            ###########       ##############            ##       ")        
        print("\t\t           ###########  ###########   ##            ##       ##      ##            ##           ##        ")
        print("\t\t           ###########  ###########   ##            ##       ##     ##              ##          ##           ")
        print("\t\t           ###########  ###########   ##      ##    ##       ##    ##                ##         ##           ")
        print("\t\t           ###########  ###########    ##    ##     ##       ##   ##                  ##        ##          ")
        print("\t\t           ^^^^^^^^^^^  ^^^^^^++++:      #####      ##       ##  ##                    ##       ##        \n\n")
        speak()
        editors()

def speak():
    pyttsx3.speak("WELCOME TO THE EDIT MENU")
    print("=="*60 , end="")    
    print("EDITORS")
    print("=="*60 , end="")



def editors():
    pyttsx3.speak("HERE ARE SOME OF THE EDITORS")
    while True:
        start1.start2()
        print('''\n
            [1]  NOTEPAD
            [2]  NOTEPAD++
            [3]  WORDPAD
                
            [0]  BACK
                    ''')
    
        print("=="*60 , end="")   
        pyttsx3.speak("WHICH EDITOR SHOULD I OPEN")
        a = input("ASK ME ANYTHING: ")

        if ((("open" in a) or ("start" in a)) and (("notepad" in a) and ("++" not in a))):
            pyttsx3.speak("NOTEPAD SUCCESSFULLY OPENED")
            os.system("notepad")      
        elif ((("open" in a) or ("start" in a)) and (("notepad" in a) and ("++" in a))):
            pyttsx3.speak("NOTEPAD PLUS PLUS SUCCESSFULLY OPENED")
            os.system("notepad++")
            time.sleep(3)
        elif ((("open" in a) or ("start" in a)) and ("wordpad" in a)):
            pyttsx3.speak("WORDPRESS SUCCESSFULLY OPENED")
            os.system("wordpad")
        elif(("previous" in a) or ("return" in a) or ("back" in a)):
            commands.start()
        else:
            print('''
                                            .....
                                       @@@@@@@@@@@@@
                                     @@@@@@@@@@@@@@@@@
                                    @@@@  @@@@@@  @@@@@
                                    @@@@@@@@@@@@@@@@@@@
                                    @@@@@         @@@@@
                                     @@@           @@@
                                       @@@@@@@@@@@@@
                                          ^^^^^^ 
                                
                                        WRONG SEARCH

                        ''')
            pyttsx3.speak("YOU HAVE SEARCHED SOMETHING IRRELEVANT")
            time.sleep(1)
                
        
