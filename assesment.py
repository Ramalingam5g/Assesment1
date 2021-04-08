import time
start=5
end=0
vehicle_in_list=[]
vehicle_list=[]
class Parkingslot:
    def __init__(self,two_wheeler,three_wheeler,four_wheeler,others_vehicle):
        self.two_space=two_wheeler
        self.three_space=three_wheeler
        self.four_space=four_wheeler
        self.others=others_vehicle

    def parking_floors(self,fourth,three,second,first):
        self.fourth_floor=fourth
        self.third_floor=three
        self.second_floor=second
        self.first_floor=first
        print("****************WELCOME TO PARKING***********************")        
    def user_options(self):
        option=int(input("""YOU HAVE
            1,TWO WHEELER
            2,THREE WHEELER
            3,FOUR WHEELER
            4,OTHERS
            PLEASE ENTER:"""
        ))
        vehicle_in=input("ENTER VEHICLE NUMBER:")
        vehicle_in_list.append(vehicle_in)  
        print("VEHICLE IN LIST:",vehicle_in_list)
        
        if option==1:
            print(" OCCUPIED SPACE IN PARKINGSLOT:",self.fourth_floor)
            for i in range(1,self.fourth_floor):
                print("EMPTY SPACE IN PARKINGSLOT:",i)
            vehicle_list.append(self.two_space)
            time.sleep(2)
            print("vehicle list::",vehicle_list)
            time.sleep(2)
            return self.user_options()
            
        elif option==2:
            calc_space=self.fourth_floor-option+1
            print(" OCCUPIED SPACE IN PARKINSLOT:",self.fourth_floor,"to",calc_space)
            for i in range(1,calc_space):
                print("EMPTY SPACE IN PARKINGSLOT:",i)
            vehicle_list.append(self.three_space)
            time.sleep(2)
            print("vehicle list:",vehicle_list)
            time.sleep(2)
            return self.user_options()
        elif option==3:
            calc_space=self.fourth_floor-option+1
            print("OCCUPIED SPACE IN PARKINGSLOT:",self.fourth_floor,"to",calc_space)
            for i in range(1,calc_space):
                print("REMAING SPACE IN PARKING SLOT:",i)
            vehicle_list.append(self.four_space)
            time.sleep(2)
            print("vehicle list:",vehicle_list)
            time.sleep(2)
            return self.user_options()
        elif option==4:
            calc_space=self.fourth_floor-option+1
            print("OCCUPIED SPACE IN PARKINGSLOT:",self.fourth_floor,"to",calc_space)
            for i in range(1,calc_space):
                print("REMAING SPACE IN PARKING SLOT:",i)
            vehicle_list.append(self.others)
            time.sleep(2) 
            print(vehicle_list)
            time.sleep(2) 
            return self.user_options()
    def vehicle_remove(self):
        vehicle_out=input("WANT TO REMOVE YOUR VEHICLE:")
        if vehicle_out=="yes "or "YES":
            vehicle_number=input("ENTER VEHICLE NUMBER TO REMOVE:")
            vehicle_in_list.remove(vehicle_number)
            print("...VEHICLE REMOVED SUCESSFULLY...")
            time.sleep(2)
            print("VEHICLE IN SLOT",vehicle_in_list)
            return.self.user_options()
        else:
            return self.user_options()
            
car=Parkingslot("two_wheeler","three_wheeler","four_wheeler","others_vehicle")
car.parking_floors(5,5,5,5)
car.user_options()
car.vehicle_remove()

    




    



        