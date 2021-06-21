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


def _not_count_list():
    return print('Count not in count\'s list')


def create_count(count):
    global counts

    if count not in counts:
        counts.append(count)
    else:
        print('Count already in count\'s list')


def create_c():
    count = _get_count_from_user()
    create_count(count)


def list_c():
    print('ID | Company | User | Email | Password | Description')
    print('*' * 50)

    for idx, count in enumerate(counts):
        print('{uid} | {company} | {user} | {email} | {psswd} | {description}'.format(
            uid = idx,
            company = count['company'],
            user = count['user'],
            email = count['email'],
            psswd = count['psswd'],
            description = count['description']
        ))


def search_count(c_company):
    for count in counts:
        if count['company'] != c_company:
            continue
        else:
            return True


def search_c():
    count_name = _get_count_field('company')
    found = search_count(count_name)

    if found:
        print('The count is in the count\'s list')
    else:
        print('The count: {} is not in our count\'s list.'.format(count_name))


def delete_count(c_id):
    global counts

    for idx, count in enumerate(counts):
        if idx == c_id:
            del counts[idx]
            break


def delete_c():
    count_id = int(_get_count_field('id'))
    delete_count(count_id)


def update_count(c_id, updated_c):
    global counts

    if len(counts) - 1 >= c_id:
        counts[c_id] = updated_c
    else:
        _not_count_list()

def update_c():
    count_id = int(_get_count_field('id'))
    updated_count = _get_count_from_user()
    update_count(count_id, updated_count)
