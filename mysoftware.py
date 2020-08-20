import os
import time
import commands
import browsers
import pyttsx3

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
        
def speak():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-10)
    engine.say('WELCOME TO THE WINDOWS TERMINAL USER INTERFACE')
    engine.runAndWait()
    print("=="*60 , end="")    
    print("WELCOME TO WINDOWS TUI:")
    print("=="*60 , end="")



if __name__ =='__main__':
    start()
    speak()    
    commands.start()    
    


