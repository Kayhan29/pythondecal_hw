# Problem 1:
def computePower(a,b):
    c = a
    for i in range(1,b):
        c *= a
    return c
x = 2
y = 3
print(computePower(x,y))

# Problem 2:
readings = [15, 14, 17, 20, 23, 28, 20]
def temperatureRange(list):
    min_temp = min(list)
    max_temp = max(list)
    return(min_temp, max_temp)
print(temperatureRange(readings))

# Problem 3:
def isWeekend(d):
    
    if d == 6 or d == 7:
        return True
    else:
        return False
day = int(input("Enter a number from 1-7: "))
print(isWeekend(day))

# Problem 4:
def fuelEfficiency(d, f):
    fuel_eff = float(d/f)
    return fuel_eff
distance = 70 # miles
fuel = 21.5 # gallons
print(fuelEfficiency(distance, fuel))

# Problem 5:
n = 12345
def decodeNumbers(num):
    mod_n = num % 10 # Extracts the last digit from the number
    num = num // 10 # Reduces the inputted number to the first four digits
    new_n = (mod_n * (10**4)) + num # Brings the last digit from the original number to the front of the number
    return new_n
print(decodeNumbers(n))

nums = [2024, 92, 293, 20, 190]
# Problem 6.1(For loops):
def find_Min_For(n):
    current_min_number = n[0]
    for i in n:
        if i < current_min_number:
            current_min_number = i 
        
    return(current_min_number)
def find_Max_For(n):
    current_max_number = n[0]
    for i in n:
        if i > current_max_number:
            current_max_number = i
        
    return current_max_number
print(find_Min_For(nums))
print(find_Max_For(nums))

# Problem 6.2(While loops):
def find_Min_While(n):
    i = 0
    current_min_num = n[0]
    while i < len(n):
        if n[i] < current_min_num:
            current_min_num = n[i]
        i += 1
    return current_min_num
def find_Max_While(n):
    i = 0
    current_max_num = n[0]
    while i < len(n):
        if n[i] > current_max_num:
            current_max_num = n[i]
        i += 1
    return current_max_num
print(find_Min_While(nums)) 
print(find_Max_While(nums))

# Problem 7:
text = "UC Berkeley, founded in 1868!"
def vowels_And_Consonants(string):
    v_count = 0
    c_count = 0
    vowels = set("aeiouAEIOU")
    for alphabet in string:
        if alphabet.isalpha():
            if alphabet in vowels:
                v_count += 1
            else:
                c_count += 1
    return(v_count, c_count)
print(vowels_And_Consonants(text))

# Problem 8:
num = 2468
def digital_Root(n):
    sum_of_digits = 0
    while n != 0:
        sum_of_digits += (n % 10)
        n = n // 10
    return(sum_of_digits)
print(digital_Root(num))


