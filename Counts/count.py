import csv
import os

COUNT_SCHEMA = ['company', 'user', 'email', 'psswd', 'description']
COUNT_TABLE = '.sslm.csv'
counts = []


def _initialize_counts_from_storage():
    with open(COUNT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=COUNT_SCHEMA)

        for row in reader:
            counts.append(row)


def _save_counts_to_storage():
    tmp_table_name = '{}.tmp'.format(COUNT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=COUNT_SCHEMA)
        writer.writerows(counts)

    os.remove(COUNT_TABLE)
    os.rename(tmp_table_name, COUNT_TABLE)


#---------------------------------------------------------------------------------------------------------------COUNT
def _get_count_field(field_name, message= '  What is the {}? '):
    field = None
    
    while not field:
        field = input(message.format(field_name))

    return field


def _get_count_from_user():
    count = {
            'company': _get_count_field('company'),
            'user': _get_count_field('user'),
            'email': _get_count_field('email'),
            'psswd': _get_count_field('psswd'),
            'description': _get_count_field('description'),
            }

    return count


def create_count(count):
    global counts

    if count not in counts:
        counts.append(count)
    else:
        print('Count already in count\'s list')

def create_c():
    count = _get_count_from_user()
    create_count(count)
