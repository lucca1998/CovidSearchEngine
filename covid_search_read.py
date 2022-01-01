import csv
import tkinter as tk


def read_by_country(filename, Entry):
   
    country_list_dates = []
   
    country_wish = ''
    country_wish = Entry
   
    #this section will help to shortain the research process, 
    #the password reads "United_States_of_America" or "United_Kingdom"
    #but you can type just 'usa' or 'united states' and it will work also
    ok = True
    while ok:
        #if the input is similiar to "usa", the computer will understand
        #that the user wants information about the United States
        if country_wish == "Usa" or country_wish=="usa" or country_wish=="united states" or country_wish=="united states of america" or country_wish== "United States" or country_wish== "United States Of America" or country_wish== 'United_States_of_America':
            country_wish = "United_States_of_America"
            ok = False
        elif country_wish != "Usa":
            #the following lines will change "brazil" to "Brazil"
            #and "united kingdom" to "United_Kingdom"
            #and it will be able to read the input
            country_wish = country_wish.title()
            country_wish = country_wish.replace(" ", "_")
            ok = False
        else:
            ok = True
            print("Wrong input, try again")
    else:    
        with open (filename, "rt") as data:


            reader = csv.reader(data)
            next(reader)

            for x in data:
                column = x.split(",")
                date= column[0]
                cases = int(column[4])
                deaths = int(column[5])
                country = column[6]
                per = column[11]
                per100000 = per.strip("\n")

                if country_wish == country:
                    country_list_dates.append([country, date, cases, deaths, per100000])
                    
                   
    return country_list_dates


def read_by_date(filename, Entry):
   
    day_list_dates = []
    day_wish = Entry

    
    with open (filename, "rt") as data:
        reader = csv.reader(data)
        next(reader)
        for x in data:
            column = x.split(",")
            date= column[0]
            cases = int(column[4])
            deaths = int(column[5])
            country = column[6]
            per = column[11]
            per100000 = per.strip("\n")
            if day_wish == date:
                day_list_dates.append([date, country, cases, deaths, per100000])
                
               
    return day_list_dates



class IntEntry(tk.Entry): 
    """An Entry widget that accepts only
    integers between a lower and upper bound.
    """
    def __init__(self, parent, lower_bound, upper_bound, **kwargs):
        super().__init__(parent)
        if lower_bound > 1:
            lower_bound = 1
        if upper_bound < -1:
            upper_bound = -1
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = max(len(str(lower_bound)), len(str(upper_bound)))
        kwargs["validate"] = "key"
        kwargs["validatecommand"] = (parent.register(self.validate), "%P")
        self.config(**kwargs)

    def validate(self, value_if_allowed):
        valid = False
        try:
            i = int(value_if_allowed)
            valid = (str(i) == value_if_allowed and
                    self.lower_bound <= i and i <= self.upper_bound)
        except:
            valid = (len(value_if_allowed) == 0 or
                    (self.lower_bound < 0 and value_if_allowed == "-"))
        return valid

    def get(self):
        """Return the integer that the user entered."""
        return int(super().get())

    def set(self, n):
        """Display the integer n for the user to see."""
        self.delete(0, tk.END)
        self.insert(0, str(int(n)))
