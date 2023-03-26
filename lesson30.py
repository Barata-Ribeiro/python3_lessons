"""
CONSTANT = "Variables" that will not change
Too many conditions in the same 'if' (bad)
     <- Complexity count (bad)
"""
speed = 80  # current car speed
car_location = 100  # where the car is on the road

# These are variables that will not change
# their values no matter what. Even though Python
# doesn't have a constant variable; it is only good practice.
RADAR_1 = 60  # maximum speed of radar_1
PLACE_1 = 100  # location where radar_1 is
RADAR_RANGE = 1  # The distance where the radar picks up

# Python allows the use of backslashes to
# continue the code underneath...
vehicle_too_fast = speed > RADAR_1
vehicle_passed_through_radar = car_location >= (PLACE_1 - RADAR_RANGE) and \
    car_location <= (PLACE_1 + RADAR_RANGE)
vehicle_is_finable = vehicle_passed_through_radar and vehicle_too_fast

if vehicle_too_fast:
    print('INFO: Speeding vehicle...')

if vehicle_passed_through_radar:
    print('A vehicle has passed through the radar.')

if vehicle_is_finable:
    print('WARNING! The vehicle was too fast \
and was fined by the radar!')
else:
    print('Have a safe trip!')
