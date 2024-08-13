# Iftikhar Mahmud, CSW8 (F21)

# Option 1

def list_categories(main_db, showID = False):
    if (len(main_db) == 0):
        print('There are no categories.') # The here we are checking the length of the main database
    elif (len(main_db) == 1):
        print('There is only 1 category:')
    else:
        print("There are {} categories:".format(len(main_db))) # I decided to create 2 different string formats to incorporate the ID part of dict
    for i, items in enumerate(main_db): 
        if (showID): # Here it would show the id
            print('{id} - {category} : {percentage}%'.format(id = items, category = main_db[items][0].upper(), percentage = main_db[items][1]))
        else:# Here it won't
            print('{category} : {percentage}%'.format(category = main_db[items][0].upper(), percentage = main_db[items][1]))
    return (len(main_db))

# Option 2

def add_category(db, cid, info_str):
    info = info_str.split() #Here we create a new category for the db
    if (len(info) != 2):
        return -2  # This if statement checks to see if there is not enough info
    elif (is_numeric(info[1]) != True): 
        return -1 # This function checks to see if the info is a percentage input is a float or int
    else:
        db[cid] = [info[0], (float(info[1]))] # This line implements the info to the dictionary

        return cid


def is_numeric(val):
        if val.isdigit() == True: #First we check to see if the string input is a integer
            return True
        elif '.' in val: # If it fails the first test then it check to see if its a float
            for char in val:
                if char.isdigit() == True or char == '.': # Checks to see if each character is a digit or a period
                    if '.' != val[-1:]: # Another check to see if the period is at the end
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False

def create_id(db, offset = 0):
    if len(db) == 0: # Check to see if the dictionary has any categories and creates an ID if it has none
        return offset
    else:
        dict_key_list = db.keys() # Make a list of keys to find the max value key
        max_key = int(max(dict_key_list))
        max_key += 1 + offset #  and increment from the max value obtained from max_key
        return max_key


def add_categories(db, max_num, id_offset):
    print("You can add up to {} categories".format(max_num)) # Made all the print statements and got all the information needed to add a new category
    print('::: How many categories will you add?')
    num_cat = ((input('> ')))
    if len(db) + int(num_cat) > max_num:  #Tests whether the desired number of categories the user wants to input is within max_num
        print('WARNING: Adding {} categories would exceed the allowable max.'.format(num_cat))
        print('You can store up to {} categories.'.format(max_num))
        print('Current total of categories is {}.'.format(len(db)))
    else:
        for i in range(int(num_cat)): # Loops over how many categories the user wanted to add
            print('::: Enter the category {} name (no spaces) followed by its percentage'.format(i + 1))
            new_offset = create_id(db, id_offset)
            id_offset = 0 # Sets the offset to 0 to reset the offset and increments the id by 1 instead of 101
            tester = add_category(db, new_offset, input('>'))
            while tester == -2 or tester == -1: # Uses a while loop to account for multiple entries 
                print('WARNING: invalid input for the name and percentage.')
                print('::: Enter the category {} name (no spaces) followed by its percentage'.format(i + 1))
                print('::: or enter M to return back to the menu.')
                string_input = input('>')
                if string_input == 'M': # If user enters M then it returns them to main menu
                    return
                else:
                    tester = add_category(db, new_offset, string_input)
                

# Option 3

def update_category(db): 
    print('Below is the info for the current categories.')
    list_categories(db, True) # shows all the categories but this time with ID
    print('::: Enter the category ID that you want to update')
    upd_id = int(input('> ')) # Uses an input to check if it exists in the dictionary and update it to new values
    if upd_id in db:
        print('Found a category with ID `{}`:'.format(upd_id))
        print('Enter the updated info:')
        new_info = input('> ')
        upd_tester = add_category(db, upd_id, new_info) #Using a variable to test cases where errors can result
        if upd_tester == -2:
            print('WARNING: insufficient information for the update.')
            print('Record with ID `{}` was not updated!'.format(upd_id))
        elif upd_tester == -1:
            print('WARNING: invalid input for the name and/or percentage.')
            print('Record with ID `{}` was not updated!'.format(upd_id))
        else:
            upd_tester # Updates the dictionary with new values
    else:
        print('WARNING: `{}` is not an ID of an existing category.'.format(upd_id))
        print('::: Enter the ID of the category you want to update')
        print('::: or enter M to return back to the menu.')

# Option 4
def delete_category(db):
    if (list_categories(db, True) == 0):
        pass
    else:
        print('::: Enter the category ID that you want to delete')
        del_id = int(input('> ')) # Again using input to track down the ID in the dictionary
        if del_id in db:
            print('Found a category with ID `{}`:'.format(del_id))
            print(db[del_id])
            print('::: Are you sure? Type Y or N')
            ans = input('> ')
            if ans == 'Y':
                del db[del_id] # This function is used to remove keys and items from the dictionary
            else:
                print("Looks like you aren't 100% sure.")
                print('Cancelling the deletion.')

