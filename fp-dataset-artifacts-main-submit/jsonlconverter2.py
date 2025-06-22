import json

def modify_record(record):
    record['premise'] = record['sentence1']
    record['hypothesis'] = record['sentence2']

    label_text = record['gold_label']
    if label_text == 'entailment':
        record['label'] = 0
    elif label_text == 'neutral':
        record['label'] = 1
    elif label_text == 'contradiction':
        record['label'] = 2
    else:
        raise("Error: unknown text label")

    return record

# Read and modify the data, then write it to a new JSONL file
with open('breaking_nli_dataset\\dataset.jsonl', 'r') as input_file:
    with open('breaking_nli_modified.jsonl', 'w') as output_file:
        for line in input_file:
            record = json.loads(line)
            modified_record = modify_record(record)

            json.dump(modified_record, output_file)
            output_file.write('\n')
