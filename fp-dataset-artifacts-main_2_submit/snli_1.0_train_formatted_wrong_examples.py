import json

from sympy.codegen.ast import continue_
from collections import Counter

# Initialize an empty set to store the numbers
numbers_set = set()

# Open the file and read line by line
with open("snli_1.0_train_wrong_indices_set_1_and_2_and_3.txt", "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the set
        number = int(line.strip())  # strip() removes any leading/trailing whitespace
        numbers_set.add(number)

# Print the set
print(numbers_set)



with open('snli_1.0_train_formatted.jsonl', 'r') as input_file:
#with open('snli_1.0\\snli_1.0_train.jsonl', 'r') as input_file:
    with open('snli_1.0_train_formatted_wrong_examples.jsonl', 'w') as output_file:

        for example_index, line in enumerate(input_file):
            record = json.loads(line)
            if example_index in numbers_set:
                json.dump(record, output_file)
                output_file.write('\n')
                print(f"writing example {example_index} to file")

