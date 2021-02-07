###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
from operator import itemgetter
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    # TODO: Your code here
    content = {}
    with open(filename) as f:
        for line in f:
            cow, weight = line.split(',')
            content[cow] = int(weight)
    return content


# Problem 2
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
    cows = [(key, value) for key, value in cows.items()]
    sorted_cows = sorted(cows, key=itemgetter(1))
    trips = []
    while len(sorted_cows) > 0:
        current_load = 0
        current_trip = []
        while current_load <= limit and len(sorted_cows):
            cow, weight = sorted_cows[-1]
            if current_load + weight <= limit:
                current_load += weight
                current_trip.append(cow)
                sorted_cows.pop()
            else:
                # no space left
                break
        trips.append(current_trip)

    return trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    cows = [(key, value) for key, value in cows.items()]
    candidates = []
    for combination in get_partitions(cows):
        # sanity check: check if every list is in limit
        all_valid = True
        for trip in combination:
            current_trip_weight = 0
            for cow, weight in trip:
                current_trip_weight += weight
            if current_trip_weight > limit:
                all_valid = False
                break

        if all_valid:
            candidates.append(combination)

    # find the candidates with minimal trips
    current_shortest_length, best_candidate = None, None
    for candidate in candidates:
        if current_shortest_length is None:
            current_shortest_length = len(candidate)
            best_candidate = candidate
        elif len(candidate) < current_shortest_length:
            current_shortest_length = len(candidate)
            best_candidate = candidate

    # print(len(best_candidate))
    # print(best_candidate)
    # insert only names in result
    return [[name for name, weight in sub] for sub in best_candidate] 
        
# Problem 4
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
    d = load_cows('ps1_cow_data_2.txt')
    start = time.time()
    greedy_result = greedy_cow_transport(d, limit=10)
    end = time.time()
    print(f"Greedy Length: {len(greedy_result)}, time: {end - start:.6f}")

    start = time.time()
    brute_result = brute_force_cow_transport(d, limit=10)
    end = time.time()
    print(f"Brute Length: {len(brute_result)}, time: {end - start:.6f}")
