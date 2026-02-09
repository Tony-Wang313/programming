
def check_day(day_number):
    if 0>=day_number or 7<day_number:
         return "Not a proper day number"
    elif 1<= day_number <=5:
        return "It is workday!"
    else:
        return "It is weekend!" 
  

def identify_day(day_number):
    if   1==day_number:
        return "It is monday!"
    elif 2==day_number:
        return "It is tuesday!"
    elif 3==day_number:
        return "It is wednesday!"
    elif 4==day_number :
        return "It is thursday!"
    elif 5==day_number :
        return "It is friday!"
    elif 6==day_number :
        return "It is saturday!"
    elif 7==day_number :
        return "It is sunday!"
    else:
        return "Not a proper day number"

if __name__ == '__main__':
    day_number=int(input("Enter the day number: "))
    print(check_day(day_number))
    print(identify_day(day_number))