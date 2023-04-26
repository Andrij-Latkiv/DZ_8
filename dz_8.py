from datetime import datetime, timedelta


users = [
    { 'name' : 'Oleg', 'birthday' : datetime(year = 1988, month = 4, day = 25 )},
    { 'name' : 'Oleksandr', 'birthday' : datetime(year = 1987, month = 9, day = 25 )},
    { 'name' : 'Ivan', 'birthday' : datetime(year = 1987, month = 10, day = 12 ) },
    { 'name' : 'Petro', 'birthday' : datetime(year = 1990, month = 4, day = 30 )},
    { 'name' : 'Volodya', 'birthday' : datetime(year = 1989, month = 1, day = 22 )},
    { 'name' : 'Mykola', 'birthday' : datetime(year = 1991, month = 4, day = 26 )},
    { 'name' : 'Myhaylo', 'birthday' : datetime(year = 1995, month = 4, day = 26 )},
    { 'name' : 'Georgij', 'birthday' : datetime(year = 1995, month = 4, day = 27 )}
]


#-----------поточний--тиждень------------------------------------------------------------------------------
def week():

    week_now = []

    week_day = datetime.now()

    period = timedelta(days=6)
    delta = timedelta(days = 1)
    delta_2 = timedelta(days = 2)
    
    if week_day.weekday() != 0:

        week_end = week_day + period     

        while week_day <= week_end:
            week_now.append(week_day.date())
            week_day += delta
            
        return week_now
    else:

        week_day = week_day - delta_2
        week_end = week_day + period     

        while week_day <= week_end:
            week_now.append(week_day.date())
            week_day += delta
            
        return week_now

#------------------------------------------------------------------------------------------

def print_name_bd(sp):
    if not sp:
        return 'no birthdays'
    else:
        name = ' '
        for i in sp:
            name  += i + ' '
        return name

#------------------------------------------------------------------------------------------

def get_birthday_per_week(data):
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    monday = []
    today = datetime.now()

    for sl in data:
        
        name, bd = sl.values()
              
        bd = bd.replace(year = today.year)
                
        if bd.date() in week():
            
            if bd.weekday() == 1:
                tuesday.append(name)
                
            elif bd.weekday() == 2:
                wednesday.append(name)
                
            elif bd.weekday() == 3:
                thursday.append(name)
                
            elif bd.weekday() == 4:
                friday.append(name)
                
            else:
                monday.append(name)

    

    print(f'Monday: {print_name_bd(monday)}\nTuesday: {print_name_bd(tuesday)}\nWednsday: {print_name_bd(wednesday)}\nThursday: {print_name_bd(thursday)}\nFriday: {print_name_bd(friday)}')



        
            
    
    
if __name__ == '__main__':

    get_birthday_per_week(users)


