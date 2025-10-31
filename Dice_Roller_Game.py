import random

def roll_dice():
    return random.randint(1, 6)

def play():
    print("🎲 Welcome to the Dice Roller Challenge!")
    score = 0

    for round in range(1, 6):
        input(f"\nRound {round}: Press Enter to roll the dice...")
        user_roll = roll_dice()
        computer_roll = roll_dice()

        print(f"You rolled: {user_roll}")
        print(f"Computer rolled: {computer_roll}")

        if user_roll > computer_roll:
            print("✅ You win this round!")
            score += 1
        elif user_roll < computer_roll:
            print("❌ You lose this round!")
        else:
            print("🤝 It's a tie!")

    print(f"\n🏁 Game Over! Your final score: {score}/5")

play()
