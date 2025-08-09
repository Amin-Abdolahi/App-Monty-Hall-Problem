import random

def monty_hall(times):
    wins = 0
    losses = 0
    doors = ["door1", "door2", "door3"]
    change = input("play with change option? y/n default: y").lower()
    for i in range(times):
        prize_door = random.choice(doors)
        goat_doors = [door for door in doors if door != prize_door]
        user_door = random.choice(doors)
        show_door = [door for door in goat_doors if door != user_door]
        change_door = [door for door in doors if door != user_door and door != show_door[0]]
        if change == "y":
            user_door = change_door[0]

        if user_door == prize_door:
            wins += 1
        elif user_door != prize_door:
            losses += 1

    return wins, losses


if __name__ == "__main__":
    print("Monty Hall Problem Simulation")
    input("Press Enter to start the simulation...")
    times = int(input("Enter the number of times to play:"))
    wins, losses = monty_hall(times)
    print(f"Win rate: {wins / times * 100:.2f}%")
    print(f"Loss rate: {losses / times * 100:.2f}%")
