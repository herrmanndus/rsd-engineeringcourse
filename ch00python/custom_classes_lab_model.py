
# experimenting DH: can I write a class to a .py file and import it? 

class Lab:
    def __init__(self,name,capacity):
        self.name = name
        self.scientists = {} # note that this is not a required input. if you want to initialize it with a default do as below for scientist
        self.capacity = capacity
        
    def is_full(self):
        return len(self.scientists) > self.capacity
    
    def add_scientist(self,scientist):
        scientist.lab_name = self.name
        scientist.lab = self # important so you can access the lab functions from a scientist object
        self.scientists[scientist.name] = scientist # assign a scientist object to the lab onject (dict entry)
        
    def delete_scientist(self,scientist):
        del self.scientists[scientist.name] 
        

# define a class called scientist which has some attributes (name, projects, collaborations etc.)

class Scientist:
    def __init__(self,name,interests,age,location, lab = None): # init lab as None such that
        self.name = name
        self.interests = interests # list of interests
        self.age = age
        self.location = location
        self.lab = lab
        
    def switch_labs(self,to_lab):
        self.lab.delete_scientist(self)
        destination_lab = to_lab
        destination_lab.add_scientist(self)
        print(self.name, " has a new job at ", destination_lab.name)
        
    def how_old_is(self):
        print(self.name, " is", self.age, " years old")
    
    def where_do_they_work(self):
        if bool(self.lab):
            print(self.name, " works in the ", self.lab.name, " lab")
        else:
            print(self.name, "has no lab")
                
    def is_interested_in(self):
        if bool(self.interests):
            print(self.name, " is interested in ", " & ".join(self.interests))
        else:
            print(self.name, " has no interests")
                                  
    def tell_me_about_your_lab(self):
        if bool(self.lab):
            print("My lab is called",self.lab.name, "lab")
            print("My colleagues are", " & ".join(self.lab.scientists.keys()))
        else:
            print("I have no lab")

