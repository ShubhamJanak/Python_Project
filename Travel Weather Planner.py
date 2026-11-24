distance_mi = float(input("Enter the distance in miles: "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
has_bike = input("Do you have a bike? (yes/no): ").lower() == "yes"
has_car = input("Do you have a car? (yes/no): ").lower() == "yes"
has_ride_share_app = input("Do you have a ride-share app? (yes/no): ").lower() == "yes"5

if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)