class Leader():
    """
    Class defining Leader 
    Leaders will be assigned to countries
    """
    def __init__(
            self, idleader : str = "", first_name : str = "", 
            last_name : str = "", birth_date: str = "",
            death_date: str = "", place_of_birth: str = "",
            start_mandate: str = "", end_mandate: str = "", 
            wikipedia_url: str = "", first_paragraph: str = ""
    ):
        self.idleader = idleader
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.place_of_birth = place_of_birth
        self.start_mandate = start_mandate
        self.end_mandate = end_mandate
        self.wikipedia_url = wikipedia_url
        self.first_paragraph = first_paragraph

    def set_leader(self, idleader, 
                   first_name, last_name, 
                   birth_date, death_date, 
                   place_of_birth,  
                   start_mandate, end_mandate, 
                   wikipedia_url, first_paragraph
    ):
        self.idleader = idleader
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.death_date = death_date
        self.place_of_birth = place_of_birth
        self.start_mandate = start_mandate
        self.end_mandate = end_mandate
        self.wikipedia_url = wikipedia_url
        self.first_paragraph = first_paragraph
        


class Country():
    """ classe definig the countries that will be assigned to the AllData"""
    def __init__(self, name : str = None, number_leaders : int = 100):
        self.name = name                                                           
        self.number_leaders = number_leaders
        self.leaders_assigned = 0
        self.Leaders = [Leader() for i in range(self.number_leaders)]      #list of allocated Leader()  
        #self.Leaders = [Leader("1","","","","","","","","","") for i in range(self.number_leaders)]      #list of allocated Leader()  

        #self.Seats =  [Seat(True, "Name Occupant Seat") for i in range(self.capacity)] 
    
    def assign_leader(self, idleader, 
                first_name, last_name, 
                birth_date, death_date, 
                place_of_birth,  
                start_mandate, end_mandate, 
                wikipedia_url, first_paragraph
    ):
        """add a leader to the country"""
        self.Leaders[self.leaders_assigned].set_leader(idleader,first_name, last_name, birth_date, death_date, place_of_birth, start_mandate, end_mandate, wikipedia_url, first_paragraph)
        self.leaders_assigned += 1
