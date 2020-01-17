from b_Application.Room_Processor import _RoomProcessor
from c_Domain.Room import _Room

class _RoomSearchUI:
    def __init__(self, check_in_date, check_out_date):
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def Show_Available_Room_On_Given_day(check_in_date):
        if Get_Number_of_Available_Room_On_Given_date() > 0:
            print('There are ',Get_Number_of_Available_Room_On_Given_date(),' rooms avaible on this day.')
        else:
            No_Room_Notification()

    def No_Room_Notification():
        print('Sorry, we are sold out on this day.')
    





    