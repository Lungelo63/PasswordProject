#assigning 0 to a variable
all_boolean = 0

#if user enters yes program will change variable to True
# and plus 1 to all_boolean 
have_length = False
have_length_input = input('Have length: yes or no: ')
if have_length_input == "yes":
    have_length = True
    all_boolean += 1

#if user enters yes program will change variable to True
# and plus 1 to all_boolean 
up_case = False
up_case_input = input("Have up case: yes or no: ")
if up_case_input == "yes":
    up_case = True
    all_boolean += 1

#if user enters yes program will change variable to True
# and plus 1 to all_boolean 
low_case = False
low_case_input = input("Have low case: yes or no: ")
if low_case_input == "yes":
    low_case = True
    all_boolean += 1

#if user enters yes program will change variable to True
# and plus 1 to all_boolean 
have_num = False
have_num_input = input("Have numbers: yes or no: ")
if have_num_input == "yes":
    have_num = True
    all_boolean += 1

#checks if at least 3 characteristics are met
#if so...
if all_boolean >= 3:
    print("This is a suitable password")
else:
    print("This is not a suitable password")