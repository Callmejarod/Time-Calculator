#Time Calculator

def add_time(start, duration, day=''):

    


    start_list = start.split(":")
    start_list += start_list[1].split(" ")
    start_list.pop(1)
    print(start_list)



    duration_list = duration.split(":")
    print(duration_list)

    initial_hour = int(start_list[0]) + int(duration_list[0])
    new_hour = int(start_list[0]) + int(duration_list[0])
    new_minutes = int(start_list[1]) + int(duration_list[1]) 
    initial_am_pm = str(start_list[2])
    new_pm_am = str(start_list[2])
  
    if new_hour >= 12:
        if new_pm_am == 'PM':
            new_pm_am = 'AM'
            print(new_pm_am)
        else:
            new_pm_am = 'PM'
            print(new_pm_am)

    if new_hour > 12:
        new_hour -= 12

    if new_minutes > 59:
        new_hour += 1
        new_minutes -= 60
    
    if new_minutes < 10:
            new_minutes = str(new_minutes).rjust(2, "0")







    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    if day.lower() in days_of_the_week:
        if initial_hour >= 12 and initial_am_pm == 'PM':
            index = (days_of_the_week.index(day.lower()) + 1)
            day = days_of_the_week[index]


              
                 
                
        



    new_time = (f'{new_hour}:{new_minutes} {new_pm_am} {day.capitalize()}')


    return new_time

print(add_time('11:43 PM', '3:00', 'tueSday'))


#FIX: Changes throughout the days of the week 


