import random

"""Generate a random integer between the given min and max values """
def generate_integer(min, max):
    
    return random.randint(min, max)

"""Generate a random arithmetic operator: '+', '-', or '*' """
def generate_operator():
    
    return random.choice(['+', '-', '*'])

"""Perform the arithmetic operation based on the given operator and return the problem and the correct answer """
def perform_operation(num1, num2, operator):
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2

    problem = f"{num1} {operator} {num2}"
    return problem, result

"""Main function to run the Math Quiz game """
def math_quiz():
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_integer(1, 10)
        num2 = generate_integer(1, 5)
        operator = generate_operator()


        problem, answer = perform_operation(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
