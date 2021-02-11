###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def recursion(egg_weights, target_weight, choice, memo={}):
    if target_weight == 0 or (not bool(egg_weights)):
        return len(choice), choice
    elif egg_weights[-1] > target_weight:
        # right branch only
        return recursion(egg_weights[:-1], target_weight, list(choice))
    else:
        item = egg_weights[-1]
        left_choice = list(choice) + [item]
        # check if finished
        if target_weight - item == 0:
            return len(left_choice), left_choice
        else:
            # go deeper into rabbit hole
            left, result = recursion(egg_weights, target_weight - item, left_choice)

        # when we only have 1 choice and already choose it (left), than we must use left
        if len(egg_weights) == 1:
            return len(result), result

        right_choice = list(choice)
        right, result = recursion(egg_weights[:-1], target_weight, right_choice)

        if left <= right:
            result = choice + left_choice
        else:
            result = choice + right_choice

        return len(result), result

def dp_make_weight(egg_weights, target_weight, memo={}):
    length, result = recursion(egg_weights, target_weight, [], memo)
    print(result)
    return length

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    # egg_weights = (1, 5, 10, 25)
    egg_weights = (1, 2)
    n = 3
    print(f"Egg weights = {egg_weights}")
    print(f"n = {n}")
    # print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
