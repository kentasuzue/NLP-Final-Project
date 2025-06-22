import json

from sympy.codegen.ast import continue_
from collections import Counter

category_totals = {
    'antonyms': 1147,
    'synonyms': 894,
    'cardinals': 759,
    'nationalities': 755,
    'drinks': 731,
    'antonyms_wordnet': 706,
    'colors': 699,
    'ordinals': 663,
    'countries': 613,
    'rooms': 595,
    'materials': 397,
    'vegetables': 109,
    'instruments': 65,
    'planets': 60}

label_totals = {
    'entailment': 982,
    'neutral': 47,
    'contradiction': 7164}

# Initialize an empty set to store the numbers
numbers_set = set()

# Open the file and read line by line
with open(".\\process_dataset_D2\\trained_MNLI_model_epochs_3_SNLI_epochs_1_lr_2e-7_breaking_stats\\wrong_indices.txt", "r") as file:
    for line in file:
        # Convert each line to an integer and add it to the set
        number = int(line.strip())  # strip() removes any leading/trailing whitespace
        numbers_set.add(number)

# Print the set
print(numbers_set)

category_count = Counter()
label_count = Counter()

with open('breaking_nli_modified.jsonl', 'r') as input_file:
    with open('.\\process_dataset_D2\\trained_MNLI_model_epochs_3_SNLI_epochs_1_lr_2e-7_breaking_stats\\breaking_wrong_examples.jsonl', 'w') as output_file:
        for example_index, line in enumerate(input_file):
            record = json.loads(line)
            if example_index in numbers_set:
                json.dump(record, output_file)
                output_file.write('\n')
                print(f"writing example {example_index} to file")

                category = record['category']
                category_count[category] += 1

                label = record['gold_label']
                label_count[label] += 1

print(category_count)

category_ratios = Counter()
for key in list(category_count.keys()):
    category_ratios[key] = category_count[key] / category_totals[key]
print(category_ratios)


print(label_count)

label_ratios = Counter()
for key in list(label_count.keys()):
    label_ratios[key] = label_count[key] / label_totals[key]
print(label_ratios)

with open('.\\process_dataset_D2\\trained_MNLI_model_epochs_3_SNLI_epochs_1_lr_2e-7_breaking_stats\\breaking_summary_stats.jsonl', 'w') as output_file2:
    output_file2.write(json.dumps(category_totals))
    output_file2.write('\n')

    output_file2.write(json.dumps(category_count))
    output_file2.write('\n')

    output_file2.write(json.dumps(category_ratios))
    output_file2.write('\n')

    output_file2.write(json.dumps(label_totals))
    output_file2.write('\n')

    output_file2.write(json.dumps(label_count))
    output_file2.write('\n')

    output_file2.write(json.dumps(label_ratios))
    output_file2.write('\n')
