import random
import time

def play():
    emojis = ['😀', '🐶', '🍎', '🚗', '🌟', '🎈']
    board = emojis * 2
    random.shuffle(board)
    revealed = ['❓'] * 12
    matched = [False] * 12

    def display():
        print("\nBoard:")
        for i in range(12):
            print(f"{revealed[i]}", end=' ')
            if (i + 1) % 4 == 0:
                print()
        print()

    print("🎮 Welcome to Emoji Memory Match!")
    print("Match all pairs by choosing positions (0–11).")

    while not all(matched):
        display()
        try:
            first = int(input("Choose first position: "))
            second = int(input("Choose second position: "))
            if first == second or not (0 <= first < 12) or not (0 <= second < 12):
                print("⚠️ Invalid positions. Try again.")
                continue
            if matched[first] or matched[second]:
                print("🔁 Already matched. Choose different ones.")
                continue

            revealed[first] = board[first]
            revealed[second] = board[second]
            display()

            if board[first] == board[second]:
                print("✅ Match found!")
                matched[first] = matched[second] = True
            else:
                print("❌ Not a match.")
                time.sleep(1)
                revealed[first] = revealed[second] = '❓'
        except:
            print("⚠️ Invalid input. Use numbers 0–11.")

    print("\n🎉 You matched all emojis! Game over.")

play()
