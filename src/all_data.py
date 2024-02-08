from src.country import Country
import json
import pprint
import csv



class All_data():
    """
    class defining a container associated countries whit their associated Leaders 
    """
    def __init__(self, number_of_countries : int = 5):
        self.countries = [Country() for i in range(number_of_countries)]
        self.number_of_countries = number_of_countries
        self.number_of_countries_affected = 0

    def assign_country(self, name):
        """assigns leaders to an empty room"""
        self.countries[self.number_of_countries_affected].name = name
        self.number_of_countries_affected += 1 


                    
  
    def display(self):
        """"display a panda view of Countries & Leaders"""
        list_export = []
        list_export.append(["Country", "First Name", "Last Name", "Birth date", "Death date", "Place of birth", 
                            "Start mandate", "End mandate", "Wikipedia URL", "First paragraph"])
        
        for i in range(self.number_of_countries):
            for j in range(self.countries[i].number_leaders):
                list_export.append([self.countries[i].name,
                                    self.countries[i].Leaders[j].first_name,
                                    self.countries[i].Leaders[j].last_name,
                                    self.countries[i].Leaders[j].birth_date,
                                    self.countries[i].Leaders[j].death_date,
                                    self.countries[i].Leaders[j].place_of_birth,
                                    self.countries[i].Leaders[j].start_mandate,
                                    self.countries[i].Leaders[j].end_mandate,                                    
                                    self.countries[i].Leaders[j].wikipedia_url,
                                    self.countries[i].Leaders[j].first_paragraph
                ])

        return(list_export)
    
    def export_csv(self, list_csv):
        """ Export the list to the csv file """
        fichier_csv = 'list_Countries_Leaders_EXPORT.csv'
        with open(fichier_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for ligne in fichier_csv:
                writer.writerow(ligne)
     
        print("Exportation terminée avec succès.")

        
                                                                        
