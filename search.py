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
        search()

def speak():
    pyttsx3.speak("WELCOME TO THE SEARCH MENU")
    print("=="*60 , end="")    
    print("SEARCHING BROWSERS")
    print("=="*60 , end="")



def search():
    while True:
        start1.start3()
        print('''\n
            [1]  SEARCH WITH GOOGLE CHROME
            [2]  SEARCH WITH FIREFOX
            [3]  SEARCH WITH MS EDGE
                
            [0]  BACK
                    ''')
    
        print("=="*60 , end="")   
        pyttsx3.speak("FROM WHICH BROWSER YOU WANT TO SEARCH")
        a = input("YOUR SEARCHING BROWSER: ")
        if ("chrome" in a):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            if ((("open" in a) or ("search" in a)) and ("redhat" in a)):
                os.system("chrome www.redhat.com")      
            elif ((("open" in a) or ("search" in a)) and ("yahoo" in a)):
                os.system("chrome www.yahoo.com")
            elif ((("open" in a) or ("play" in a)) and ("song" in a)):
                os.system("chrome https://www.youtube.com/watch?v=uEJuoEs1UxY")
                time.sleep(4)
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

        elif (("firefox" in a) or ("mozilla" in a)):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            if ((("open" in a) or ("search" in a)) and ("redhat" in a)):
                os.system("firefox www.redhat.com")      
            elif ((("open" in a) or ("search" in a)) and ("yahoo" in a)):
                os.system("firefox www.yahoo.com")
            elif ((("open" in a) or ("play" in a)) and ("song" in a)):
                os.system("firefox https://www.youtube.com/watch?v=uEJuoEs1UxY")
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
        
        elif (("edge" in a) or ("msedge" in a)):
            pyttsx3.speak("WHAT YOU WANT TO SEARCH")
            a = input("TELL SOMETHING: ")
            if ((("open" in a) or ("search" in a)) and ("redhat" in a)):
                os.system("msedge www.redhat.com")      
            elif ((("open" in a) or ("search" in a)) and ("yahoo" in a)):
                os.system("msedge www.yahoo.com")
            elif ((("open" in a) or ("play" in a)) or ("song" in a) or ("songs"  in a)):
                os.system("msedge https://www.youtube.com/watch?v=uEJuoEs1UxY")
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
                
