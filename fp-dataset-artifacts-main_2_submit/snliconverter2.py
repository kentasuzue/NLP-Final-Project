import json

from sympy.codegen.ast import continue_
from collections import Counter

def modify_record(record):
    del record['sentence1_binary_parse']
    del record['sentence2_binary_parse']
    del record['sentence1_parse']
    del record['sentence2_parse']

    record['premise'] = record['sentence1']
    record['hypothesis'] = record['sentence2']

    text_label = record['gold_label']

    if text_label == 'entailment':
        record['label'] = 0
    elif text_label == 'neutral':
        record['label'] = 1
    elif text_label == 'contradiction':
        record['label'] = 2
    else:
        record['label'] = -1

    return record

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

with open('snli_1.0\\snli_1.0_dev.jsonl', 'r') as input_file:
#with open('snli_1.0\\snli_1.0_test.jsonl', 'r') as input_file:
#with open('snli_1.0\\snli_1.0_train.jsonl', 'r') as input_file:
    with open('snli_1.0_dev_formatted.jsonl', 'w') as output_file:
    #with open('snli_1.0_test_formatted.jsonl', 'w') as output_file:
    #with open('snli_1.0_train_formatted.jsonl', 'w') as output_file:

        for line in input_file:
            record = json.loads(line)

            modified_record = modify_record(record)


            pairid = record['pairID']

            if modified_record['label'] != -1:
                json.dump(modified_record, output_file)
                output_file.write('\n')
