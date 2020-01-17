from a_UI.Room_Search_UI import _RoomSearchUI
from a_UI.Reservation_UI import _ReservationUI
from b_Application.Room_Processor import _RoomProcessor
from c_Domain import _Reservation
from ReservationList_processor import _ReservationListProcessor

class _ReservationProcessor:
    def __init__(self, name):
        self.name = name

    def make_reservation():
        check_in_date, check_out_date = _RoomProcessor.check_in_date, _RoomProcessor.check_out_date
        newRes = _Reservation(self.name, check_in_date, check_out_date)
        newRes.export_to_json()
        return newRes

#used in Check_In_UI
    def Match_Number_In_List(reservationNum):
        ResNumList = _ReservationListProcessor.get_reservation_number_list()
        if reservationNum in ResNumList:
            return True
        else:
            return False


#Triggered by check in UI
    def write_room_num(Reservation,roomNum):
        Reservation.write_room_num(roomNum)


#Triggered by check in UI
    def write_check_in_time(Reservation):
        time = datetime.now.strftime("%H%M%S")
        Reservation.write_check_in_time(time)

#Triggered by room management UI when the status is flipped from occupied to vacant
    def write_check_out_time(Reservation):
        time = datetime.now.strftime("%H%M%S")
        Reservation.write_check_out_time(time)

    def ReturnReservationByRoomNumber(roomNum):
        ReservationList = _Reservation.get_reservation_number_list()
        for item in ReservationList:
            if item.roomNum == roomNum
                return item
