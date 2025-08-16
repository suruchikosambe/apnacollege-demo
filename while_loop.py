favourite_language = {}

program = input("Do you want to enter the data for the favourite programming language : ").lower().strip()
if program == "yes":
    print("Enter the following data.")
    while True:
        name = input("Enter your name : ").lower().strip()
        language = input("Enter the language : ").lower().strip()
        favourite_language[name] = language
        print("\nYour data is successfully added in the dictionary.")
        for name , language in favourite_language.items():
            print(f"{name.title()} : {language.title()}")
        while True:
            conti = input("\nDo you want to enter more data like yours friends : ").lower().strip()
            if conti == "yes" or "no":
                break
            else:
                print("Enter 'yes' or 'no'")
                continue
        if conti == "yes":
            continue
        else:
            print("Following are the data you have added : ")
            for name , language in favourite_language.items():
                print(f"{name.title()} : {language.title()}")
            break
elif program == "no":
    print(f"thank you for your response may participate in another poll.")

