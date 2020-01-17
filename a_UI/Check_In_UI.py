from b_Application.Reservation_Processor import _Reservation

class _CheckInUI:
    def __init__(self, reservationNum):
        self.reservationNum = reservationNum

    def Check_reservation_validity():
        if _Reservation.Match_Number_In_List(reservationNum):
            self.Show_Success_Message()
        else:
            self.Show_Warning

    def Show_Warning():
        print("Invalid reservation number!")

    def Show_Success_Message():
        print("Success!")