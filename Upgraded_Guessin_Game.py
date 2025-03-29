import random

def show_rules():
    """Display game rules when requested."""
    print("""
    📜 The Rules:
     1.Guess the correct number ➝ *2 points* 🎯
    2.Guess within 5 of the correct number ➝ *1 point* ✅
    3.Fail to guess in 3 attempts ➝ PC gets *1 point* ❌
    4.First to reach 5 points wins 🏆
    """)

def get_valid_number():
    """Prompt user for a valid integer input, handling rules display."""
    while True:
        user_input = input("Enter your guess (or type 'rules' for help): ")
        
        if user_input.lower() == "rules":
            show_rules()
            continue  # Show rules and ask for input again
        
        if user_input.isdigit():
            return int(user_input)  # Convert to integer and return
        
        print("⚠️ Invalid input! Please enter a number.")

def play_game():
    """Main game loop."""
    pc_score = 0
    user_score = 0

    print("\n🎮 Welcome to the Number Battle!")
    print("💻 VS 🧑‍💻 — Who will win?\n")

    while pc_score < 5 and user_score < 5:
        print("\nNew Round!\n")
        random_number = random.randint(1, 100)
        awarded = False  # Track if points were given in this round

        for attempt in range(3):
            num = get_valid_number()

            if num == random_number:
                print("🎯 Correct! You earn *2 points*!")
                user_score += 2
                awarded = True
                break  # End round early if correct
            elif abs(num - random_number) <= 5 and not awarded:
                print("✅ Close! You earn *1 point*!")
                user_score += 1
                awarded = True  # Prevent multiple close-guess points
                break  # End round after awarding 1 point
            else:
                print("❌ Wrong guess. Try again!")

        if not awarded:  # If no points were earned
            print(f"😢 Out of attempts! The correct number was *{random_number}*.")
            pc_score += 1

        print(f"\n📊 Scoreboard:\n💻 PC: {pc_score} | 🧑‍💻 User: {user_score}")

    # Announce winner
    if user_score >= 5:
        print("\n🏆 *Congratulations! The User wins!* 🎉")
    else:
        print("\n💻 *Game Over! The PC wins!* 😢")

    input("\nPress Enter to exit...")

# Run the game
play_game()
