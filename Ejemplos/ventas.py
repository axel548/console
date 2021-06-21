import csv
import os

CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
CLIENT_TABLE = '.clients.csv'
clients =[]

#------------------------------------------------------------INITIALIZE CLIENTS FROM STORAGE
def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)

#--------------------------------------------------------------------SAVE CLIENTS TO STORAGE
def _save_clients_to_storage():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)

#------------------------------------------------------------------------------CREATE CLIENT
def create_client(client):
   global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already in client\'s list')

#--------------------------------------------------------------------------------LIST CLIENT
def list_clients():
    print('uid | name | company | email | position')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position'])) 


#---------------------------------------------------------------------------UPDATE CLIENTS
def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        _not_client_list()

#------------------------------------------------------------------------------DELETE CLIENT
def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break

#------------------------------------------------------------------------------SEARCH CLIENT
def search_client(client_name):

    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True

#------------------------------------------------------------------------------PRINT WELCOME
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')
    command = input()
    
    return command

#---------------------------------------------------------------------------GET CLIENT FIELD
def _get_client_field(field_name, message = 'What is the client {}?'):
    field = None

    while not field: 
        field = input(message.format(field_name))
   
    return field

#----------------------------------------------------------------------GET CLIENT FROM USER

def _get_client_from_user():
    client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
            }
    return client

#-----------------------------------------------------------------------CLIENT ISN'T IN LIST
def _not_client_list():
    return print('Client not in client\'s list')

#-------------------------------------------------------------------INTERACTION WITH DE USER
if __name__ == '__main__':

    _initialize_clients_from_storage()
    close = False
    command = _print_welcome()

    while not close:
        if command == 'c':
            client = _get_client_from_user()
            create_client(client)
            command =_print_welcome() 

        elif command == 'd':
            client_id = int(_get_client_field('id'))
            delete_client(client_id)
            command =_print_welcome() 

        elif command == 'l':
            list_clients()
            command = _print_welcome() 

        elif command == 'u':
            client_id = int(_get_client_field('id'))
            updated_client = _get_client_from_user()
            update_client(client_id, updated_client)
            command = _print_welcome() 

        elif command == 's':
            client_name = _get_client_field('name')
            found = search_client(client_name)
            if found:
                print('The client is in the client\'s list') 
                command =_print_welcome()       
            else:
                print('The client: {} is not in our client\'s list.'.format(client_name))
                command = _print_welcome()

        elif command == 'exit':
            close = True

        else:
            print('Invalid command')
            command = _print_welcome() 
            
    
        _save_clients_to_storage()
