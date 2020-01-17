from b_Application.Room_Processor import _RoomProcessor


class _RoomManagementUI:

    # __init__ == select_Room
    def __init__(self, room_num):
        self.room_num = room_num
        pass
    
    def Change_Room_Status(room_num):
        _RoomProcessor.Flip_Status(room_num)
        pass

    def Show_Success_Message():
        print("Success!")