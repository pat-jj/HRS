from c_Domain.Room import _Room
from ReservationList_processor import _ReservationListProcessor
from Reservation_Processor import _ReservationProcessor
from a_UI.Room_Search_UI import _RoomSearchUI
import json

class _RoomProcessor:
    def Get_roomlist_from_json():
        roomList = []
        #parse room.json as a list of room object                    
        return roomList
        pass

    def get_date_from_RoomSearchUI():
        self.check_in_date = _RoomSearchUI.check_in_date
        self.check_out_date =  _RoomSearchUI.check_out_date



    def Get_Number_of_Available_Room_On_Given_date(date):
        ReservationOnThatDay = 0
        list = []
        #Parse corresponding json file as list of reservation object
        for item in list:
            if item.check_in_date == date:
                ReservationOnThatDay += 1
        
        return _Room.total_num_of_room() - ReservationOnThatDay


    def Flip_Status(room_num):
        room_list = Get_roomlist_from_json()
        ThisReservation = _ReservationProcessor.ReturnReservationByRoomNumber(a_room.RoomNum)
        for a_room in room_list:
            if a_room.RoomNum == room_num:
                if a_room.Status == False:
                    a_room.Status = True
                    _ReservationProcessor.write_room_num(ThisReservation, room_num)
                    _ReservationProcessor.write_check_in_time(ThisReservations)
                    #write roomnum into reservation class 
                    # as the staff select a room for the user
                    _RoomManagementUI.Show_Success_Message()
                else:
                    a_room.Status = False
                    _ReservationProcessor.write_check_out_time(ThisReservation)
                    #write checkout time into reservation object 
                    #when a room status is switch from occupied to vacant
                    _RoomManagementUI.Show_Success_Message()


                a_room.update_status
                break
        pass
