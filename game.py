import threading
import time
from utils import generate_question, validate_answer

def timed_input(prompt: str, timeout: int):
    """
    Reads user input with a time limit.

    USes a background thread to avoid blocking the main program, allowing 
    the timer to continue running. WOrks on Windows, macOS, and Linux.
    Returns user input or None if time expires.
    """
    result = [None]

    def get_input():
        try:
            result[0] = input(prompt)
        except EOFError:
            result[0] = None

    t = threading.Thread(target=get_input, daemon=True)
    t.start()
    # Wait for the thread to finish or timeout
    # If the time expires, the game continues without blocking
    t.join(timeout)

    return result[0]


def start_game():
    """
    Runs the main game loop for the Multiplication Toaster. 

    The player answers 5 unique multiplication questions within a total time limit
    of 45 seconds. The remaining time is displayed each round.
    The player's score is tracked and displayed at the end, with an option to play again.

    """

    print("Welcome to the Multiplication Toaster!\n"
            "You have 45 seconds to answer 5 multiplication questions.\n"
            "If not, you're toast! :/")

    player_name = input("Please enter your name: ").strip() or "Player"

    score = 0
    questions_asked = 0
    asked_questions = set()

    time_limit = 45  # total game duration (seconds)
    start_time = time.time()

    while questions_asked < 5:
        elapsed_time = time.time() - start_time
        remaining_time = int(time_limit - elapsed_time)

        if remaining_time <= 0:
            print("\nTime's up!")
            break

        question, answer = generate_question(asked_questions)
        print(f"\nQuestion {questions_asked + 1}: {question}")
        print(f"You have {remaining_time} seconds left.")

        user_answer = timed_input("Your answer: ", remaining_time)

        if user_answer is None:
            print("\nTime's up!")
            break

        if validate_answer(user_answer.strip(), answer):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {answer}.")

        questions_asked += 1

    end_game(score, player_name)

def end_game(score, player_name):
    """
    Displays the final score and offers the player the option to play again.
    """
    print(f"\nGame over, {player_name}! Your score: {score}/5")

    print(input("\nPress Enter to continue..."))

    while True:
        play_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if play_again == "yes":
            start_game()
            break
        elif play_again == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    start_game()