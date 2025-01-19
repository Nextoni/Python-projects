import random
from game_data import data

def Higher_or_lower():
    game_over = False
    points = 0
    char1 = random.choice(data)

    print(f"Your current score is {points} points.\n")

    while not game_over:
        print("Which one has more followers?")
        print(f'Is it "A" {char1["name"]}: {char1["description"]} from {char1["country"]}.\n')

        char2 = random.choice(data)
        while char2 == char1:
            char2 = random.choice(data)
        print(f'Or is it "B" {char2["name"]}: {char2["description"]} from {char2["country"]}.\n')

        choose = input('Which is it "A" or "B"? ').lower()

        if choose == "a" and char1["follower_count"] >= char2["follower_count"]:
            print(f"\n\nThat is correct {char1["name"]} has more followers than {char2["name"]}.")
            points += 1
            print(f"Your current score is {points} points.\n")

        elif choose == "b" and char2["follower_count"] >= char1["follower_count"]:
            print(f"\n\nThat is correct {char2["name"]} has more followers than {char1["name"]}.")
            char1 = char2
            points += 1
            print(f"Your current score is {points} points.\n")

        elif choose == "a" and char1["follower_count"] < char2["follower_count"] or choose == "b" and char2["follower_count"] < char1["follower_count"]:
            print(f"That was incorrect. You scored {points} points.")
            game_over = True

Higher_or_lower()