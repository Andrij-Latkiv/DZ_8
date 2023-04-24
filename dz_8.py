from datetime import datetime, timedelta, date


users = [
    { 'name' : 'Oleg', 'birthday' : datetime(year = 1988, month = 4, day = 25 )},
    { 'name' : 'Oleksandr', 'birthday' : datetime(year = 1987, month = 9, day = 25 )},
    { 'name' : 'Ivan', 'birthday' : datetime(year = 1987, month = 10, day = 12 ) },
    { 'name' : 'Petro', 'birthday' : datetime(year = 1990, month = 4, day = 30 )},
    { 'name' : 'Volodya', 'birthday' : datetime(year = 1989, month = 1, day = 22 )},
    { 'name' : 'Mykola', 'birthday' : datetime(year = 1991, month = 4, day = 26 )},
    { 'name' : 'Myhaylo', 'birthday' : datetime(year = 1995, month = 2, day = 26 )},
    { 'name' : 'Georgij', 'birthday' : datetime(year = 1995, month = 4, day = 24 )}
]


#-----------поточний--тиждень------------------------------------------------------------------------------
def week():

    week_day = datetime.now()
    period = timedelta(days=6)
    delta = timedelta(days = 1)
    week_end = week_day + period

    week_now = []

    while week_day <= week_end:
        week_now.append(week_day.date())
        week_day += delta
        
    
    return week_now

#------------------------------------------------------------------------------------------

days_name = {
    0 : 'Понеділок',
    1 : 'Вівторок',
    2 : 'Середа',
    3 : 'Четвер',
    4 : "П'ятниця",
    5 : 'Субота',
    6 : 'Неділя'
}

#------------------------------------------------------------------------------------------

def get_birthday_per_week(data):
    
    for sl in data:
        
        name, bd = sl.values()
            
        for d in week():

            if d.strftime('%d/%m') == bd.strftime('%d/%m'):
                
                if days_name.get(d.weekday()) == days_name[1]:
                    print(f'{days_name.get(d.weekday())} - {name}')

                elif days_name.get(d.weekday()) == days_name[2]:
                    print(f'{days_name.get(d.weekday())} - {name}')
                    
                elif days_name.get(d.weekday()) == days_name[3]:
                    print(f'{days_name.get(d.weekday())} - {name}')

                elif days_name.get(d.weekday()) == days_name[4]:
                    print(f'{days_name.get(d.weekday())} - {name}')

                else:
                    print(f'Понеділок - {name}')
    
    
if __name__ == '__main__':

    get_birthday_per_week(users)

