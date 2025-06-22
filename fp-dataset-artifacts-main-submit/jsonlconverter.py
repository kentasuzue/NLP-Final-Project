import json

def modify_record(record):
    del record['label_counter']
    del record['majority_label']
    del record['label_dist']
    del record['entropy']

    entailment_count, neutral_count, contradiction_count = record['label_count']
    #print(f"entailment_count, neutral_count, contradiction_count = {entailment_count, neutral_count, contradiction_count}")

    record['premise'] = record['example']['premise']
    record['hypothesis'] = record['example']['hypothesis']

    return record, entailment_count, neutral_count, contradiction_count

def write_record(record, output_file, count, label, original_uid):

    for i in range(count):
        record['label'] = label

        record['uid'] = original_uid
        record['uid'] += '_label_'
        record['uid'] += str(label)
        record['uid'] += '_count_'
        record['uid'] += str(i)

        json.dump(modified_record, output_file)
        output_file.write('\n')

# Read and modify the data, then write it to a new JSONL file
with open('chaosNLI_v1.0\\chaosNLI_snli.jsonl', 'r') as input_file:
    with open('chaosNLI_snli_modified.jsonl', 'w') as output_file:
        for line in input_file:
            record = json.loads(line)
            modified_record, entailment_count, neutral_count, contradiction_count = modify_record(record)

            original_uid = record['uid']

            write_record(modified_record, output_file, entailment_count, 0, original_uid)
            write_record(modified_record, output_file, neutral_count, 1, original_uid)
            write_record(modified_record, output_file, contradiction_count, 2, original_uid)
            # json.dump(modified_record, output_file)
            # output_file.write('\n')
