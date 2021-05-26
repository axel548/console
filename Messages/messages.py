import pywhatkit as kt
import os

def _get_info_mssg(field_name, message = '  What is the {}?'):
    field = None
    
    while not field:
        field = input(message.format(field_name))

    return field

def _get_info_from_user():
    mssg = {
            'contact': _get_info_mssg('contact'),
            'message': _get_info_mssg('message'),
            'hour': _get_info_mssg('hour'),
            'minute': _get_info_mssg('minute'),
            }

    return mssg

def create_mssg(mssg):
    kt.sendwhatmsg(""+str(mssg['contact'])+"",""+str(mssg['message'])+"", int(mssg['hour']), int(mssg['minute']))


# Enviar mensaje -- Función exportable
def send_mssg():
    mssg = _get_info_from_user()
    create_mssg(mssg)
   
def history_mssg():
    kt.showHistory()
 

'''
try:
    wt.playonyt("Sayuri - Mikazuki")
    wt.shutdown(time=100)
    wt.cancelShutdown()
    wt.send_mail("axel.aatl@gmail.com", "katonendan40", "Test email", "This is a test email", "tuchezlopezaxelabel@gmail.com")
except:
    print("An Unexpected Error!")
'''
