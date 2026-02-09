# Part 1
def calculate_height (h0, t):
    g=9.8
    height=h0-0.5*g*t**2
    return round(height, 1)

#Part 2
def car_distance (t):
    speed=20
    distance=speed*t
    return round(distance, 2)

if __name__ == '__main__':
 t=float(input("Enter the amount of time the car travelled (in seconds): "))
 final_distance=(car_distance(t))
 print(f"Your car travelled for {final_distance} meters")
 h0=float(input("Enter your h0 value in meters: "))
 t=float(input("Enter the time in second: "))
 final_value=(calculate_height(h0, t))
 print(f"Height of the ball at {t} seconds is {final_value}")

def check_weekday_or_weekend(day_number):
    if day_number < 1 or day_number > 7:
        return "Not a proper day number!"
    
    if 1 <= day_number <= 5:
        return "It is a Weekday!"
    else:
        return "It is a Weekend!"