import random


def factorial(n):
    """Calculate the factorial of a number."""
    fct = 1
    for i in range(1, n + 1):
        fct *= i
    return fct


def solve_linear_equation():
    """Generate a random linear equation ax + b = 0 and calculate its solution."""
    while True:
        a = random.randint(1, 10)
        if a != 0:  # Ensure 'a' is non-zero to avoid division by zero
            break
    b = random.randint(1, 10)
    x = -b / a
    return a, b, x


def is_prime(val):
    """Check if a number is prime."""
    if val <= 1:
        return False
    if val == 2:
        return True
    if val % 2 == 0:
        return False
    for i in range(3, int(val ** 0.5) + 1, 2):
        if val % i == 0:
            return False
    return True


def nearest_prime(n):
    """Find the nearest prime number greater than or equal to n."""
    while not is_prime(n):
        n += 1
    return n


def math_roulette_challenge():
    """Present a math roulette challenge with random operations."""
    numbers = [random.randint(1, 20) for _ in range(5)]
    operation = random.choice(['addition', 'subtraction', 'multiplication'])

    if operation == "addition":
        res = sum(numbers)
        operation_sign = "+"
    elif operation == "subtraction":
        res = numbers[0]
        for num in numbers[1:]:
            res -= num
        operation_sign = "-"
    elif operation == "multiplication":
        res = 1
        for num in numbers:
            res *= num
        operation_sign = "*"

    numbers_str = f" {operation_sign} ".join(map(str, numbers))
    print(f"Calculate the result of: {numbers_str}")

    try:
        user_answer = int(input("Your answer: "))
        if user_answer == res:
            print("Correct! Well done!")
            return True
        else:
            print(f"Wrong! The correct answer was {res}.")
            return False
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False


def math_challenge():
    """Math challenges where the game asks the question and validates the player's answer."""
    challenges = ["factorial", "is_prime", "nearest_prime", "math_roulette", "solve_linear_equation"]
    selected_challenge = random.choice(challenges)
    print(f"Selected challenge: {selected_challenge}")

    if selected_challenge == "factorial":
        number = random.randint(3, 7)
        correct_answer = factorial(number)
        print(f"What is the factorial of {number}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! Well done!")
                return True
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")
                return False
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return False

    elif selected_challenge == "is_prime":
        number = random.randint(2, 50)
        correct_answer = is_prime(number)
        print(f"Is {number} a prime number? (yes or no)")
        user_answer = input("Your answer: ").strip().lower()
        if (user_answer == "yes" and correct_answer) or (user_answer == "no" and not correct_answer):
            print("Correct! Well done!")
            return True
        else:
            correct_text = "yes" if correct_answer else "no"
            print(f"Wrong! The correct answer is '{correct_text}'.")
            return False

    elif selected_challenge == "nearest_prime":
        number = random.randint(10, 30)
        correct_answer = nearest_prime(number)
        print(f"What is the nearest prime number greater than or equal to {number}?")
        try:
            user_answer = int(input("Your answer: "))
            if user_answer == correct_answer:
                print("Correct! Well done!")
                return True
            else:
                print(f"Wrong! The correct answer is {correct_answer}.")
                return False
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return False

    elif selected_challenge == "math_roulette":
        return math_roulette_challenge()

    elif selected_challenge == "solve_linear_equation":
        a, b, x = solve_linear_equation()
        print(f"Solve the linear equation: {a}x + {b} = 0")
        try:
            user_answer = float(input("Your answer: x = "))
            if abs(user_answer - x) < 0.01:  # Allow minor floating-point differences
                print("Correct! Well done!")
                return True
            else:
                print(f"Wrong! The correct answer is x = {x:.2f}.")
                return False
        except ValueError:
            print(f"Invalid input. The correct answer is x = {x:.2f}.")
            return False


# Run the math challenge
