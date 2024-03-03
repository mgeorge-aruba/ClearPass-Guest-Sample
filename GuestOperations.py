# This is a sample Python script.

import pyclearpass
from pyclearpass import *
from pprint import pprint
import json
import credsConfig
from password_generator import PasswordGenerator

# Fetch list of all guest accounts. Contains all attributes of all guest accounts
def get_guest_list():
    guest_list = pyclearpass.ApiIdentities.get_guest(login)
    pprint(guest_list)
    return guest_list


# Create new guest account with a random password
def create_guest():
    pwo = PasswordGenerator()
    guest_attributes = {
        'username': 'api-guest-01@aruba.com',
        'email': 'api-guest-01@aruba.com',
        'do_expire': '1',
        'expire_time': 1712043264,
        'role_id': 2,
        'role_name': '[Guest]',
        'simultaneous_use': '1',
        'visitor_name': 'mathew',
        'visitor_phone': '14084567890',
        'password': pwo.generate(),
        'enabled': True
    }
    guest_create = pyclearpass.ApiIdentities.new_guest(login, body=guest_attributes)
    pprint(guest_create)

# Update guest account attributes
def update_guest():
    guest_attributes = {
        'username': 'api-guest-01@aruba.com',
        'email': 'api-guest-01@aruba.com',
        'expire_time': 1712045000,
        'visitor_name': 'api-guest'
    }
    # calling guest update based on username. API also supports guest update based on guest ID. Fetch guest list contains the IDs of guest accounts
    guest_update = pyclearpass.ApiIdentities.update_guest_username_by_username(login, username=guest_attributes["username"], body=guest_attributes)
    pprint(guest_update)






#Configuring ClearPass OAuth client credentials. Creds are stored in separate file credsConfig
#SAMPLE clientid = "CPPM-TMELab-Cloud"
#SAMPLE clientsecret = "D4fg32jBIhdfh454932/1MKOwNEly3wZTok6Lq2ET"

clientid = credsConfig.clientid
clientsecret = credsConfig.clientsecret
login = ClearPassAPILogin(server="https://cxcii.arubasecurity.net:443/api", granttype="client_credentials",clientsecret=clientsecret, clientid=clientid)
guest_list = get_guest_list()
guest_create = create_guest()
guest_update = update_guest()
