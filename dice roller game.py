import random

def roll_dice(num_dice=1):
    """Simulates rolling dice and returns the results.

    Args:
        num_dice: The number of dice to roll (default is 1).

    Returns:
        A list containing the results of each dice roll.
    """
    roll_results = []
    for _ in range(num_dice):
        roll_results.append(random.randint(1, 6))
    return roll_results

if __name__ == "__main__":
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? (Enter 0 to quit): "))
            if num_dice == 0:
                break
            if num_dice < 0:
                raise ValueError
            results = roll_dice(num_dice)
            print("Results:", results)
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")
