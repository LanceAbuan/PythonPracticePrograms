import speech_recognition as sr
import random as rd

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something and I'll print out whatever you say")
    audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        if text == "how good-looking am I":
            print(text)
            print("You are a",rd.randint(1,10))
        print("Input:",text)
        text = text.split(" ")


        if text[0] == "8Ball" or text[0]+text[1]=="8ball" or text[0] == "eight-ball":
            choice = rd.randint(0,6)
            if choice == 0:
                print("Yes")
            elif choice == 1:
                print("No")
            elif choice == 2:
                print("Maybe")
            elif choice == 3:
                print("Definitely")
            elif choice == 4:
                print("Definitely Not")
            elif choice == 5:
                print("Ask again")
            elif choice == 6:
                print("Not Sure")
                

    except:
        print("I'm sorry, I could not understand you.")