print("---Welome to AI Chatbot")
print("->Type 'bye' to Exit!")

while True:
    
    user=input("you: ").lower()
    if "hello" in user:
        print("bot: how are you?")
    elif "fine" in user:
        print("bot: great to hear that what can i help?")
    elif "course" in user:
        print("bot: you have selected AI Course.")
    elif "language" in user:
        print("bot: python programing.")
    elif "what is your age?" in user:
        print("bot: sorry i dont understand your qustion..")
    elif "class" in user:
        print("bot: MCA B1")
    elif "university" in user:
        print("bot: Marwadi")
    elif "town" in user:
        print("bot: rajkot")
    elif "bye" in user:
        print("bot: goodbye thank you! have a nice day..")
        break    

    else:
        print("sorry! i dont understand your question..")

    
