#!/usr/bin/env python3

def water_plants(plant_list: list[:str]):
    try:
        print("Opening watering system")
        for plant in plant_list:
            print(f"Watering {plant}")
    except Exception as e:
        print(e)
        #print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)\n")
plant=[99,
       43]
water_plants(plant)