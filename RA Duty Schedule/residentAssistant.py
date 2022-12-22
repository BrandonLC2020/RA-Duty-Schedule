import calendar
from datetime import date, datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# Index using weekday int value
days[date.weekday()]

class RA:
    def __init__(self, name, dayOfWeekdayDuty):
        self.name = name
        self.totalDuty = 0
        self.weekdayDutyDay = dayOfWeekdayDuty

        self.totalWeekdayDuty = 0
        self.totalWeekdayPrimaryDuty = 0
        self.totalWeekdaySecondaryDuty = 0

        self.totalWeekendNightDuty = 0
        self.totalWeekendNightPrimaryDuty = 0
        self.totalWeekendNightSecondaryDuty = 0

        self.totalWeekendDayDuty = 0
        self.totalWeekendDayPrimaryDuty = 0
        self.totalWeekendDaySecondaryDuty = 0

    def getName(self):
        return self.name

    def getTotalDuty(self):
        return self.totalDuty

    def getWeekdayDutyDay(self):
        return self.weekdayDutyDay

    def getTotalWeekdayDuty(self):
        return self.totalWeekdayDuty

    def getTotalWeekdayPrimaryDuty(self):
        return self.totalWeekdayPrimaryDuty

    def getTotalWeekdaySecondaryDuty(self):
        return self.totalWeekdaySecondaryDuty

    def getTotalWeekendNightDuty(self):
        return self.totalWeekendNightDuty

    def getTotalWeekendNightPrimaryDuty(self):
        return self.totalWeekendNightPrimaryDuty

    def getTotalWeekendNightSecondaryDuty(self):
        return self.totalWeekendNightSecondaryDuty

    def getTotalWeekendDayDuty(self):
        return self.totalWeekendDayDuty

    def getTotalWeekendDayPrimaryDuty(self):
        return self.totalWeekendDayPrimaryDuty

    def getTotalWeekendDaySecondaryDuty(self):
        return self.totalWeekendDaySecondaryDuty