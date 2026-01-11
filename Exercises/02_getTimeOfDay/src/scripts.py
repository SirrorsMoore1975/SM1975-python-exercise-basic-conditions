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

def getTimeOfDay(hrs: int, mins: int, meridiem: str) -> str:
    """
    Return the time of day morning / afternoon / evening / night for the given hours, minutes and meridiem
    
    Args
        hrs (int): hours of the day
        mins (int): minutes of the day
        meridiem (str): meridiem of the day
    
    Returns:
        result (str): time of day
    """
    # Solution 1
    # checkMeridiem = False
    # if (meridiem == "AM" or meridiem == "PM"):
    #     checkMeridiem = True
    # if hrs <= 0 or hrs > 12 or mins < 0 or mins >= 60 or not checkMeridiem:
    #     return "invalid input"
    # # The code will be cleaner if we use 24hrs for each day
    # if meridiem == "PM" and hrs != 12:
    #     hrs += 12
    # if meridiem == "AM" and hrs == 12:
    #     hrs = 24
    # #print(hrs, meridiem)
    # if hrs < 4:
    #     return "night"
    # elif hrs >= 4 and hrs < 12:
    #     return "morning"
    # elif hrs >= 12 and hrs < 17:
    #     return "afternoon"
    # elif hrs >= 17 and hrs < 20:
    #     return "evening"
    # elif hrs == 20:
    #     if mins < 30:
    #         return "evening"
    #     elif mins >= 30:
    #         return "night"
    # elif hrs >= 21 and hrs <= 24:
    #     return "night"

    # Solution 2
    check_meridiem = meridiem in ('AM', 'PM')
    check_hours = 0 < hrs <= 12
    check_minutes = 0 <= mins < 60
    if not check_meridiem or not check_hours or not check_minutes:
        return "invalid input"
    if meridiem == "AM":
        if hrs == 12:
            hrs = 24
    if meridiem == "PM":
        if hrs != 12:
            hrs += 12
    if 21 <= hrs <= 24:
        return "night"
    if 4 <= hrs < 12:
        return "morning"
    if 12 <= hrs < 17:
        return "afternoon"
    if 17 <= hrs < 19:
        return "evening"
    if hrs == 20:
        if mins < 30:
            return "evening"
        return "night"
    if hrs < 4 :
        return "night"
