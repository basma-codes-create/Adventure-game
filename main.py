import time
import random

# ======================
# GAME STATE
# ======================
player_score = 0
current_level = 1
game_active = True
lives = 3


# ======================
# UTILITIES
# ======================
def print_pause(message, delay=1.5):
    print(message)
    time.sleep(delay)


def validate_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print_pause(f"Invalid input. Choose from: {', '.join(options)}")


def show_status():
    print_pause(f"\n Lives: {lives} |  Score: {player_score}\n")


# ======================
# LEVEL 1
# ======================
def level_one():
    global player_score, lives, current_level

    print_pause("\nLEVEL 1: The mystery forest")
    print_pause("You wake up in a mystery forest full of trees and birds sounds")
    print_pause("You have a bag contains:a rope, a compass and a torch")

    events = [
        "You hear someone's footsteps nearby...",
        "A bird flys over your head...",
        "The weather become colder and foggy..."
    ]
    print_pause(random.choice(events))

    while True:
        show_status()
        print_pause("\nChoose your own way:")
        print_pause("1. Follow the water stream sound")
        print_pause("2. Climb over a tall tree for some fruits")
        print_pause("3. Stay and wait for anyone to help you")

        choice = validate_input("Enter (1-3): ", ["1", "2", "3"])

        if choice == "1":
            print_pause("You find a a river and drinkable water")
            player_score += 15
        elif choice == "2":
            print_pause("You fall down from the tree and hurt your head")
            player_score -= 5
            lose_life()
        else:
            print_pause("No one comes to help... but luckly you a way out of the forest")
            player_score += 5

        break

    level_transition()


# ======================
# LEVEL 2
# ======================
def level_two():
    global player_score, lives

    print_pause("\n LEVEL 2: The ancient ruins")
    print_pause("You enter an old ruin covered in roooted grass and dust")

    correct = random.randint(1, 3)

    paths = [
        "It smells like flowers",
        "Have some fresh footprints",
        "Cold and foggy"
    ]

    while True:
        show_status()
        print_pause("\nChoose a path:")

        for i in range(3):
            print_pause(f"{i+1}. {paths[i]}")

        choice = validate_input("Enter (1-3): ", ["1", "2", "3"])

        if int(choice) == correct:
            print_pause("Congrats you found a golden ancient box")
            player_score += 25
            break
        else:
            print_pause("You get in a trap...but you escape it and get hurt")
            player_score -= 10
            lose_life()

            if lives <= 0:
                break

    level_transition()


# ======================
# LEVEL 3
# ======================
def level_three():
    global player_score, game_active

    print_pause("\nLEVEL 3: The wizard's tower")
    print_pause("A huge door blocks your way in... and a deep voice speaks: 'Solve my riddle to get in'")

    riddles = [
        ("I speak without a mouth. What am I?",
         ["1. Book", "2. Echo", "3. Shadow"], "2",
         "It repeats sound"),

        ("What gets water while it dries?",
         ["1. Towel", "2. Sun", "3. River"], "1",
         "You use it after water")
    ]

    question, options, answer, hint = random.choice(riddles)

    print_pause("\n" + question)

    for opt in options:
        print_pause(opt)

    attempts = 2

    while attempts > 0:
        show_status()
        choice = validate_input("Your answer (1-3): ", ["1", "2", "3"])

        if choice == answer:
            print_pause("That's right, The door opens... and you find the treasure inside")
            player_score += 50
            break
        else:
            attempts -= 1
            print_pause(f"Wrong answer, try again Hint: {hint}")
            if attempts > 0:
                print_pause(f"Attempts left: {attempts}")
            else:
                print_pause("The wizard rejects you and throw you away from the tower")
                player_score -= 20

    end_game()


# ======================
# HELP SYSTEM
# ======================
def lose_life():
    global lives
    lives -= 1
    print_pause(f"You lost a life Remaining: {lives}")

    if lives <= 0:
        print_pause("You ran out of lives")
        end_game()


# ======================
# LEVEL TRANSITION
# ======================
def level_transition():
    global current_level

    if lives <= 0:
        return

    if current_level == 1:
        print_pause("\nWould you like to go to the next level or replay this one?")
        choice = validate_input("1. Yes  2. Replay level: ", ["1", "2"])

        if choice == "1":
            current_level = 2

    elif current_level == 2:
        print_pause("\nWould you like to go to the final level or replay this one?")
        choice = validate_input("1. Yes  2. Replay level: ", ["1", "2"])

        if choice == "1":
            current_level = 3


# ======================
# END GAME
# ======================
def end_game():
    global game_active

    print_pause("\nGAME OVER")

    if player_score >= 70:
        print_pause("That was amazing: You become a brave explorer, congrats")
    elif player_score >= 40:
        print_pause("That was not bad: You survived the adventure with honor")
    else:
        print_pause("That was bad: The forest will find another explorer")

    game_active = False


# ======================
# GAME LOOP
# ======================
def play_game():
    global current_level, game_active

    while game_active:
        if current_level == 1:
            level_one()
        elif current_level == 2:
            level_two()
        elif current_level == 3:
            level_three()

    play_again()


def play_again():
    global player_score, current_level, game_active, lives

    choice = validate_input("\nPlay again? (y/n): ", ["y", "n"])

    if choice == "y":
        player_score = 0
        current_level = 1
        lives = 3
        game_active = True
        play_game()
    else:
        print_pause("Thank you for your playing")


# ======================
# START GAME
# ======================
def main():
    print_pause("Welcome to the Adventure Game")
    print_pause("Make tour choices wisely... every choice matters")
    print_pause("You have 3 lives. Good luck and have fun\n")

    play_game()


if __name__ == "__main__":
    main()