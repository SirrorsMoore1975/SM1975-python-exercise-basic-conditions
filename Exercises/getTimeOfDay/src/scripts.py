"""
04:00 AM (inclusive) - 12:00 PM (exclusive): morning\n
12:00 PM (inclusive) - 05:00 PM (exclusive): afternoon\n
05:00 PM (inclusive) - 08:30 PM (exclusive): evening\n
08:30 PM (inclusive) - 04:00 AM (exclusive): night\n

AM = Ante meridiem (Before noon)\n
PM = Post meridiem (After noon) \n

\t@param {1|2|3|4|5|6|7|8|9|10|11|12} ??? - the hour (12-hour style)\n
\t@param {number} ??? - the number of minutes past the hour\n
\t@param {"AM"|"PM"} ??? - "AM" or "PM"\n
\t@returns {"morning"|"afternoon"|"evening"|"night"} the rough "time of day"\n

"""

def getTimeOfDay(hrs:int,mins:int,meridiem:str) -> str:
    checkMeridiem = False
    if (meridiem == "AM" or meridiem == "PM"):
        checkMeridiem = True
    if hrs <= 0 or hrs > 12 or mins < 0 or mins >= 60 or not checkMeridiem:
        return "invalid input"
    # The code will be cleaner if we use 24hrs for each day
    if meridiem == "PM" and hrs != 12: 
        hrs += 12 
    if meridiem == "AM" and hrs == 12:
        hrs = 24
    #print(hrs, meridiem)
    if hrs < 4:
        return "night"
    elif hrs >= 4 and hrs < 12:
        return "morning"
    elif hrs >= 12 and hrs < 17:
        return "afternoon"
    elif hrs >= 17 and hrs < 20:
        return "evening"
    elif hrs == 20:
        if mins < 30:
            return "evening"
        elif mins >= 30:
            return "night"
    elif hrs >= 21 and hrs <= 24:
        return "night"