# Problem 2.1:
zero_to_twenty = []
for i in range(0, 21):
    zero_to_twenty.append(i)
print(zero_to_twenty)

# Problem 2.2:
def squareList(sl):
    sqlist = []
    for i in sl:
        i = i**2
        sqlist.append(i)    # Accidentally appended i to the zero_to_twenty list
    
    return sqlist   # Earlier, the terminal printed "None", because I forgot to add this line.

squared_list = squareList(zero_to_twenty)
print(squared_list)

# Problem 2.3:
def first_fifteen_elements(ff):
    if(len(ff) >= 15):
        print(ff[0:15])     # Slicing
        # I forgot that the index starts from and includes the 0 index, so I printed the first 16 elements instead.    
    else:
        print("List doesn't contain at least 15 elements.")
    
first_fifteen_elements(squared_list)

# Problem 2.4:
def every_fifth_element(fe):
    print(fe[4::5])     # Striding
    # Initially wrote fe[::5], but it printed the first element as well.

every_fifth_element(squared_list)

# Problem 2.5:
def fancyFunction(reverse):
    n = len(reverse) - 1
    print(reverse[n:0:-3])  # First try!

fancyFunction(squared_list)

# Problem 3.1:
def create_2D_list():
    mt_5x5 = []
    n = 1
    for i in range(5):
        row = []    # this list resets to an empty list after every iteration of i.
        for j in range(5):
            row.append(n)
            n += 1
        mt_5x5.append(row)
    
    return mt_5x5

matrix = create_2D_list()
print(matrix)

# Problem 3.2:
def modified_2D_list(mult_of_three):
    mt = []
    for i in mult_of_three:
        for j in i:
            if(j % 3 == 0):
                index = i.index(j)
                i[index] = '?'
        mt.append(i)
        
    return mt 

print(modified_2D_list(matrix))

# Problem 3.3:
new_matrix = modified_2D_list(matrix)
def sum_non_question_elements(nqe):
    sum_matrix = 0
    for i in nqe:
         for j in i:
             if(j != '?'):
                 sum_matrix += int(j)
    
    print(sum_matrix)

sum_non_question_elements(new_matrix)

