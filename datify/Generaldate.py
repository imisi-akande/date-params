import datetime
import dateparser

class Datify:
    """General date class for date watch"""
    def __init__(self):
        pass

    def calculate_years(self, date_one, date_two=None):
        """ Args:
            date_one(string)
            date_two(string)

        Attributes:
            date_one(string) representing the first input date
            date_two(string) representing the second input date
        """
        self.date_one = dateparser.parse(date_one)
        self.date_two = dateparser.parse(date_two) if date_two else None

        if self.date_one and self.date_two:
            dates = [self.date_one, self.date_two]
            self.date_one = max(dates)
            self.date_two = min(dates)
            new_date = round(abs((self.date_one - self.date_two).days/365.25))
        elif self.date_one and not date_two:
            current_date = datetime.datetime.now()
            new_date = round(abs((current_date - self.date_one).days/365.25))
        else:
            raise ValueError("Incorrect input date type")

        return new_date