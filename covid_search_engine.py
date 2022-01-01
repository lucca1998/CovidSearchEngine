from pprint import pprint
import tkinter as tk
import datetime

from covid_search_read import read_by_country, read_by_date
import covid_search_read as cov_sr #IntEntry copied from Number_Entry file



 #the main funtion shou run the funtion window_country
def main():
   
    window_country()

#Part 1 (country)
#This function will create a gui in a new window
def window_country():                                                             
    root = tk.Tk()
    frm_main = tk.Frame(root)
    frm_main.master.title("Covid Search Engine - 2020 - Country")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(frm_main, root)                                
    
    root.mainloop()


#this function will create widgets
def populate_main_window(frm_main, root):
    
    Lb1 = tk.Label(frm_main, text="Country: ")
    En1 = tk.Entry(frm_main)   
    Lb1.grid(row=1, column=0, padx=3, pady=3)
    En1.grid(row=1, column=1, padx=3, pady=3)
    btn_clear = tk.Button(frm_main, text="Clear")
    btn_search = tk.Button(frm_main, text="Search")
   
    btn_search.grid(row=2, column=0, padx=3, pady=3, columnspan=5)
    btn_clear.grid(row=2, column=2, padx=3, pady=3, columnspan=5)

    btn_new = tk.Button(frm_main, text="New window")
    btn_new.grid(row=3,column=0, padx=3, pady=3, columnspan=5)

    btn_change = tk.Button(frm_main, text="Date Search")
    btn_change.grid(row=3, column=2 , padx=3, pady=3, columnspan=10)


    #this funtion will create a new window and you will search by date
    def change():
        window_date()
    btn_change.config(command=change)
    

    #this funtion is a button that will double the window and you can search 
    # two different countries and compare the final data
    def new_window():
        window_country()
    btn_new.config(command=new_window)

    #this function allows to press "enter" and run the search
    def enter(event):
        search()
    root.bind('<Return>', enter)

    #This function calls the list in the covid_search_read.py which reads from data.csv
    def search():
           
        try:
        
            country_list = read_by_country("data.csv", Entry=En1.get())
            
            total_death =0
            total_cases =0
            best_so_far2 = -1
            best_so_far3 = -1
            print("Country, Date, Cases, Deaths, Deaths per 100000")
            for item in country_list:
                                
                print(item)
                country = item[0]
                deaths = item[3]
                cases = item[2]
                total_death += deaths
                total_cases += cases
                date = item[1]

                if deaths > best_so_far2:
                    best_so_far2 = deaths
                    date_ = date
                if cases > best_so_far3:
                    best_so_far3 = cases
                    date__ = date


            country = country.replace("_", " ")
            text = f"""
{country} in 2020:
Total: {total_cases} cases, {total_death} deaths 
Largest number of deaths: {date_} - {best_so_far2}
Largest number of cases: {date__} - {best_so_far3}
"""
            print(text)

            lbl3 = tk.Label(frm_main, text=text)        
            lbl3.grid(row=1, column=5, padx=3, pady=3, columnspan=25)
            def clear1():
                
                lbl3.config(text="")
                En1.delete(0, tk.END)
                En1.config(text="")
            btn_clear.config(command=clear1)
            
        
        except (FileNotFoundError, PermissionError) as error:
            print(type(error).__name__, error, sep=": ")
            print("There is no such file")

    #this function clear all the labels in the gui
    def clear():
        
        En1.delete(0, tk.END)
        En1(text="")
        En1.focus()


    btn_search.config(command=search)
    btn_clear.config(command=clear)
    En1.focus()


#part2 (date)
#This function will create a gui in a new window
def window_date():
    root = tk.Tk()
    frm_main = tk.Frame(root)
    frm_main.master.title("Covid Search Engine - 2020 - Date")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_date(frm_main, root)                                
    root.mainloop()
 
