# and, or, not

is_raining = True
is_windy = False

stay_inside = is_raining and is_windy

print("stay inside :"+ str(stay_inside))

take_coat = is_raining or is_windy

print("take coat :"+ str(take_coat))

print("is windy :" + str(not is_windy))

take_umbrella = is_raining and not is_windy
print("take umbrella :" + str(take_umbrella))

