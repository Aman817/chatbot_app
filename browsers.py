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
        browsers()

def speak():
    pyttsx3.speak("WELCOME TO THE BROWSERS MENU")
    print("=="*60 , end="")    
    print("BROWSERS")
    print("=="*60 , end="")



def browsers():
    pyttsx3.speak("HERE ARE SOME OF THE BROWSERS")
    while True:
        start1.start1()
        print('''\n
            [1]  GOOGLE CHROME
            [2]  MOZILLA FIREFOX
            [3]  MICROSOFT EDGE
                
            [0]  BACK
                    ''')
    
        print("=="*60 , end="")   
        pyttsx3.speak("WHICH BROWSER SHOULD I OPEN")
        a = input("ASK ME ANYTHING: ")
        
        if ((("open" in a) or ("start" in a)) and ("chrome" in a)):
            pyttsx3.speak("CHROME SUCCESSFULLY OPENED")
            os.system("chrome")
            
        elif ((("open" in a) or ("start" in a)) and ("firefox" in a)):
            pyttsx3.speak("FIREFOX SUCCESSFULLY OPENED")
            os.system("firefox")
            time.sleep(1)
        
        elif ((("open" in a) or ("start" in a)) and (("edge" in a) or ("msedge" in a))):
            pyttsx3.speak("MICROSOFT EDGE SUCCESSFULLY OPENED")
            os.system("msedge")
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
            
