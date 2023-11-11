contestants = [
    ["Binkie", 1, False, []],
    ["Butterball", 3, True, ["herding sheep", "singing", "fetch", "pulling sleds"]],
    ["Kerby", 5, True, ["swimming"]],
    ["Lucy", 5, False, ["fetch", "solving puzzles"]],
    ["Toaster", 2, False, []],
    ["Fifi", 1, False, []],
    ["Noodles", 4, True, ["pulling sleds"]]
]
labels = ["name", "age", "does_tricks", "other_talents"]

def no_puppies_allowed(list1):
    """function to remove dogs age 1 and under"""
    #list comprehension removing any dogs age 1 and under
    return [age for age in list1 if age[1] > 1]
#put function into no_puppies variable for next function
no_puppies = no_puppies_allowed(contestants)

def lists_to_dicts(key_list, value_list):
    """Function to take dog lists and turn them into dictionaries
    arguments:
        key_list: list of labels to use as keys 
        value_list: list of dog traits to use as values 
    
    keys: labels 
    values: contestant information
    """
    #empty list to append dictionaries to
    dict_list = []
    #nested = values for dogs
    for nested in value_list:
        #zipped key_list with nested values. Wrapped into dict
        dict1 = dict(zip(key_list, nested))
        #append dicts to empty dict_list
        dict_list.append(dict1)
    return dict_list

dog_dict = lists_to_dicts(labels, no_puppies)

def assign_points(list2):
    """Function to assign 'points' key and integer value to each dog
    dogs get:
        1 point if they do tricks, 0 if they do not
        1 point for each special talent they possess
    """
    for dict1 in list2:
        #assign variable to the integer 0 so we can add to it
        x = 0
        #gives 1 point to the dog if 'does_tricks' = True
        if True in dict1.values():
            x += 1
        #gives 1 point to each dog per 'other_talents' present
        for k, v in dict1.items():
            #adds to x based on length of 'other_talents' value(s)
            if k == "other_talents":
                x += len(v)
        #append the point total to dog's 'points' value
        dict1["points"] = x
    return list2
dict_with_points = assign_points(dog_dict)

def most_points(list3):
    """Function to find the dog with the most points, and 
       congratulate that dog on winning the contest
    """
    #used lambda function to find specific value from key x 
    #used max() to find dict with largest value in 'points'
    dog_with_most_points = max(dict_with_points, key=lambda x:x['points'])
    #put dict with largest 'points' value into variable dog_with_most_points
    print(f"Congratulations! {dog_with_most_points['name']} is the official winner of the DataStack Dog Contest!")




