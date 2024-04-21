#Time Calculator

def add_time(start, duration, day=''):

    days_of_the_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


    start_list = start.split(":")
    start_list += start_list[1].split(" ")
    start_list.pop(1)
    print(start_list)



    duration_list = duration.split(":")
    print(duration_list)


    new_hour = int(start_list[0]) + int(duration_list[0])
    new_minutes = int(start_list[1]) + int(duration_list[1]) 
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



    new_time = (f'{new_hour}:{new_minutes} {new_pm_am} {day}')


    return new_time

print(add_time('10:00 PM', '12:05','tuesday'))


#FIX: Changes throughout the days of the week 
#FIX: Single minutes digits error 