# Option 5

def add_grades(db):
    print('Below is the info for the current categories.')
    if (list_categories(db, showID = True)) == 0:
        return
    else:
        print('::: Enter the category ID for which you want to add grades')
        grd_id = int(input('>')) # Tracks down what category we want to add grades to
        if grd_id in db:
            print('You selected a {} category.'.format(db[grd_id][0]))
            print('::: Enter space-separated grades')
            print('::: or enter M to return back to the menu.')
            grade_string = input('>')
            add_category_grades(db, grd_id, grade_string)

        else:
            print('`{}` is not an ID of an existing category.'.format(grd_id))
            print('::: Enter the ID of the category to add grades to')
            print('::: or enter M to return back to the menu.')

def add_category_grades(db, cid, grades_str):
    gsl = grades_str.split() # First split it to make a list of the string values
    grade_float = [] # Used a local variable to keep track of all the grades
    for index, grades in enumerate(gsl):
        if is_numeric(grades) == False: # If any value is not a numeric value
            return -1
        else:
            grade_float.append(float(grades)) # Adds the grades to the list initialize earlier in the def function
    if len(db[cid]) == 3: # Check to see if we already have an existing grade list for the category
        show_grades_category(db, cid)
        for index, values in db.items(): # we are assigning indices to the values in the dictionary for the given ID.
            for i in grade_float: # Looping over every value in grade float 
                values[2].append(i) # we are adding each value in grade float to the pre-existing list in the given ID
        show_grades_category(db, cid)
        print('Success! Grades for the {category} category were added.'.format(category = db[cid][0].upper()))
    
    else:
        db[cid] = [db[cid][0], db[cid][1], grade_float] # if there was no pre-existing grade list then we are creating one here and updating the dict to account for it
        print('Success! Grades for the {category} category were added.'.format(category = db[cid][0].upper()))
    return len(grade_float)

# Option 6

def show_grades(db):
    if (list_categories(db, True) == 0):
        return 
    else:
        print("::: Enter the category ID for which you want to see the grades")
        print("::: or enter A to list all of them.")
        user_input = input()

        if (user_input == 'A'): # Shows all the grades in the list
            for index, keys in db.items():
                show_grades_category(db, keys)
        else:
            while (user_input in db == False): # Used another while to try and get either an existing ID or return to the main menu 
                print("WARNING: `{}` is not an ID of an existing category.".format(user_input))
                print("::: Enter a valid category ID to see the grades")
                print("::: or enter M to return back to the menu.")
                user_input = input("> ")
                if (user_input == 'M'):
                    return
            show_grades_category(db, user_input)

def show_grades_category(db, cid):
    key_info = db[int(cid)] 
    if (len(key_info) != 3): # Checks if the given ID has a grade list 
        print("No grades were provided for category ID `{}`.".format(cid))
        return 0
    else:
        print(key_info[0].upper(), "grades", key_info[2]) # If it does then it prints the grades 
        return len(key_info[2])

# Option 7

def sum_percentages(db): 
    percentage_total = 0
    for index, items in db.items(): # Loop over every id in the dictionary and increment the total by the provided percentage in each ID
        percentage_total += items[1]
    return percentage_total

def get_avg_grade(grade_list):
    if len(grade_list) == 0: # returns 0 if there are no grades in the grade list
        return 0
    else:
        avg = sum(grade_list)/len(grade_list) # Formula to find the average of the list
    return avg

def grade_stats(db):
    if len(db) == 0:
        print('There are no categories.')
        return 0
    else:
        total = 0
        list_categories(db, showID = False)
        print()
        print('Provided grades')
        for index, items in db.items(): # test to see if ther is a grade list in the database
            if len(items) == 3:
                show_grades_category(db, index)
        print()
        if sum_percentages(db) != 100: # Keeps track of all the percentage values and warms user if the percentage total is over 100
            print("WARNING: Category percentages don't add up to 100.")
            print('Current category percentages comprise {} of the total.'.format(sum_percentages(db)))
        print()
        print('Grade calculation:')
        for index, value in db.items():
            if len(value) != 3:
                decimal = value[1]/100 # Transforms the percentage to decimal for formating purposes
                print('{} = 0 * {} = 0.00 '.format(value[0], decimal))
            else:
                avg = get_avg_grade(value[2]) # This occurs if the function does have a grade list
                decimal = value[1]/100
                weight = avg * decimal
                total += weight
                print('{} = {:.1f} * {} = {:.2f} '.format(value[0], avg, decimal, weight))
        print('Total grade = {:.1f}'.format(total))

# Option 8

