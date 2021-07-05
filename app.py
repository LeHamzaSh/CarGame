#Car Game

command = ""

while True:
    command = input("> ").lower()

    if command == "start":
        print("Car Started, Ready to roll!!")

    elif command == "stop":
        print("Car Stopped")

    elif command == "help":
        print("""
start - to start the car
stop -  to stop the car
quit - to terminate the program
        """)

    elif command == "quit":
        print("Quiting program")
        break
    else:
        print("I don't understand what you have entered.")
