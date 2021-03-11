def add_time(*args):

    start = args[0].split()
    time = start[0].split(':')

    hours = int(time[0])
    minutes = int(time[1])
    ampm = start[1]

    if ampm == 'PM' and hours != 12: hours+=12
    elif ampm == 'AM' and hours == 12: hours-=12

    duration = args[1].split(':')
    durationHours = int(duration[0])
    durationMinutes = int(duration[1])

    (totalHours, totalMinutes, ampm, dayCount) = calculateTime(hours, minutes, ampm, durationHours, durationMinutes)

    newTime = str(totalHours) + ':' + str(totalMinutes) + ' ' + ampm

    try: startDay = args[2]
    except: startDay = None

    newTime = formatTime(newTime, startDay, dayCount)

    return newTime


def calculateTime(hours, minutes, ampm, durationHours, durationMinutes):
    totalHours = hours + durationHours
    totalMinutes = minutes + durationMinutes
    dayCount = 0

    while totalMinutes >= 60:
        totalMinutes-=60
        totalHours+=1

    if totalMinutes < 10: totalMinutes = '0' + str(totalMinutes)

    if totalHours % 24 >= 12: ampm = 'PM'
    else: ampm = 'AM'

    while totalHours >= 24:
        totalHours-=24
        dayCount+=1

    if ampm == 'PM' and totalHours != 12: totalHours-=12
    if ampm == 'AM' and totalHours == 0: totalHours+=12

    return totalHours, totalMinutes, ampm, dayCount


def formatTime(newTime, startDay, dayCount):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    endDay = ''

    if startDay is not None:
        for i in range(len(days)):
             if days[i].lower() == startDay.lower():
                 newI = i + dayCount
                 while newI >= 7: newI-=7
                 endDay = days[newI]

    if endDay == '':
        if dayCount == 0: newTime = newTime
        if dayCount == 1: newTime = newTime + ' (next day)'
        if dayCount > 1: newTime = newTime + f' ({dayCount} days later)'

    if endDay != '':
        if dayCount == 0: newTime = newTime + f', {endDay}'
        if dayCount == 1: newTime = newTime + f', {endDay} (next day)'
        if dayCount > 1: newTime = newTime + f', {endDay} ({dayCount} days later)'

    return newTime