# import the requests library 
import requests
from bs4 import BeautifulSoup
import re
import time 

import json
from pprint import pprint
import src.api as api


#define dictionary of Staus_Code Errors 
dict_resp_get_url = {
    "1": "informational response – the request was received, continuing process",                  
    "2": "successful – the request was successfully received, understood, and accepted",           
    "3": "redirection – further action needs to be taken in order to complete the request",        
    "4": "client error – the request contains bad syntax or cannot be fulfilled",                  
    "5": "server error – the server failed to fulfil an apparently valid request"                  
    }

# check the status_code using a condition and print appropriate messages
def check_status_code(code):
    if code ==200:
        print("STATUS CODE ", code, "            Standard response for successful HTTP requests")
    else :
        print("STATUS CODE ", code, " => ", str(code)[0], "XX", dict_resp_get_url[str(code)[0]])


# edit the text of the request when request Status Caode == 200
def requests_check(explore_url, cookief=None, parameters=None):
        cpt = 0
        while True:
            print("URL : ", explore_url)
            if cookief == None and parameters == None:
                print("COOKIE   None \nPARAMS   None")
                req = requests.get(explore_url)
            elif cookief != None and parameters == None :
                print("COOKIE   used \nPARAMS   None\ncookie : ", cookief)
                req = requests.get(explore_url, cookies=cookief)
            elif cookief != None and parameters != None:
                print("COOKIE   used \nPARAMS   used\ncookie : ", cookief, "\nparams : ",parameters)
                req = requests.get(explore_url, cookies=cookief, params=parameters )
         
            check_status_code(req.status_code)
        
            if req.status_code == 200:
                texte = req.text
                cookief = req.cookies
                print("cookie : ", cookief)
                break
            elif cpt < 2:
                print(" ...Resended...")
                time.sleep(5.0)
                cookief = api.get_cookie()
                cpt += 1
            else:
                print("ERROR utils/request_check!!!")
                exit() 
        return texte, cookief


def display_after_processing():

    print("\n\n\n*********************************************************")
    print("*********************************************************")
    print("********           ERROR FREE PROCESSING            *****")
    print("********             Export File created            *****")
    print("********                                            *****")
    print("*********************************************************")
    print("*********************************************************")
    return_value = input("\n                     What's your choice ? \n")
    return return_value





