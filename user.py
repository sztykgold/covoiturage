from calendar import FRIDAY, MONDAY, THURSDAY, TUESDAY, WEDNESDAY
from email import message_from_binary_file
import flask_login
import enum

class WorkingHour(enum.Enum):
    NONE = -1
    M1 = 0
    M2 = 1
    M3 = 2
    M4 = 3
    S1 = 4
    S2 = 5
    S3 = 6

class WorkingDay(enum.Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4

class WorkingWeek():
    _data = {
        WorkingDay.MONDAY.name : [ WorkingHour.NONE, WorkingHour.NONE],
        WorkingDay.TUESDAY.name : [ WorkingHour.NONE, WorkingHour.NONE],
        WorkingDay.WEDNESDAY.name : [ WorkingHour.NONE, WorkingHour.NONE],
        WorkingDay.THURSDAY.name : [ WorkingHour.NONE, WorkingHour.NONE],
        WorkingDay.FRIDAY.name : [ WorkingHour.NONE, WorkingHour.NONE],
    }

class BerthelotUser(flask_login.UserMixin):
    def __init__(self, user_email = "undefined", password="undefined", phone = "9876543210", city = "unknown city", zipcode = 54321) -> None:
        super().__init__()
        self.id = user_email
        self.user_email = user_email
        self.password = password
        self.phone = phone
        self.city = city
        self.zipcode = zipcode
        self.AWeek = WorkingWeek
        self.BWeek = WorkingWeek