def save_data(db): 
    default = 'grade_save.csv' # Setting a default name for the file
    if len(db) == 0:
        print('There are no categories.') # Most this is just face and where to get the data to save to the file
        print('Skipping the creation of an empty file.')
        return 0
    else:
        list_categories(db)
        print('::: Save to the default file {}? Type Y or N'.format(default))
        ans = input('>')
        if ans == 'Y':
            print('Saving the database in {}'.format(default))
            print('Database contents:{}'.format(db))
        elif ans == 'N':
            print('File name to save database to')
            default = input('>') # Checks if you want save the database to another file
            print('Saving the database in {}'.format(default))
            print('Database contents:{}'.format(db))
        save_dict_to_csv(db, default)

            

def save_dict_to_csv(db, filename):
    import csv
    info = [] # Setting a local varaible to empty list
    for id, items in db.items():
        if len(db[id]) == 3: # Checking if the data we want to save has a list or not. Also indexing values to input specific data in a specific location
            key = id
            category =items[0] 
            percent = items[1]
            grades = items[2]
            data = [key, category, percent] 
            for val in grades:
                data.append(val)
        elif len(db[id]) == 2:
            key = id
            category = items[0]
            percent = items[1]
            data = [key, category, percent]
        info.append(data)

        with open(filename, 'w', newline ='') as f: # Writes the data into a file
            writer = csv.writer(f)
            writer.writerows(info)


# Option 9

def load_dict_from_csv(filename): # We get a file name to use as our input
    import csv
    import os
    p = os.path.join(filename)
    if os.path.exists(p): # Checks to see if the file exist on your computer
        with open(filename, 'r') as f:
            data_dictionary = {}
            grade_list = []
            lines = csv.reader(f)
            for dl in lines: # Here we test to see if the function is empty or has values and if the grade list is included
                if len(dl) == 0:
                    return {}
                elif len(dl) == 3:
                    data_dictionary[int(dl[0])] = [dl[1], float(dl[2])] # Final formating without the grades
                else:
                    grade_list = ((dl[3:]))
                    for i, val in enumerate(grade_list):
                        val = float(val)
                        grade_list[i] = val
                    data_dictionary[int(dl[0])] = [dl[1], float(dl[2]), grade_list] # Final formating with the grades
        return (data_dictionary)     
    else:
        print("WARNING: Cannot find a CSV file named '{}'".format(p))
        return



def load_data(db):
    default = 'grade_save.csv' # The default file
    print('::: Load the default file ({})? Type Y or N'.format(default))
    ans = input('>')
    if ans == 'Y':
        db.update(load_dict_from_csv(default)) # Using the update function to update the database with new information
    elif ans == 'N':
        print('::: Enter the name of the csv file to load.')
        default = input('>')
        while default[-4:] != '.csv':
            print('WARNING: data.txt does not end with `.csv`')
            print('::: Enter the name of an existing csv file.') 
            default = input('>')
        print('Reading the database from data.csv')
        load_dict_from_csv(default)






def print_main_menu(X):
    print('**************************') # Prints 26 stars and loops for as dictionary entries there are
    print('What would you like to do?')
    for i, key in enumerate(X):  
        if i == 9:
            print('Q', ':', X[key])
        else:
            print(i + 1, ':', X[key])
    print('**************************')


def check_option(option, menu):
    for x in menu.keys():   # Checks to see if the inputed option exist in the dictionary and if the input is valid
        if (str(x) == option):
            return 'valid'
    if str(option).isdigit() != True:
        print("Warning: `{}` is not an integer".format(option))
        print('Please enter an integer.')
        return 'invalid'
    else:
        print(" Warning: `{}` is not a valid option".format(option))
        print('Please enter a valid option.')
        return 'invalid'

if __name__ == "__main__":
    the_menu = {'1': 'List categories', 
                '2': 'Add a category', 
                '3': 'Update a category', 
                '4': 'Delete a category',
                '5': 'Add grades',
                '6': 'Show grades',
                '7': 'Grade statistics',
                '8': 'Save the data',
                '9':'Upload data from file',
                'Q' :'Quit this program'}

    main_db = {} # stores the grading categories and info
    max_cat = 10 # the max total num of categories a user can provide
    cat_id_offset = 100 # the starting value for the category ID

    opt = None

    while True:
        print_main_menu(the_menu)
        print("::: Enter an option")
        opt = input("> ")

        if opt == 'q' or opt == 'Q':
            print("Goodbye")
            break
        else:
            if check_option(opt, the_menu) == "invalid": # TODO 3: implement check_option
                continue
            print("You selected option {} to > {}.".format(opt, the_menu[opt]))

        if opt == '1':
            list_categories(main_db)
        elif opt == '2':
            add_categories(main_db, max_cat, cat_id_offset)
        elif opt == '3':
            update_category(main_db)
        elif opt == '4':
            delete_category(main_db)
        elif opt == '5':
            add_grades(main_db)
        elif opt == '6':
            show_grades(main_db)
        elif opt == '7':
            grade_stats(main_db)
        elif opt == '8':
            save_data(main_db)
        elif opt == '9':
            load_data(main_db)
        else:
            print("This option is not yet implemented.") # TODO: implement it

        opt = input("::: Press Enter to continue...")

    print("See you next time!")
    
