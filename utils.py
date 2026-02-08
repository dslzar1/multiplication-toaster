import random

def generate_question(asked_questions):
    """
    Generates a unique multiplciation question that has not been asked before.

    Parameters:
        - asked_questions (set): A set of questions that have already been asked.

    Returns:
        - tuple: (question string, correct answer)
    """
    while True:
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        question = f"What is {num1} x {num2}?"

        if question not in asked_questions:
            asked_questions.add(question)
            answer = num1 * num2
            return question, answer

def validate_answer(user_answer, correct_answer):
    """
    Validates whether the user's answer is correct.
    Parameters: 
        - user_answer (str): The answer provided by the user.
        - correct_answer (int): The correct answer to the question.

    Returns:
        - bool: True if the user's answer is correct, False otherwise.
    """
    try:
        return int(user_answer) == correct_answer
    except ValueError:
        # handles non-integer inputs gracefully by returning False
        return False