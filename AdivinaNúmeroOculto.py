import random

def app():
    number = random.randint(1, 100)
    dif_level = ""
    chances = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    print("Please select your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard\n")
    
    while dif_level != "1" and dif_level != "2" and dif_level != "3":
        dif_level = input("Enter your choice: ")
    
    if dif_level == "1":
        chances = 10
        print("Great! You have set the difficulty level to easy.")
    elif dif_level == "2":
        chances = 5
        print("Great! You have set the difficulty level to medium.")
    elif dif_level == "3":
        chances = 3
        print("Great! You have set the difficulty level to hard.")
    
    for _ in range(chances):
        number_chosen = int(input("\nEnter your guess: "))
        
        if number_chosen == number:
            print("Congratulations! You guessed the number correctly.")
            return
        elif number_chosen > number:
            print("Your guess is too high. Please try again.")
        elif number_chosen < number:
            print("Your guess is too low. Please try again.")
    
    print(f"Sorry, you ran out of chances. The number was {number}.")


if __name__ == "__main__":
    app()
