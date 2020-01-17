from b_Application.Reservation_Processor import _ReservationProcessor

class _ReservationUI:
    def __init__(self, name):
        self.name = name 
    
    def display_Reservation_Num():
        print(self.Register_Reservation())

    def Register_Reservation():
        res_process = _ReservationProcessor(name)
        res = res_process.make_reservation()
        return res.reservationNum


