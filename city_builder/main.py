from city.city import City
from city.building import *

def main():
    city = City()
    print("Üdvözöllek a városépítő játékban!")
    
    while True:
        command: str = input(f"Mit szeretnél építeni:\n")
        
        if command == "ház":
            city.add_building(House())
            print("Ház épült")
            
        elif command == "farm":
            city.add_building(Farm())
            print("Farm épült")
        elif command == "favágó":
            city.add_building(Forest())
            print("Favágó épült")
        elif command == "malom":
            city.add_building(Mill())
            print("Malom épült")
        
        elif command == "pékség":
            city.add_building(Bakery())
            print("Pékség épült")
            
        elif command == "bánya":
            city.add_building(Mine())
            print("Bánya épült")
            
        elif command == "vadász":
            city.add_building(Hut())
            print("Vadászház épült")
            
        elif command == "kilép":
            break
        else:
            print("Ismeretlen parancs")

if "__name__" == "__main__":
    main() 
    