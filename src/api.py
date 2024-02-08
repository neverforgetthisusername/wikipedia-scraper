import json
import src.utils as utils

from datetime import datetime
import requests
from bs4 import BeautifulSoup
import re


root_url = "https://country-leaders.onrender.com"
status_url = f"{root_url}/status"
cookie_url = f"{root_url}/cookie"
check_url = f"{root_url}/check"
countries_url = f"{root_url}/countries"
leaders_url = f"{root_url}/leaders"
leader_url = f"{root_url}/leader"


def get_cookie():
    """ get the cookie on the cookie_url"""
    print("********Get cookie********\n")
    text_status, cookieresp = utils.requests_check(status_url)
    text_cookies, mycookie = utils.requests_check(cookie_url)
    text_check, cookieresp = utils.requests_check(check_url, mycookie)
    return mycookie

def load_data():
    """extract data and save it in a flie.txt"""
    mycookie = get_cookie()
    print("********COUNTRIES********\n")
    text_countries, cookieresp = utils.requests_check(countries_url, mycookie)
    list_json_countries = json.loads(text_countries)
    print("---countries extracted---")
    print(list_json_countries)
    print("********LEADERS********\n")
    cpt = 0
    list_import = []

    for country in list_json_countries[:]:                           #for testing and reduce time, change the borders
        list_leaders = []
        cpt += 1
        print(f"\n************************* COUNTRY  N° {cpt} = {country}")
        texte_req_atrt, cookie_req_atrt = utils.requests_check(leaders_url + "?country=" + country, mycookie)
        listjson_req_atrt = json.loads(texte_req_atrt)
        for elem in listjson_req_atrt:  
            firstparagraph = create_first_paragraph(elem["wikipedia_url"])
            list_leaders.append([elem["id"], elem["first_name"], elem["last_name"], 
                                elem["birth_date"], elem["death_date"],  
                                elem["place_of_birth"],  
                                elem["start_mandate"], elem["end_mandate"],
                                elem["wikipedia_url"], firstparagraph
                                ])
            
            """# not used (data from leader_url are the same)
            print("********LEADERS********\n")
            texte_req_atrt, cookie_req_atrt = utils.requests_check(leader_url + "?leader_id=" + elem, mycookie)
            listjson_req_atrt = json.loads(texte_req_atrt)"""
        print(firstparagraph)
        #print("list_leaders ", list_leaders)
        list_import.append([country, list_leaders])
    # Save the imported data in a file.txt
    save_file_import(list_import)
    return list_import   
   

def create_first_paragraph(url):
    # Extract the first paragraph from the content
    req_url = requests.get(url)
    soup = BeautifulSoup(req_url.text, 'html.parser')
    first_paragraph = ""
    paragraphs = soup.find_all('p')
    first_paragraph = paragraphs[0].text.strip()
    
    # clean caracters between () or []
    clean_text = re.sub(r'\[.*?;?\]', '', first_paragraph)  # Remove Wikipedia references
    clean_text = re.sub(r'\(.*?;?\)', '', clean_text)       # Remove phonetic pronunciations
    return clean_text

def save_file_import(list_import):
    # Save ExportFile as export_%date time%.txt 
    now = datetime.now()
    now_string = now.strftime("%Y-%m-%d %H-%M-%S")
    file_import = "API_Import_" + now_string + ".txt"
    with open(file_import, 'w', encoding='utf-8') as f:
        # Convert list to str and save the data imported
        f.write(str(list_import))
    print("\n********************  " + file_import + "     SUCCESFULL")

  