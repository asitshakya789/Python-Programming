def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except TypeError as e:
        print(f"Error: {e}")

    finally:
        print("Cleanup: This block always executes.")

# Example usage
divide_numbers(10, 2)  # Result: 5.0, Cleanup: This block always executes.
divide_numbers(10, 0)  # Error: Division by zero is not allowed., Cleanup: This block always executes.
divide_numbers(10, '2')  # Error: unsupported operand type(s) for /: 'int' and 'str', Cleanup: This block always executes.
