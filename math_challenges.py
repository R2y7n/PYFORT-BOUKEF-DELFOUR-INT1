import random


def factorial(n):
    fct = 1
    for i in range(1, n + 1):
        fct = fct * i
    return fct


def solve_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    x = -b / a

    return a, b, x


def is_prime(val):
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
    # Find the first prime number greater than or equal to n.

    while not is_prime(n):  # Keep checking numbers until a prime is found
        n += 1
    return n


def math_roulette_challenge():
    # Generate 5 random numbers between 1 and 20
    numbers = [random.randint(1, 20) for _ in range(5)]

    # Randomly select an operation
    operation = random.choice(['addition', 'subtraction', 'multiplication'])

    # Calculate the result based on the selected operation
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

    # Format the numbers for display
    numbers_str = f" {operation_sign} ".join(map(str, numbers))
    print(f"Calculate the result of: {numbers_str}")

    # Get the user's answer
    try:
        user_answer = int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False

    # Check the user's answer
    if user_answer == res:
        print("Correct! You win!")
        return True
    else:
        print(f"Wrong! The correct answer was {res}. Better luck next time!")
        return False


def math_challenge():
    # Define the available challenges with their argument requirements
    challenges = {
        "factorial": {
            "function": factorial,
            "requires_input": True,
            "prompt": "Enter a positive integer for the factorial calculation: ",
            "validate": lambda x: x.isdigit() and int(x) >= 0,  # Ensure input is a non-negative integer
            "input_type": int,
        },
        "is_prime": {
            "function": is_prime,
            "requires_input": True,
            "prompt": "Enter a positive integer to determine if it’s a prime number: ",
            "validate": lambda x: x.isdigit() and int(x) > 0,  # Ensure input is a positive integer
            "input_type": int,
        },
        "nearest_prime": {
            "function": nearest_prime,
            "requires_input": True,
            "prompt": "Enter a positive integer to find the nearest prime: ",
            "validate": lambda x: x.isdigit() and int(x) > 0,  # Ensure input is a positive integer
            "input_type": int,
        },
        "math_roulette": {
            "function": math_roulette_challenge,
            "requires_input": False,
        },
        "solve_linear_equation": {
            "function": solve_linear_equation,
            "requires_input": False,
        },
    }

    # Randomly select a challenge
    selected_challenge = random.choice(list(challenges.keys()))
    challenge_details = challenges[selected_challenge]

    print(f"Selected challenge: {selected_challenge}")

    # Handle challenges that require user input
    if challenge_details["requires_input"]:
        while True:
            user_input = input(challenge_details["prompt"])
            if challenge_details["validate"](user_input):
                user_input = challenge_details["input_type"](user_input)
                break
            else:
                print("Invalid input. Please try again.")

        # Execute the selected function with the user's input
        result = challenge_details["function"](user_input)
        print(f"Result: {result}")
        return True
    else:
        # Execute the selected function without input
        result = challenge_details["function"]()
        if selected_challenge == "solve_linear_equation":
            a, b, x = result
            print(f"Linear equation: {a}x + {b} = 0")
            try:
                sol = float(input("Solve the linear equation: x = "))
                if sol == x:
                    print("Correct! The solution is right.")
                else:
                    print(f"Wrong! The correct solution is x = {x:.2f}")
            except ValueError:
                print(f"Invalid input. The correct solution is x = {x:.2f}")
        return True


print(math_challenge())
