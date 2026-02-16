#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp_str = int(temp_str)
        if temp_str > 40:
            print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        elif temp_str < 0:
            print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp_str}°C is perfect for plants!")
    except:
        print(f"Error: '{temp_str}' is not a valid number")
    


print("=== Garden Temperature Checker ===\n")

print("Testing temperature: 25")
check_temperature(25)
print("\n")
print("Testing temperature: abc")
check_temperature("abc")
print("\n")
print("Testing temperature: 100")
check_temperature(100)
print("\n")
print("Testing temperature: -50")
check_temperature(-50)
print("\n")

print("All tests completed - program didn't crash!")