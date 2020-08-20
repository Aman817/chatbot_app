import os
import time
import pyttsx3
import browsers
import speech_recognition as sr
import notepad
import search

def start():
    while True:
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
         print("=="*60 , end="")    
        print("WELCOME TO WINDOWS TUI:")
        print("=="*60 , end="")
        commands()

def commands():
    print()
    print('''
        [1]    BROWSERS
        [2]    WMPLAYER
        [3]    EDITORS
        [4]    SYSTEM INFO
        [5]    IP ADDRESS
        [6]    TREE
        [7]    ATTRIB
        [8]    PING
        [9]    NETWORK PORTS
        [10]   SEARCH WITH BROWSER 
        [11]   JAVA
        [12]   PYTHON
        [13]   JUPYTER NOTEBOOK   
            ''')
            
    print("=="*60 , end="")   
    pyttsx3.speak("ASK ME ANYTHING")
    '''r = sr.Recognizer()
    mic = sr.Microphone(device_index=1)

    with mic as source:
        print("ASK ME ANYTHING.....")
        audio =  r.listen(source)
     
    a = r.recognize_google(audio)'''
    a = input("ASK ME ANYTHING: ")
   
    if (("open" in a) or ("start" in a) or ("show" in a)) and (("browser" in a) or ("webbrowser" in a) or ("browsers" in a)):
        browsers.start()
    elif (("open" in a) or ("start" in a)) and (("wmplayer" in a) or ("player" in a)):
        os.system("wmplayer")
        input("\nPRESS ENTER TO CONTINUE....")
    elif ((("open" in a) or ("show" in a)) and ("editors" in a)):
        notepad.start()
    elif ((("open" in a) or ("show" in a)) and ("system" in a)):
        os.system("msinfo32")
        input("\nPRESS ENTER TO CONTINUE....")
    elif ((("open" in a) or ("show" in a)) and ("ip" in a)):
        os.system("ipconfig")
        input("\nPRESS ENTER TO CONTINUE....")
    elif ((("open" in a) or ("show" in a)) and ("tree" in a)):
        os.system("tree")
        input("\nPRESS ENTER TO CONTINUE....")
    elif ((("open" in a) or ("show" in a)) and ("attribute" in a)):
        os.system("attrib")
        input("\nPRESS ENTER TO CONTINUE....")
    elif ((("open" in a) or ("show" in a)) and  (("ports" in a) or ("port"  in a))):
        os.system("netstat")    
        input("\nPRESS ENTER TO CONTINUE....")
    elif (("open" in a) or ("search" in a)) and (("browser" in a) or ("webbrowser" in a) or ("browsers" in a)):
        search.start()
    elif (("ping" in a)):
        os.system("ping")
        input("\nPRESS ENTER TO CONTINUE....")
    elif (("java" in a)):
        os.system("java")
        input("\nPRESS ENTER TO CONTINUE....")
    elif (("python" in a)):
        os.system("python")
        input("\nPRESS ENTER TO CONTINUE....")
    elif (("jupyter" in a)):
        os.system("jupyter noteebook")
        input("\nPRESS ENTER TO CONTINUE....")
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
        


   