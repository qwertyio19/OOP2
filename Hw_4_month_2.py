""" Домашнее задание """


class Vehicle:
    def move(self):
        return "Транспорное средство движется"
    
    def fuel(self):
        return "Тип топлива - Неизвестный тип топлива"
        
      
class Car:
    def move(self):
        return "Машина едет по дороге"
    
    def fuel(self):
        return "Тип топлива - Бензин"
    
    
class Bicycle:
    def move(self):
        return "Велосипед едет по велосипедной дорожке"
    
    def fuel(self):
        return "Тип топлива - Человек"
    
    
class Boat:
    def move(self):
        return "Лодка плывёт по воде"
    
    def fuel(self):
        return "Тип топлива - Дизель или электричество"
    
    
vehicles = [Vehicle(), Car(), Bicycle(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
    print(vehicle.fuel())