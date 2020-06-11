import datetime

class Datify:
    """General date class for date watch"""
    def __init__(self):
        pass

    def calculate_age(self, year, month, day):
        """ Args:
            year(int)
            month(int)
            day(int)

        Attributes:
            year(int) representing the year section of an input date
            month(int) representing the month section of an input date
            day(int) representing the day section of an input date
        """

        if all(isinstance(i, int) for i in [year, month, day]):
            self.year = int(year)
            self.month = int(month)
            self.day = int(day)
            current_date = datetime.datetime.now()
            input_date = datetime.datetime(self.year, self.month, self.day)
            new_date = round((abs(current_date - input_date).days/365.25))
            return new_date
        else:
            raise ValueError("Incorrect input date type")
