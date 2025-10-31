# 1. Function with Default Argument
def greet(name, msg="Hello"):
    print(f"{msg}, {name}")

greet("Devrj")
greet("Harsh", msg="Hi")

# 2. Function Demonstrating Keyword Arguments
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

describe_person("devraj", 17, "Jodhpur")
describe_person(age=20, name="Srishti", city="Udaipur")

# 3. Function with Variable Length Positional Arguments
def add_numbers(*numbers):
    total = sum(numbers)
    print(f"Sum of numbers {numbers} is {total}")

add_numbers(1, 2, 3, 4, 5)
