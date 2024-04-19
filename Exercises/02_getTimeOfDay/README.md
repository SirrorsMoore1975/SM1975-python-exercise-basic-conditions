# getTimeOfDay
- [ ] Declare a function called getTimeOfDay
```py
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
```
Write tests for getTimeOfDay:-
```py
@pytest.mark.parametrize("hours,minutes,meridiem,expected",[
    (0,31,"AM","invalid input"),
    (3,29,"AM","night"),
    (3,59,"AM","night"),
    (4,0,"AM","morning"),
    (4,30,"AM","morning"),
    (11,59,"AM","morning"),
    (12,0,"PM","afternoon"),
    (4,59,"PM","afternoon"),
    (5,30,"PM","evening"),
    (8,29,"PM","evening"),
    (8,30,"PM","night"),
    (11,59,"PM","night"),
    (12,0,"AM","night"),
    (12,59,"AM","night")
])
```