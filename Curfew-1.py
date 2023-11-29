def curfew (District, age):
    if age <18 or age >60:
        if District in [1, 3, 5]:
            return "Monday, Thursday, and Fridays is 10:00pm - 4:00am"
        elif District in [2, 4, 6]:
            return "Wednesday, Saturday, and Mondays is 10:00pm - 4:00am"
        elif District in [7, 8, 9]:
            return "Tuesday, Friday, and Saturday is 10:00pm - 4:00am"
    else: 
        if District in [1, 3, 5]:
            return "Monday and Thursday is 10:00pm - 4:00pm"
        elif District in [2, 4, 6]:
            return "Wednesday and Saturday is 10:00pm - 4:00am"
        elif District in [7, 8, 9]:
            return "Tuesday and Friday is 10:00pm - 4:00am"
    return "Sunday is 11:00pm - 3:00am"
def main():
    user_name = (input("Enter your name: "))
    age = int(input("Enter your age: "))
    District = int(input("Enter your district number: "))

    if District in [1, 3, 5]:   
        Color = "Blue"
    elif District in [2, 4, 6]:
        Color = "Red"
    elif District [7, 8, 9]:
        Color = "Green"
    else:
        Color = "Unknown"
    
    curfew_sched = curfew(District, age)
    
    print("User Information: ")
    print("Name: {}".format(user_name))
    print("District Color: {}".format(Color))
    print("Curfew Schedule: {}".format(curfew_sched))
    
if __name__ == "__main__":
    main()