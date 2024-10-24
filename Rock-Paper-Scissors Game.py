import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["r", "p", "s"])  # r, p, s for rock, paper, scissors

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "s" and computer_choice == "p") or \
         (user_choice == "p" and computer_choice == "r"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")
    print("Choose 'r' for rock, 'p' for paper, or 's' for scissors.")
    
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Your choice (or type 'exit' to quit): ").lower()

        if user_choice == 'exit':
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in ["r", "p", "s"]:
            print("Invalid choice! Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
