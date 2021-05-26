from Counts.count import create_c, _initialize_counts_from_storage, _save_counts_to_storage
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
    command =_execute_commands()

    close = False

    while not close:
        if command == 'exit':
            close = True

        elif command == 'mssg':
            send_mssg()
            _spaces()
            command =_execute_commands()

        elif command == 'history -mssg':
            history_mssg()
            _spaces()
            command = _execute_commands()

        elif command == 'create -count':
            create_c()
            _spaces()
            command = _execute_commands()
        
        elif command == 'clear':
            call('clear')
            _spaces()
            command = _execute_commands()

            #------------------------------------------------------------------
        elif command == 'prueba':
            nombre = input("cadena>")
            tratado = nombre.split()

            if tratado[-1] == 'list':
                print(tratado[-1])
               
            elif tratado[0] == 'list': 
                if tratado[1] == '-mssg':
                    print(tratado[1])
                elif tratado[1] == '-count':
                    print(tratado[1])
                else:
                    print('no funciono') 
            else:
                print('no funciono')
            #-----------------------------------------------------------
        else:
            print("  Invalid command")
            _spaces()
            command = _execute_commands()
        
        _save_counts_to_storage()
