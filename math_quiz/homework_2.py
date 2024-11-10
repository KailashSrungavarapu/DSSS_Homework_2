import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.
    
    Parameters:
        min_value (int): The minimum integer value.
        max_value (int): The maximum integer value.
        
    Returns:
        int: A randomly generated integer.
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Select a random arithmetic operator.
    
    Returns:
        str: A random operator from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(num1, num2, operator):
    """
    Formulate a math problem and calculate its incorrect answer deliberately.

    Parameters:
        num1 (int): The first operand.
        num2 (int): The second operand.
        operator (str): The arithmetic operator ('+', '-', '*').

   
    problem_text = f"{num1} {operator} {num2}"
    
  
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return problem_text, answer


def math_quiz():
    """
    Run a math quiz game where the user answers math problems.
    """
    score = 0
    total_questions = 5  # Set a fixed number of questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random operands and operator
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)
        operator = generate_random_operator()

        problem_text, correct_answer = create_math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem_text}")

        # Try-except block to handle invalid user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Move to the next question if the input is invalid

        # Check if the user's answer matches the correct answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
