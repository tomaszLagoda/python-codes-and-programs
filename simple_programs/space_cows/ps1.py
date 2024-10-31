from ps1_partition import get_partitions
from typing import Dict
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(f'/home/tomasz/Pulpit/python-codes-and-programs/simple_programs/space_cows/' + filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if not cows:
        return [[]]

    trips,  already_processed = [], []

    cows_organized = sorted(cows.items(), key= lambda item: item[1], reverse=True)

    # Loop untill all cows are processed
    while len(cows_organized) > len(already_processed):
        current_trip = []
        current_cargo = 0
        for name, weight in cows_organized:
            if name in already_processed:
                continue;
            
            # When cow weight exceed the cargo limit, do not take the cow
            if limit < weight:
                already_processed.append(name)
                continue

            if current_cargo + weight <= limit:
                current_trip.append(name)
                current_cargo += weight
                already_processed.append(name)

        if current_trip:
            trips.append(current_trip)
     
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    if not cows:
        return [[]]
    
    best_list = []
    weighted_list = []

    for partition in get_partitions(cows):
        weights = []
        exceed_cargo_limit = False

        for trip in partition:
            trip_weight = 0
            for name in trip:
                trip_weight += cows[name]
            weights.append((trip, trip_weight))

            if trip_weight > limit:
                exceed_cargo_limit = True
        
        if weights and not exceed_cargo_limit:
            weighted_list.append((weights))

    for l, weight in sorted(weighted_list, key=len).pop(0):
        best_list.append(l)

    return best_list

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)


start = time.time()
## code to be timed
print(greedy_cow_transport(cows, limit))
end = time.time()
print(end - start)



start = time.time()
## code to be timed
print(brute_force_cow_transport(cows, limit))
end = time.time()
print(end - start)



