import json

from sympy.codegen.ast import continue_
from collections import Counter

# Initialize an empty set to store the numbers
numbers_set_1 = set()
numbers_set_2 = set()
numbers_set_3 = set()

numbers_set_1_or_2 = set()
numbers_set_1_or_3 = set()
numbers_set_2_or_3 = set()

numbers_set_1_or_2_or_3 = set()

numbers_set_1_and_2 = set()
numbers_set_1_and_3 = set()
numbers_set_2_and_3 = set()

numbers_set_1_and_2_and_3 = set()


# Open the file and read line by line
with open("wrong_indices_epochs_1.txt", "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the set
        number = int(line.strip())  # strip() removes any leading/trailing whitespace
        numbers_set_1.add(number)
        numbers_set_1_or_2.add(number)
        numbers_set_1_or_3.add(number)
        numbers_set_1_or_2_or_3.add(number)

with open("wrong_indices_epochs_2.txt", "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the set
        number = int(line.strip())  # strip() removes any leading/trailing whitespace
        numbers_set_2.add(number)
        numbers_set_1_or_2.add(number)
        numbers_set_2_or_3.add(number)
        numbers_set_1_or_2_or_3.add(number)

with open("wrong_indices_epochs_3.txt", "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the set
        number = int(line.strip())  # strip() removes any leading/trailing whitespace
        numbers_set_3.add(number)
        numbers_set_1_or_3.add(number)
        numbers_set_2_or_3.add(number)
        numbers_set_1_or_2_or_3.add(number)

print(f"len(numbers_set_1): {len(numbers_set_1)}")
print(f"len(numbers_set_2): {len(numbers_set_2)}")
print(f"len(numbers_set_3): {len(numbers_set_3)}")
print(f"len(numbers_set_1_or_2): {len(numbers_set_1_or_2)}")
print(f"len(numbers_set_1_or_3): {len(numbers_set_1_or_3)}")
print(f"len(numbers_set_2_or_3): {len(numbers_set_2_or_3)}")
print(f"len(numbers_set_1_or_2_or_3): {len(numbers_set_1_or_2_or_3)}")

numbers_set_1_and_2 = numbers_set_1.intersection(numbers_set_2)
numbers_set_1_and_3 = numbers_set_1.intersection(numbers_set_3)
numbers_set_2_and_3 = numbers_set_2.intersection(numbers_set_3)

numbers_set_1_and_2_and_3 = numbers_set_1_and_2.intersection(numbers_set_3)

print(f"len(numbers_set_1_and_2): {len(numbers_set_1_and_2)}")
print(f"len(numbers_set_1_and_3): {len(numbers_set_1_and_3)}")
print(f"len(numbers_set_2_and_3): {len(numbers_set_2_and_3)}")
print(f"len(numbers_set_1_and_2_and_3): {len(numbers_set_1_and_2_and_3)}")

# with open(f"snli_1.0_train_wrong_indices_set_1_and_2_and_3.txt", "w") as file:
with open(f"snli_1.0_train_wrong_indices_set_1_and_2_and_3.txt", "w") as file:
    for index in sorted(list(numbers_set_1_and_2_and_3)):
        file.write(f"{index}\n")  # Convert to string and write each item on a new line
