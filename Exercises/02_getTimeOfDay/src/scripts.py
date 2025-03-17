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

def getTimeOfDay():
    pass