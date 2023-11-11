from dog import no_puppies_allowed
from dog import lists_to_dicts
from dog import assign_points
from dog import most_points

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

def main(key_list, value_list):
    no_puppies = no_puppies_allowed(value_list)
    dog_dict = lists_to_dicts(key_list, no_puppies)
    dict_with_points = assign_points(dog_dict)
    most_points(dict_with_points)

main(labels, contestants)