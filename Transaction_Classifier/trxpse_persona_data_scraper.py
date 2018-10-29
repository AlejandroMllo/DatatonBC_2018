import sys
import csv

from random import shuffle, seed

labeled_data = []
unlabeled_data = []

csv.field_size_limit(sys.maxsize)

# Data Loading & Classification (labeled/unlabeled)
dataset_path = # 'dt_trxpse_personas_2016_2018_muestra_adjt.csv'
with open(dataset_path) as dataset:

    entries = csv.reader(dataset)

    i = 0
    for entry in entries:

        mod_entry = entry.copy()
        if len(entry) > 8:
            if entry[8] == '\\N' or entry[8] == ' ':
                mod_entry[8] = ''
            if entry[9] == '\\N' or entry[9] == ' ':
                mod_entry[9] = ''
            if entry[10] == '\\N' or entry[10] == ' ':
                mod_entry[10] = ''

            if not (mod_entry[8] == mod_entry[9] == mod_entry[10] == ''):
                labeled_data.append(mod_entry)
            else:
                unlabeled_data.append(mod_entry)
        else:
            unlabeled_data.append(entry)

        i += 1

        if i % 500000 == 0:
            print('******', i)

# Data Persistence
seed(1)
shuffle(labeled_data)
shuffle(unlabeled_data)

with open('LABELED_DATA_TRXPSE_BC.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',',
                             quotechar="'", quoting=csv.QUOTE_MINIMAL)
    data_writer.writerows(labeled_data)

with open('UNLABELED_DATA_TRXPSE_BC.csv', 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile, delimiter=',',
                             quotechar="'", quoting=csv.QUOTE_MINIMAL)
    data_writer.writerows(labeled_data)

# Data Stats
print('data length =', i)
print('labeled data length =', len(labeled_data))
print('unlabeled data length =', len(unlabeled_data))