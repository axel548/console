from Counts.count import create_c, list_c, search_c, delete_c, update_c, _initialize_counts_from_storage, _save_counts_to_storage
from Scrapers import scraper as s
from Messages.messages import send_mssg, history_mssg

from subprocess import call
import time

#------------------------------------------------------------------------------------------------------------------------

def _spaces():  
    print('')


def _execute_commands():
    date = time.strftime('%Y-%m-%d', time.localtime())
    print("",date)
    command = input(" >")

    return command


#--------------------------------------------------------------------------------------MAIN
if __name__ == '__main__':

    _initialize_counts_from_storage()     
    print(' Hello, I am V.E.R.O.N.I.C.A') 
    print(' Select a command')
    _spaces()
    cmd =_execute_commands()
    command = cmd.split()

    close = False

    while not close:
        if command[-1] == 'exit':
            close = True


        elif command[-1] == 'history':
            history_mssg()
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()

        
        elif command[-1] == 'clear':
            call('clear')
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()
        

        elif command[-1] == 'list':
            list_c()
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()


        elif command[-1] == 'search':
            search_c()
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()


        elif command[-1] == 'delete':
            delete_c()
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()


        elif command[-1] == 'update':
            update_c()
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()


        elif command[0] == 'create':
            if command[-1] == '-mssg':
                send_mssg()
                _spaces()
                cmd = _execute_commands()
                command = cmd.split()

            elif command[-1] == '-count':
                create_c()
                _spaces()
                cmd = _execute_commands()
                command = cmd.split()

            else:
                _spaces()
                cmd = _execute_commands()
                command = cmd.split()


        else:
            print("  Invalid command")
            _spaces()
            cmd = _execute_commands()
            command = cmd.split()
        
        _save_counts_to_storage()
