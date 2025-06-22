import json

from sympy.codegen.ast import continue_
from collections import Counter

def modify_record(record):
    del record['sentence1_binary_parse']
    del record['sentence2_binary_parse']
    del record['sentence1_parse']
    del record['sentence2_parse']

    entailment_count = 0
    neutral_count = 0
    contradiction_count = 0

    for label in record['annotator_labels']:
        if label == "entailment":
            entailment_count += 1
        elif label == "neutral":
            neutral_count += 1
        elif label == "contradiction":
            contradiction_count += 1
        elif label == "":
            continue
        else:
            print(f"weird label: {label}")
            print(f"record['annotator_labels']: {record['annotator_labels']}")
            raise BaseException("label counting error")




    #print(f"entailment_count, neutral_count, contradiction_count = {entailment_count, neutral_count, contradiction_count}")

    record['premise'] = record['sentence1']
    record['hypothesis'] = record['sentence2']

    return record, entailment_count, neutral_count, contradiction_count

def write_record(record, output_file, count, label, original_uid):

    for i in range(count):
        record['label'] = label

        record['uid'] = original_uid
        record['uid'] += '_label_'
        record['uid'] += str(label)
        record['uid'] += '_count_'
        record['uid'] += str(i)

        json.dump(record, output_file)
        output_file.write('\n')

# Read and modify the data, then write it to a new JSONL file

label_counter = Counter()

with open('snli_1.0\\snli_1.0_train.jsonl', 'r') as input_file:
    with open('snli_modified.jsonl', 'w') as output_file:

        multiple_opinions = 0
        examples = 0
        multiple_opinions_2 = 0
        opinion_4 = 0

        for line in input_file:
            record = json.loads(line)
            examples += 1
            if len(record['annotator_labels']) > 1:
                multiple_opinions += 1

            modified_record, entailment_count, neutral_count, contradiction_count = modify_record(record)

            label_count = entailment_count + neutral_count + contradiction_count

            label_counter[label_count] += 1


            if label_count <= 1:
                continue

            if entailment_count >= 4 or neutral_count >= 4 or contradiction_count >= 4:
                continue

            if label_count == 3 and \
                (entailment_count == 3 or neutral_count == 3 or contradiction_count == 3):
                continue

            multiple_opinions_2 += 1

            pairid = record['pairID']

            write_record(modified_record, output_file, entailment_count, 0, pairid)
            write_record(modified_record, output_file, neutral_count, 1, pairid)
            write_record(modified_record, output_file, contradiction_count, 2, pairid)
            json.dump(modified_record, output_file)
            output_file.write('\n')
        print(f"examples = {examples}")
        print(f"multiple_opinions = {multiple_opinions}")
        print(f"multiple_opinions_2 = {multiple_opinions_2}")
        print(f"label_counter = {label_counter}")
        print(f"label_counter_total = {label_counter.total()}")
        print(f"multiple_label_total = {label_counter[3] + label_counter[4] + label_counter[5]}")
