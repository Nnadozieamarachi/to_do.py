# prompt user for weight and mass

weight = input("weight: ")
mass = input("(k)g or (L)bs: ")

# get result of weight in pounds or kilograms

if mass.upper() == "L":
    result = int(weight) / 2.205
    result = round(result, 1)
    print("weight in kg is ", (result))
elif mass.upper() == "K":
    result = (int(weight)) * 2.205
    result = round(result, 1)
    print("weight in pounds is ",  (result))