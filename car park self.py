from  time import *
class car_park():
    def __init__(self,capacity):
        self.capacity=capacity
        self.available_space=capacity
        self.cars=set()
    def available(self):
        return self.available_space
    def entry(self,car_no):
        if (self.available_space>0):
            self.cars.add(car_no)
            self.available_space -=1
            t=localtime()
            timee=strftime(" %H:%M:%S",t)
            print(f"the car is parked in {timee}")
            print(f"the car no {car_no} was successfully parked")
        else:
            print("the parking slot is full")
    def remove(self,car_no):
        sleep(3)
        if car_no in self.cars:
            self.cars.remove(car_no)
            self.available_space+=1
            t=localtime()
            timee=strftime(" %H:%M:%S",t)
            print(f"the car is leave the parking at {timee}")
            print(f"the car no {car_no} was successfully leave the parking")
        else :
            print("the card is not available in the parking ")
# hear cities are added 
city_space={"delhi":15,"indore":20,"mumbai":25,"pune":64,"khargone":50}
space=city_space.get(input("enter the place you are in -->> "))

s2=car_park(space)
for i in range(50):
    for_what= (input(" P for parking-- E for exit--A to cheak the avaiblity--Q for quite\n"))
    if (for_what.upper()=="P"):
        car_number=input("enter the car number ")
        s2.entry(car_number)
    elif(for_what.upper()=="E"):
        car_number=input("enter the car number ")
        s2.remove(car_number)
    elif(for_what.upper()=="A"):
        print(f"in the paring {s2.available()} slot are available")
    elif(for_what.upper()=="Q"):
        print("you successfully quite the parking ")
        break
    else:
        print("you enter wrong syntax")