#this function will create widgets
def populate_main_date(frm_main, root):
    Lb1 = tk.Label(frm_main,text="Month: ")
    Lb2 = tk.Label(frm_main,text="Day: ")
    
    En1 = cov_sr.IntEntry(frm_main,1,12, width=5)   #month enter
    En2 = cov_sr.IntEntry(frm_main,1,31, width=5)   #day enter
    Lb1.grid(row=0, column=0, padx=3, pady=3)
    Lb2.grid(row=1, column=0, padx=3, pady=3)
    En1.grid(row=0, column=1, padx=3, pady=3)
    En2.grid(row=1, column=1, padx=3, pady=3)
    btn_clear = tk.Button(frm_main, text="Clear", width=7)
    btn_search = tk.Button(frm_main, text="Search")
   
    
    
    btn_search.grid(row=2, column=0, padx=3, pady=3, columnspan=5)
    btn_clear.grid(row=2, column=4, padx=3, pady=3, columnspan=5)


    btn_new = tk.Button(frm_main, text="New window")
    btn_new.grid(row=3,column=0, columnspan=5)

    btn_change = tk.Button(frm_main, text="Country")
    btn_change.grid(row=3, column=4 , padx=8, pady=8, columnspan=12)

    #this funtion will create a new window and you will search by country
    def change():
        window_country()
    btn_change.config(command=change)

    #this function allows to press "enter" and run the search
    def enter(event):
        En2.focus()
        def enter(event):
            search()
        root.bind('<Return>', enter)    
    root.bind('<Return>', enter)

    #this funtion is a button that will double the window and 
    #you can search two different dates and compare the final data
    def new_window():
        window_date()

    btn_new.config(command=new_window)
    


    #This function calls the list in the covid_search_read.py which reads from data.csv

    def search():
        if En1.get() < 10: #month
            if En2.get() < 10: #day
                entry = f"0{En2.get()}/0{En1.get()}/2020"
            else:
                entry = f"{En2.get()}/0{En1.get()}/2020"
        elif En1.get()>9: #month
            if En2.get() > 9: #day
                entry = f"{En2.get()}/{En1.get()}/2020"
            else:
                entry = f"0{En2.get()}/{En1.get()}/2020"
        try:
        
            #the entry is a important part of the file, it will get the user input
            #and use it to search the especifi information the user request
            country_list = read_by_date("data.csv", Entry=entry)
            
            total_death =0
            total_cases =0
            best_so_far1 = -1
            best_so_far2 = -1
            print("Date, Country, Cases, Deaths, Deaths per 100000")

            for item in country_list:
                print(item)
                country = item[1]
                deaths = item[3]
                cases = item[2]
                total_death += deaths
                total_cases += cases
                
                date = item[0]

                if deaths > best_so_far1:
                    best_so_far1 = deaths
                    new_country1 = country.replace("_", " ")
                if cases > best_so_far2:
                    best_so_far2 = cases
                    new_country2 = country.replace("_", " ")
                
            #as the date is in the european format (dd-mm-yyyy), 
            # it provide a way to read in the american format (mm-dd-yyyy)   
            parts = date.split('/')
            day = int(parts[0])
            monthint = int(parts[1])
            year= int(parts[2])

            month = datetime.date(1900, monthint, 1).strftime('%B')


            final_date = (f"{month} {day}, {year}")

            tex = f"""
In {final_date}:
Total in the world: {total_cases} cases, {total_death} deaths 
Largest number of deaths: {new_country1} - {best_so_far1}
Largest number of cases: {new_country2} - {best_so_far2}
"""
            print(tex)

            lbl3 = tk.Label(frm_main, text=tex)        
            lbl3.grid(row=5, column=0, padx=3, pady=3, columnspan=25)
            def clear1():
                lbl3.config(text="")
                En1.delete(0, tk.END)
                En1.config(text="")
                En2.delete(0, tk.END)
                En2.config(text="")
                En1.focus()
            btn_clear.config(command=clear1)
            
        
        except (FileNotFoundError, PermissionError) as error:
            print(type(error).__name__, error, sep=": ")
            print("There is no such file")

    #this function clear all the labels in the gui        
    def clear():
        En1.delete(0, tk.END)
        En1(text="")
        En2.delete(0, tk.END)
        En2(text="")
        En1.focus()
    btn_search.config(command=search)
    btn_clear.config(command=clear)
    En1.focus()



if __name__ == "__main__":
    main()