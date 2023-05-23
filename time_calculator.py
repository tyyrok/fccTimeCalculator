

def add_time(start, duration, startDay = False):

    def changeDay(startDay, numberOfDays = 0):
        weekDays = ['monday', 'tuesday', 'wednesday', 'thuesday', 'friday', 'saturday', 'sunday']

        if startDay == False:
            return ''
        else:
            for i in range(len(weekDays)):

                if startDay.lower() == weekDays[i]:

                    if numberOfDays == 0:
                        return ', ' + weekDays[i].capitalize()
                    else:
                        return ', ' + weekDays[((int(numberOfDays) + i) % 7)].capitalize()
                    
    
    amPm = str(start).split()[1]
    currentTimeHour = str(start).split()[0].split(':')[0]
    currentTimeMin = str(start).split()[0].split(':')[1]
    currentTime = int(currentTimeHour) * 60 + int(currentTimeMin) if amPm == 'AM' else int(currentTimeHour) * 60 + int(currentTimeMin) + 720
    durationHour = str(duration).split(':')[0]
    durationMin = str(duration).split(':')[1]
    durationTime = int(durationHour) *60 + int(durationMin)
    newTimeWhole = currentTime + durationTime

    if newTimeWhole >= 1440 :

        numberOfDays = (newTimeWhole - newTimeWhole % 1440) / 1440
        newTimeWhole = newTimeWhole % 1440

        if newTimeWhole >= 720:
            
            newTimeWhole -= 720

            newTimeHour = str(int((newTimeWhole - newTimeWhole % 60) / 60))
            newTimeHour = newTimeHour + ':' if int(newTimeHour) != 0 else '12:'
            newTimeMin = str(newTimeWhole % 60)
            amPm = 'PM'

        else:
            newTimeHour = str(int((newTimeWhole - newTimeWhole % 60) / 60))
            newTimeHour = newTimeHour + ':' if int(newTimeHour) != 0 else '12:'
            newTimeMin = str(newTimeWhole % 60)
            amPm = 'AM'

        if len(str(newTimeMin)) == 1:
            newTimeMin = '0' + newTimeMin  + ' ' + amPm 
        else:
            newTimeMin += ' ' + amPm

        new_time = newTimeHour + newTimeMin + changeDay(startDay, numberOfDays) +  ' ' + '('
        if int(numberOfDays) == 1:
            new_time += 'next day)'
        else:
            new_time += str(int(numberOfDays)) + ' days later)'

    else:
        if newTimeWhole >= 720:

            newTimeWhole -= 720
            newTimeHour = str(int((newTimeWhole - newTimeWhole % 60) / 60))
            newTimeHour = newTimeHour + ':' if int(newTimeHour) != 0 else '12:'
            newTimeMin =  str(newTimeWhole % 60) 
            amPm = 'PM'
            
        else:
            newTimeHour = str(int((newTimeWhole - newTimeWhole % 60) / 60))
            newTimeHour = newTimeHour + ':' if int(newTimeHour) != 0 else '12:'
            newTimeMin = str(newTimeWhole % 60) 
            amPm = 'AM'

        if len(str(newTimeMin)) == 1:
            newTimeMin = '0' + newTimeMin + ' ' + amPm

        else:
            newTimeMin += ' ' + amPm

        new_time = newTimeHour + newTimeMin + changeDay(startDay)

    return new_time

#print(add_time("2:59 AM", "24:00", "saturDay"))
#add_time("3:30 PM", "2:12", "Monday")
#print(add_time("3:03 AM", "2:02"))
