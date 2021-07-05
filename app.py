#Car Game

command = ""

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        print("Car Started, Ready to roll!!")

    elif command == "stop":
        print("Car Stopped")