import json
from datetime import datetime


class _Reservation:
    def get_reservation_list():
        list = []
        #obtain list of all reservation in the corresponding json file
        return list

    def __init__(self, name, check_in_date, check_out_date):
        self.reservationNum = datetime.now.strftime("%H%M%S")
        #generate reservation num using current date
        self.check_in_date =  check_in_date
        self.check_out_date = check_out_date
        self.name = name

    def export_to_json():

    def write_room_num(roomNum):
        self.roomNum = roomNum

    def write_check_in_time(time):
        self.checkintime = time

    def write_check_out_time(time):
        self.checkouttime = time
